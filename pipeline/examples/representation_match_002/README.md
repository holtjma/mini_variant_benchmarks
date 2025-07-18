# Example `representation_match_002`
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
mock	52	.	AA	CGCT	40	.	.	GT	0|1
```
## Query variants
```
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	query
mock	52	.	A	C	40	.	.	GT	0|1
mock	53	.	A	GCT	40	.	.	GT	0|1
```
## Output summary
Variant Type | Metric | Hap.py-GT | Aardvark-GT | Aardvark-Basepair
:-- | :-- | --: | --: | --:
ALL | F1 | -- | 1.0 | 1.0
ALL | Recall | -- | 1.0 (1/1) | 1.0 (8/8)
ALL | Precision | -- | 1.0 (2/2) | 1.0 (8/8)
SNV | F1 | 0.0 |  | 
SNV | Recall | 0.0 (0/0) |  (0/0) |  (0/0)
SNV | Precision | 1.0 (2/2) | 1.0 (1/1) | 1.0 (2/2)
INDEL | F1 | 1.0 | 1.0 | 1.0
INDEL | Recall | 1.0 (1/1) | 1.0 (1/1) | 1.0 (8/8)
INDEL | Precision | 1.0 (1/1) | 1.0 (1/1) | 1.0 (6/6)
## MSA visualization
![](./msa_viz/msa.png)
