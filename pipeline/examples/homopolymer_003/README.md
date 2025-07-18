# Example `homopolymer_003`
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
mock	55	.	A	ACCC	40	.	.	GT	1/1
```
## Query variants
```
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	query
mock	55	.	A	ACC,ACCCC	40	.	.	GT	1|2
```
## Output summary
Variant Type | Metric | Hap.py-GT | Aardvark-GT | Aardvark-Basepair
:-- | :-- | --: | --: | --:
ALL | F1 | -- | NaN | 0.8333333333333334
ALL | Recall | -- | 0.0 (0/1) | 0.8333333333333334 (10/12)
ALL | Precision | -- | 0.0 (0/2) | 0.8333333333333334 (10/12)
SNV | F1 | -- | -- | --
SNV | Recall | -- | -- | --
SNV | Precision | -- | -- | --
INDEL | F1 |  | NaN | 0.8333333333333334
INDEL | Recall | 0.0 (0/1) | 0.0 (0/1) | 0.8333333333333334 (10/12)
INDEL | Precision | 0.0 (0/1) | 0.0 (0/2) | 0.8333333333333334 (10/12)
## MSA visualization
![](./msa_viz/msa.png)
