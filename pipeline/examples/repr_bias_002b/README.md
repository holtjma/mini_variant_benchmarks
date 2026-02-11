# Example `repr_bias_002b`
## Notes
This example was generated in conjunction with [repr_bias_002a](../repr_bias_001a) to demonstrate how variant representation can bias GT scoring.
In this example, the query variants are represented as a single complex indel.
When scored, both Hap.py and aardvark-GT label that event as a FP, and all truth variants as FN.

In contrast, the basepair scoring is identical to the results of repr_bias_002a because the variants represent the same genomic changes.
## Reference sequences
```
>mock
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
GAAAAGAAAAAAAAAAAATATATCCCCCCCCCCCCCCCCCCCCCCCCCCC
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
```
## Truth variants
```
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	truth
mock	68	.	AT	A	40	.	.	GT	1/1
mock	73	.	T	A	40	.	.	GT	1/1
```
## Query variants
```
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	query
mock	69	.	TATAT	AAA	40	.	.	GT	1/1
```
## Output summary
Variant Type | Metric | Hap.py-GT | Aardvark-GT | Aardvark-Basepair
:-- | :-- | --: | --: | --:
ALL | F1 | -- | NaN | 0.8
ALL | Recall | -- | 0.0 (0/2) | 1.0 (8/8)
ALL | Precision | -- | 0.0 (0/1) | 0.6666666666666666 (8/12)
SNV | F1 |  |  | 
SNV | Recall | 0.0 (0/1) | 0.0 (0/1) | 1.0 (4/4)
SNV | Precision | 0.0 (0/2) |  (0/0) |  (0/0)
INDEL | F1 |  | NaN | 0.8
INDEL | Recall | 0.0 (0/1) | 0.0 (0/1) | 1.0 (4/4)
INDEL | Precision | 0.0 (0/1) | 0.0 (0/1) | 0.6666666666666666 (8/12)
## MSA visualization
![](./msa_viz/msa.png)
