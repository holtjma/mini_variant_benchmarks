# Example `representation_match_001`
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
mock	52	.	AA	CG	40	.	.	GT	0|1
```
## Output summary
Variant Type | Metric | Hap.py-GT | Aardvark-GT | Aardvark-Basepair
:-- | :-- | --: | --: | --:
ALL | F1 | -- | 1.0 | 1.0
ALL | Recall | -- | 1.0 (2/2) | 1.0 (4/4)
ALL | Precision | -- | 1.0 (1/1) | 1.0 (4/4)
SNV | F1 | 1.0 |  | 
SNV | Recall | 1.0 (2/2) | 1.0 (2/2) | 1.0 (4/4)
SNV | Precision | 1.0 (2/2) |  (0/0) |  (0/0)
INDEL | F1 | -- |  | 
INDEL | Recall | -- |  (0/0) |  (0/0)
INDEL | Precision | -- | 1.0 (1/1) | 1.0 (4/4)
## MSA visualization
![](./msa_viz/msa.png)
