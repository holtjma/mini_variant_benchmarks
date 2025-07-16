## Notes
This example is a variant of [null_variants_001](../null_variants_001) that includes an additional SNP in the truth set.
The query has injected two indels that are upstream and downstream of the SNP.
When the SNP position is shifted, these indels cancel each other out.

Both Hap.py and Aardvark treat these indels as true positives when scoring GT, showing 1 positive SNP and 2 positive indels.
At the variant level, Aardvark labels them as positives when scoring Basepair.
However, when the entire sequence is considered in `ALL` mode, only the SNP change is counted as a positive.
This effectively masking any scoring benefits from the indels that cancel each other out at the sequence level.
