
import argparse as ap
import csv
import os

from PipelineConfig import PIPELINE_FOLDER

def write_notes(example_folder, fp):
    notes_fn = f'{example_folder}/notes.md'
    if os.path.exists(notes_fn):
        fpi = open(notes_fn, 'rt')
        for l in fpi:
            fp.write(l)
        fp.write('\n')

def write_reference(example_folder, fp):
    fp.write('## Reference sequences\n')

    ref_fp = open(f'{example_folder}/inputs/reference.fa', 'rt')
    ref_content = ref_fp.read()
    ref_fp.close()

    fp.write(f'```\n{ref_content.rstrip()}\n```\n')

def write_truth_vcf(example_folder, fp):
    fp.write('## Truth variants\n')

    vfp = open(f'{example_folder}/inputs/truth.vcf', 'rt')
    lines = []
    for l in vfp:
        if l.startswith('##'):
            continue
        lines.append(l.rstrip())
    vfp.close()

    join_lines = '\n'.join(lines)
    fp.write(f'```\n{join_lines}\n```\n')

def write_query_vcf(example_folder, fp):
    fp.write('## Query variants\n')

    vfp = open(f'{example_folder}/inputs/query.vcf', 'rt')
    lines = []
    for l in vfp:
        if l.startswith('##'):
            continue
        lines.append(l.rstrip())
    vfp.close()

    join_lines = '\n'.join(lines)
    fp.write(f'```\n{join_lines}\n```\n')

def write_summary(example_folder, fp):
    fp.write('## Output summary\n')

    columns = ['Variant Type', 'Metric', 'Hap.py-GT', 'Aardvark-GT', 'Aardvark-Basepair']
    column_align = [':--', ':--', '--:', '--:', '--:']
    variant_order = ['ALL', 'SNV', 'INDEL']
    metric_order = ['F1', 'Recall', 'Precision']

    fp.write(' | '.join(columns)+'\n')
    fp.write(' | '.join(column_align)+'\n')

    happy_summary = load_happy_summary(f'{example_folder}/happy/happy.summary.csv')
    aardvark_summary = load_aardvark_summary(f'{example_folder}/aardvark/summary.tsv')

    for vt in variant_order:
        for metric in metric_order:

            h_gt_metric = happy_summary.get(vt, {}).get(metric, '--')
            h_gt_support = happy_summary.get(vt, {}).get(f'{metric}_ratio', '')
            if h_gt_support != '':
                h_gt_support = f' ({h_gt_support})'
            h_gt = f'{h_gt_metric}{h_gt_support}'

            a_gt_metric = aardvark_summary.get((vt, 'GT'), {}).get(metric, '--')
            a_gt_support = aardvark_summary.get((vt, 'GT'), {}).get(f'{metric}_ratio', '')
            if a_gt_support != '':
                a_gt_support = f' ({a_gt_support})'
            a_gt = f'{a_gt_metric}{a_gt_support}'

            a_bp_metric = aardvark_summary.get((vt, 'BASEPAIR'), {}).get(metric, '--')
            a_bp_support = aardvark_summary.get((vt, 'BASEPAIR'), {}).get(f'{metric}_ratio', '')
            if a_bp_support != '':
                a_bp_support = f' ({a_bp_support})'
            a_bp = f'{a_bp_metric}{a_bp_support}'

            row = [
                vt, metric,
                h_gt,
                a_gt,
                a_bp,
            ]
            fp.write(' | '.join(row)+'\n')

def write_msa(example_folder, fp):
    fp.write('## MSA visualization\n')
    fp.write('![](./msa_viz/msa.png)\n')

def load_happy_summary(fn):
    ret = {}
    fp = open(fn, 'r')
    csv_reader = csv.DictReader(fp)

    vt_remap = {
        'SNP' : 'SNV'
    }
    for row in csv_reader:
        if row['Filter'] == 'ALL':
            vt = row['Type']
            vt = vt_remap.get(vt, vt)
            assert(vt not in ret)

            truth_tp = int(row['TRUTH.TP'])
            truth_fn = int(row['TRUTH.FN'])
            recall_ratio = f'{truth_tp}/{truth_tp+truth_fn}'

            query_total = int(row['QUERY.TOTAL'])
            query_fp = int(row['QUERY.FP'])
            precision_ratio = f'{query_total - query_fp}/{query_total}'

            ret[vt] = {
                'F1' : row['METRIC.F1_Score'],
                'Recall' : row['METRIC.Recall'],
                'Precision' : row['METRIC.Precision'],
                'Recall_ratio' : recall_ratio,
                'Precision_ratio' : precision_ratio
            }
    fp.close()
    return ret

def load_aardvark_summary(fn):
    ret = {}
    fp = open(fn, 'r')
    csv_reader = csv.DictReader(fp, delimiter='\t')

    vt_remap = {
        'Snv' : 'SNV',
        'JointIndel' : 'INDEL'
    }
    for row in csv_reader:
        if row['filter'] == 'ALL':
            vt = row['variant_type']
            vt = vt_remap.get(vt, vt)

            ct = row['comparison']
            assert((vt, ct) not in ret)
            truth_tp = int(row['truth_tp'])
            truth_fn = int(row['truth_fn'])
            recall_ratio = f'{truth_tp}/{truth_tp+truth_fn}'

            query_tp = int(row['query_tp'])
            query_fp = int(row['query_fp'])
            precision_ratio = f'{query_tp}/{query_tp+query_fp}'

            ret[(vt, ct)] = {
                'F1' : row['metric_f1'],
                'Recall' : row['metric_recall'],
                'Precision' : row['metric_precision'],
                'Recall_ratio' : recall_ratio,
                'Precision_ratio' : precision_ratio
            }
    fp.close()
    return ret

if __name__ == '__main__':
    description = 'Summarizes the benchmark outputs into a markdown file at the example root'
    p = ap.ArgumentParser(description=description, formatter_class=ap.RawTextHelpFormatter)

    #things we want to generate
    p.add_argument('-e', '--example', dest='example_id', required=True, help='example identifier')
    
    args = p.parse_args()

    # pull the folder location
    example = args.example_id
    example_folder = f'{PIPELINE_FOLDER}/examples/{example}'
    
    fp = open(f'{example_folder}/README.md', 'w+')

    fp.write(f'# Example `{example}`\n')
    write_notes(example_folder, fp)
    write_reference(example_folder, fp)
    write_truth_vcf(example_folder, fp)
    write_query_vcf(example_folder, fp)
    write_summary(example_folder, fp)
    write_msa(example_folder, fp)

    fp.close()
