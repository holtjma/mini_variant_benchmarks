# Example `representation_mismatch_001`
## Reference sequences
```
>mock
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
```
## Truth variants
```
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	truth
mock	52	.	A	C	40	.	.	GT	0|1
mock	53	.	A	G	40	.	.	GT	0|1
```
## Query variants
```
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	query
mock	52	.	AA	CAG	40	.	.	GT	0|1
```
## Output summary
Variant Type | Metric | Hap.py-GT | Aardvark-GT | Aardvark-Basepair
:-- | :-- | --: | --: | --:
ALL | F1 | -- | NaN | 0.75
ALL | Recall | -- | 0.0 (0/2) | 0.75 (3/4)
ALL | Precision | -- | 0.0 (0/1) | 0.75 (3/4)
SNV | F1 | 0.666667 |  | 
SNV | Recall | 0.5 (1/2) | 0.0 (0/2) | 0.75 (3/4)
SNV | Precision | 1.0 (1/1) |  (0/0) |  (0/0)
INDEL | F1 |  |  | 
INDEL | Recall | 0.0 (0/0) |  (0/0) |  (0/0)
INDEL | Precision | 0.0 (0/1) | 0.0 (0/1) | 0.75 (3/4)
## MSA visualization
![](./msa_viz/msa.png)
