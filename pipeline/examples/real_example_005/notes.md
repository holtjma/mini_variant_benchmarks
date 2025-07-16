## Notes
This captures a real example that is found in `chr1:71262162-71262275` in GIAB v4.2.1.
The query variants are pulled from a HiFi sequencing run for HG001.
In this example, the HiFi variant calling has produced two indel variants that collective are the same sequence as the SNP variant.

Aardvark-GT selects the two indels as TP and marks the SNP as a FP, whereas Hap.py marks the SNP as TP and the two indels as FP.
In constrast, the Aardvark-Basepair score recognizes that the variants represent a two basepair change (one per haplotype), and that the two indels should cancel each other out.
This results in a false positive basepair assignment.