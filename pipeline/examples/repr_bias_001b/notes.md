## Notes
This example was generated in conjunction with [repr_bias_001a](../repr_bias_001a) to demonstrate how variant representation can bias GT scoring.
In this example, the query variants are represented as a single tandem-repeat call for the region.
When scored, the entire event is labeled as false, despite being partially correct (the SNP component is correct).
The genotype scores for this example is different from repr_bias_001a despite having identical underlying haplotype sequences.

In contrast, the basepair score is identical to that from repr_bias_001a because the variants represent the same genomic variants in alternate forms.

This example was generated manually using a real event in a tandem repeat within the human genome: `chr1:61,593,380-61,593,419`.
