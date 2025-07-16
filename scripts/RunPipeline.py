
import argparse as ap
import os

from PipelineConfig import *

if __name__ == '__main__':
    description = 'Runs the benchmarking examples and gathers outputs at the end'
    p = ap.ArgumentParser(description=description, formatter_class=ap.RawTextHelpFormatter)

    #standard options we have for all snakemake pipelines
    p.add_argument('-x', '--execute', dest='execute', action='store_true', default=False, help='execute the commands (default: False)')
    p.add_argument('-C', '--clean', dest='clean', action='store_true', default=False, help='clean all output files (default: False)')
    p.add_argument('-A', '--all', dest='target_all', action='store_true', default=False, help='target all outputs files (default: False)')

    #things we want to generate
    p.add_argument('-e', '--create-examples', dest='example_gen', action='store_true', default=False, help='generates the full example VCFs (default: False)')
    p.add_argument('-a', '--aardvark', dest='aardvark', action='store_true', default=False, help='generate aardvark results (default: False)')
    p.add_argument('-r', '--happy', dest='happy', action='store_true', default=False, help='generate happy results (default: False)')
    p.add_argument('-m', '--markdown', dest='markdown', action='store_true', default=False, help='generate markdown summaries (default: False)')

    # profile is required
    p.add_argument('--profile', dest='profile', default=None, required=True, help='run the commands using a provided snakemake profile')

    args = p.parse_args()

    #generate all the targets from the above commands
    targets = []
    if args.target_all or args.example_gen:
        targets.append('generate_all_examples')

    if args.target_all or args.aardvark:
        targets.append('aardvark_summary')

    if args.target_all or args.happy:
        targets.append('happy_summary')

    if args.target_all or args.markdown:
        targets.append('markdown_summary')
    
    snakemake_frags = [
        'snakemake',
        #standard options
        '--printshellcmds',
        '--keep-going',
        '--use-conda',
        '--use-singularity', f'--singularity-args "-B {PROJECT_DIR} --cleanenv"',
        '--jobs', '1000',
        #things we need to pass/configure
        '--profile', args.profile,
        '--snakefile', SNAKEFILE
    ]

    if not args.execute:
        print('Dry run only: enabled')
        snakemake_frags.append('--dry-run')
    
    if args.clean:
        print('Clean-up: enabled')
        snakemake_frags.append('--delete-all-output')

    if len(targets) > 0:
        snakemake_frags += targets
        cmd = ' '.join(snakemake_frags)
        print(cmd)
        ret_code = os.system(cmd)
        if ret_code != 0:
            raise Exception(f'Snakemake error {ret_code}, see above')
    else:
        print('WARNING: No targets specified, exiting without doing any work.')
