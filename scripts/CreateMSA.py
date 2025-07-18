
import argparse as ap
import csv
import gzip
import os
from pymsaviz import MsaViz, get_msa_testdata

def load_sequences(fn, region_id):
    fp = gzip.open(fn, 'rt')
    tsv_reader = csv.DictReader(fp, delimiter='\t')

    row_val = None
    for row in tsv_reader:
        if row['region_id'] == region_id:
            row_val = row
            break
    fp.close()

    if row_val == None:
        print(f"No region found with id: \"{region_id}\", creating null result")
        row_val = {
            'ref_seq' : 'N',
            'truth_seq1' : 'N',
            'truth_seq2' : 'N',
            'query_seq1' : 'N',
            'query_seq2' : 'N'
        }
    return row_val

def generate_fasta(seq_dict, out_fn):
    fp = open(out_fn, 'w+')
    seq_order = ['ref_seq', 'truth_seq1', 'query_seq1', 'truth_seq2', 'query_seq2']
    for seq_key in seq_order:
        fp.write(f'>{seq_key}\n')
        fp.write(f'{seq_dict[seq_key]}\n')
    fp.close()

def run_muscle(fasta_fn, out_txt):
    cmd = f'muscle -align {fasta_fn} -output {out_txt}.raw'
    ret = os.system(cmd)
    if ret != 0:
        raise Exception("Error while running MUSCLE")
    
    # we need to reorder the outputs now
    fp = open(f'{out_txt}.raw', 'r')
    seq_dict = {}
    k = None
    s = ''
    for l in fp:
        if l.startswith('>'):
            if k != None:
                seq_dict[k] = s
            k = l.rstrip()[1:]
            s = ''
        else:
            s += l.rstrip()
    if k != None:
        seq_dict[k] = s
    fp.close()

    fpo = open(out_txt, 'w+')
    seq_order = ['ref_seq', 'truth_seq1', 'query_seq1', 'truth_seq2', 'query_seq2']
    for k in seq_order:
        fpo.write(f'>{k}\n')
        fpo.write(f'{seq_dict[k]}\n')
    fpo.close()

def run_spoa(fasta_fn, out_fn):
    cmd = f'spoa -l1 -r1 {fasta_fn} > {out_fn}'
    ret = os.system(cmd)
    if ret != 0:
        raise Exception("Error while running SPOA")

def run_pymsaviz(muscle_txt, out_png):
    #mv = MsaViz(muscle_txt, color_scheme='Identity', wrap_length=200, show_count=True)
    mv = MsaViz(muscle_txt, wrap_length=200, show_count=True)
    mv.set_custom_color_func(custom_color)
    mv.savefig(out_png)

def custom_color(row_pos, col_pos, seq_char, msa):
    '''
    Custom color scheme function that will compare the truth and query rows.
    Anything that matches is colored green, and anything that does not is colored purple
    '''
    all_match = True
    for x in range(1, 5):
        all_match &= (msa[0, col_pos] == msa[x, col_pos])

    identity_color = 'lightblue'
    ref_color = 'white'
    match_color = 'lightgreen'
    mismatch_color = 'violet'

    if all_match:
        # identity column
        color = identity_color
    elif seq_char == '-' or row_pos == 0:
        # same as reference character
        color = ref_color
    elif row_pos == 1 or row_pos == 3:
        # truth value, need to compare
        if seq_char != msa[row_pos+1, col_pos]:
            color = mismatch_color
        elif seq_char == msa[0, col_pos]:
            color = ref_color
        else:
            color = match_color
    else:
        # query value, need to compare
        if seq_char != msa[row_pos-1, col_pos]:
            color = mismatch_color
        elif seq_char == msa[0, col_pos]:
            color = ref_color
        else:
            color = match_color
    return color

if __name__ == '__main__':
    description = 'Runs both MUSCLE and pymsaviz to generate a MSA and visual'
    p = ap.ArgumentParser(description=description, formatter_class=ap.RawTextHelpFormatter)

    # options
    p.add_argument('-r', '--region-id', dest='region_id', default='0', help='the region_id to visualize (default: 0)')

    # requirements
    p.add_argument('-s', '--region-sequences', dest='region_sequences', required=True, help='the region_sequences.tsv.gz file from Aardvark')
    p.add_argument('-o', '--out-folder', dest='out_folder', required=True, help='the output folder to create and populate')

    args = p.parse_args()

    if not os.path.exists(args.out_folder):
        os.makedirs(args.out_folder)

    # first, load the sequences
    sequences = load_sequences(args.region_sequences, args.region_id)

    # then generate a FASTA file
    fasta_fn = f'{args.out_folder}/sequences.fa'
    generate_fasta(sequences, fasta_fn)

    # ...and run MUSCLE on it
    #out_muscle = f'{args.out_folder}/muscle.txt'
    #run_muscle(fasta_fn, out_muscle)

    # ...and run SPOA on it
    out_spoa = f'{args.out_folder}/spoa.fa'
    run_spoa(fasta_fn, out_spoa)
    
    # last, generate our figure
    out_png = f'{args.out_folder}/msa.png'
    # run_pymsaviz(out_muscle, out_png)
    run_pymsaviz(out_spoa, out_png)
