# Example `half_correct_rev`
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
mock	52	.	A	AC	40	.	.	GT	0/1
```
## Query variants
```
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	query
mock	52	.	A	C	40	.	.	GT	0/1
```
## Output summary
Variant Type | Metric | Hap.py-GT | Aardvark-GT | Aardvark-Basepair
:-- | :-- | --: | --: | --:
ALL | F1 | -- | NaN | 0.5
ALL | Recall | -- | 0.0 (0/1) | 0.5 (1/2)
ALL | Precision | -- | 0.0 (0/1) | 0.5 (1/2)
SNV | F1 |  |  | 
SNV | Recall | 0.0 (0/0) |  (0/0) |  (0/0)
SNV | Precision | 0.0 (0/1) | 0.0 (0/1) | 0.5 (1/2)
INDEL | F1 |  |  | 
INDEL | Recall | 0.0 (0/1) | 0.0 (0/1) | 0.5 (1/2)
INDEL | Precision | 0.0 (0/0) |  (0/0) |  (0/0)
## MSA visualization
![](./msa_viz/msa.png)
