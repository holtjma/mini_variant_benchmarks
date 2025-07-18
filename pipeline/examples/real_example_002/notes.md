## Notes
This captures a real example that is found in `chr1:35692923-35693038` in GIAB v4.2.1.
The query variants are pulled from a HiFi sequencing run for HG001.
In this example, the HiFi variant calling is partially correct, but it erroneously adds an insertion and deletion pair that combined create the same sequence as the single SNP.
This is an example where the variant calling software is creating variants that are fundamentally incompatible with each other.

Hap.py selects the homozygous SNP as a TP, and marks both indels as FP.
Aardvark finds identical sequences, but instead selects the two indels as TP and the SNP is marked as half-correct (i.e., one is a FP), which increases the GT precision to 2/3.
Lastly, Aardvark-Basepair identifies that the SNP variant is found, but that something (whether the SNP or indel) is injecting extra sequence into one of the query haplotypes, lowering the ALL precision to 0.66.
