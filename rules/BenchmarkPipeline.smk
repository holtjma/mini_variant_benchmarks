
import glob

#special work to get pipeline config in here
snakefile = workflow.snakefile
scripts_folder = os.path.dirname(os.path.dirname(snakefile))+'/scripts'
sys.path.append(scripts_folder)
from PipelineConfig import *

#######################################################################
# Functions to pull files from pipeline area
#######################################################################



#######################################################################
# Primary root rules
#######################################################################

def get_example_folders():
    example_folders = sorted(glob.glob(f'{PIPELINE_FOLDER}/examples/*'))
    return example_folders

def get_all_example_files():
    ret = []
    example_folders = get_example_folders()
    for ef in example_folders:
        ret.append(f'{ef}/preprocessing/truth.vcf.gz')
        ret.append(f'{ef}/preprocessing/truth.vcf.gz.tbi')
        ret.append(f'{ef}/preprocessing/query.vcf.gz')
        ret.append(f'{ef}/preprocessing/query.vcf.gz.tbi')
    return ret

rule generate_all_examples:
    input:
        get_all_example_files()

def get_aardvark_calls():
    ret = []
    example_folders = get_example_folders()
    for ef in example_folders:
        ret.append(f'{ef}/aardvark/summary.tsv')
    return ret

rule aardvark_summary:
    input:
        get_aardvark_calls()

def get_happy_calls():
    ret = []
    example_folders = get_example_folders()
    for ef in example_folders:
        ret.append(f'{ef}/happy/happy.summary.csv')
    return ret

rule happy_summary:
    input:
        get_happy_calls()

def get_markdown_summaries():
    ret = []
    example_folders = get_example_folders()
    for ef in example_folders:
        ret.append(f'{ef}/README.md')
    return ret

rule markdown_summary:
    input:
        get_markdown_summaries()

#######################################################################
# Pre-processing rules
#######################################################################

rule bgzip_index:
    input:
        vcf="{pipeline}/examples/{example}/inputs/{root}.vcf"
    output:
        vcf="{pipeline}/examples/{example}/preprocessing/{root}.vcf.gz",
        index="{pipeline}/examples/{example}/preprocessing/{root}.vcf.gz.tbi"
    params:
    resources:
        mem_mb=1*1024,
        runtime=5 # minutes
    threads: 1
    conda: f'{ENV_FOLDER}/bcftools_1.15.1.yaml'
    log: "{pipeline}/examples/{example}/logs/{root}_bgzip_index.log"
    benchmark: "{pipeline}/examples/{example}/benchmark/{root}_bgzip_index.log"
    shell: '''
        cat {input.vcf} | bgzip > {output.vcf}
        tabix {output.vcf}
    '''

rule faidx:
    input:
        reference="{pipeline}/examples/{example}/inputs/reference.fa"
    output:
        index="{pipeline}/examples/{example}/inputs/reference.fa.fai"
    params:
    resources:
        mem_mb=1*1024,
        runtime=5 # minutes
    threads: 1
    conda: f'{ENV_FOLDER}/samtools.yaml'
    log: "{pipeline}/examples/{example}/logs/ref_faidx.log"
    benchmark: "{pipeline}/examples/{example}/benchmark/ref_faidx.log"
    shell: '''
        samtools faidx {input.reference}
    '''

#######################################################################
# Comparison rules
#######################################################################

rule aardvark:
    input:
        binary=AARDVARK_BINARY,
        reference="{pipeline}/examples/{example}/inputs/reference.fa",
        call_regions="{pipeline}/examples/{example}/inputs/regions.bed",
        truth_vcf="{pipeline}/examples/{example}/preprocessing/truth.vcf.gz",
        query_vcf="{pipeline}/examples/{example}/preprocessing/query.vcf.gz",
    output:
        summary="{pipeline}/examples/{example}/aardvark/summary.tsv",
        reg_seq="{pipeline}/examples/{example}/aardvark_debug/region_sequences.tsv.gz",
        out_folder=directory("{pipeline}/examples/{example}/aardvark"),
        debug_folder=directory("{pipeline}/examples/{example}/aardvark_debug")
    params:
    resources:
        mem_mb=4*1024,
        runtime=5 #minutes
    threads: 1
    log: "{pipeline}/examples/{example}/logs/aardvark.log"
    benchmark: "{pipeline}/examples/{example}/benchmark/aardvark.log"
    shell: '''
        {input.binary} \
            compare \
            --threads {threads} \
            --reference {input.reference} \
            --truth-vcf {input.truth_vcf} \
            --query-vcf {input.query_vcf} \
            --regions {input.call_regions} \
            --output-dir {output.out_folder} \
            --output-debug {output.debug_folder}
        '''

rule happy:
    input:
        reference="{pipeline}/examples/{example}/inputs/reference.fa",
        ref_index="{pipeline}/examples/{example}/inputs/reference.fa.fai",
        call_regions="{pipeline}/examples/{example}/inputs/regions.bed",
        truth_vcf="{pipeline}/examples/{example}/preprocessing/truth.vcf.gz",
        query_vcf="{pipeline}/examples/{example}/preprocessing/query.vcf.gz",
    output:
        summary_fn="{pipeline}/examples/{example}/happy/happy.summary.csv"
    params:
        out_prefix="{pipeline}/examples/{example}/happy/happy"
    singularity: "docker://pkrusche/hap.py:v0.3.9"
    resources:
        mem_mb=4*1024,
        runtime=10 #minutes
    threads: 1
    log: "{pipeline}/examples/{example}/logs/happy.log"
    benchmark: "{pipeline}/examples/{example}/benchmark/happy.log"
    shell: '''
    /opt/hap.py/bin/hap.py \
        --threads {threads} \
        -o {params.out_prefix} \
        -r {input.reference} \
        -f {input.call_regions} \
        --engine=vcfeval \
        {input.truth_vcf} \
        {input.query_vcf}
    '''

#######################################################################
# Analysis rules
#######################################################################

rule msa_viz:
    input:
        script=f'{SCRIPTS_FOLDER}/CreateMSA.py',
        reg_seq="{pipeline}/examples/{example}/aardvark_debug/region_sequences.tsv.gz",
    output:
        out_folder=directory("{pipeline}/examples/{example}/msa_viz"),
        png="{pipeline}/examples/{example}/msa_viz/msa.png",
    params:
    resources:
        mem_mb=1*1024,
        runtime=5 #minutes
    threads: 1
    conda: f'{ENV_FOLDER}/spoa_pymsaviz.yaml'
    log: "{pipeline}/examples/{example}/logs/msa_viz.log"
    shell: '''
        python3 -u {input.script} \
            --region-id 0 \
            --region-sequences {input.reg_seq} \
            --out-folder {output.out_folder}
    '''

def optional_notes(wildcards):
    note_fn = f'{wildcards.pipeline}/examples/{wildcards.example}/notes.md'
    if os.path.exists(note_fn):
        return [note_fn]
    else:
        return []

localrules: generate_summary
rule generate_summary:
    input:
        script=f'{SCRIPTS_FOLDER}/CreateSummaryMarkdown.py',
        aardvark_summary="{pipeline}/examples/{example}/aardvark/summary.tsv",
        happy_summary="{pipeline}/examples/{example}/happy/happy.summary.csv",
        msa_png="{pipeline}/examples/{example}/msa_viz/msa.png",
        opt_notes=optional_notes,
    output:
        readme="{pipeline}/examples/{example}/README.md"
    params:
    resources:
        mem_mb=1*1024,
        runtime=5 #minutes
    threads: 1
    log: "{pipeline}/examples/{example}/logs/generate_summary.log"
    shell: '''
        python3 -u {input.script} \
            -e {wildcards.example}
    '''
