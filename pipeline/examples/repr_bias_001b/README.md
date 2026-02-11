# Example `repr_bias_001b`
## Notes
This example was generated in conjunction with [repr_bias_001a](../repr_bias_001a) to demonstrate how variant representation can bias GT scoring.
In this example, the query variants are represented as a single tandem-repeat call for the region.
When scored, the entire event is labeled as false, despite being partially correct (the SNP component is correct).
The genotype scores for this example is different from repr_bias_001a despite having identical underlying haplotype sequences.

In contrast, the basepair score is identical to that from repr_bias_001a because the variants represent the same genomic variants in alternate forms.

This example was generated manually using a real event in a tandem repeat within the human genome: `chr1:61,593,380-61,593,419`.

## Reference sequences
```
>mock
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
TGAAAAAAAAAAAGAAAAAAAAAAAACCCCCCCCCCCCCCCCCCCCCCCC
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
```
## Truth variants
```
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	truth
mock	76	.	A	T	40	.	.	GT	1/1
```
## Query variants
```
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	query
mock	64	.	GAAAAAAAAAAAA	GAAAAAAAAAAT	40	.	.	GT	1/1
```
## Output summary
Variant Type | Metric | Hap.py-GT | Aardvark-GT | Aardvark-Basepair
:-- | :-- | --: | --: | --:
ALL | F1 | -- | NaN | 0.6666666666666666
ALL | Recall | -- | 0.0 (0/1) | 1.0 (4/4)
ALL | Precision | -- | 0.0 (0/1) | 0.5 (4/8)
SNV | F1 |  |  | 
SNV | Recall | 0.0 (0/1) | 0.0 (0/1) | 1.0 (4/4)
SNV | Precision | 0.0 (0/1) |  (0/0) |  (0/0)
INDEL | F1 |  |  | 
INDEL | Recall | 0.0 (0/0) |  (0/0) |  (0/0)
INDEL | Precision | 0.0 (0/1) | 0.0 (0/1) | 0.5 (4/8)
## MSA visualization
![](./msa_viz/msa.png)
