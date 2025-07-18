# Example `zygosity_error_001`
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
mock	55	.	A	C	40	.	.	GT	0|1
```
## Query variants
```
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	query
mock	55	.	A	C	40	.	.	GT	1/1
```
## Output summary
Variant Type | Metric | Hap.py-GT | Aardvark-GT | Aardvark-Basepair
:-- | :-- | --: | --: | --:
ALL | F1 | -- | 0.0 | 0.6666666666666666
ALL | Recall | -- | 1.0 (1/1) | 1.0 (2/2)
ALL | Precision | -- | 0.0 (0/1) | 0.5 (2/4)
SNV | F1 |  | 0.0 | 0.6666666666666666
SNV | Recall | 0.0 (0/1) | 1.0 (1/1) | 1.0 (2/2)
SNV | Precision | 0.0 (0/1) | 0.0 (0/1) | 0.5 (2/4)
INDEL | F1 | -- |  | 
INDEL | Recall | -- |  (0/0) |  (0/0)
INDEL | Precision | -- |  (0/0) |  (0/0)
## MSA visualization
![](./msa_viz/msa.png)
