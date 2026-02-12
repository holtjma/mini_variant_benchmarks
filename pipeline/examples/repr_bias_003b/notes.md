## Notes
This example was generated in conjunction with [repr_bias_003a](../repr_bias_003a) to demonstrate how variant representation can bias GT scoring.
In this example, the query variants are represented as two distinct indels.
While this representation is less succinct, variant callers that are short tandem repeat (STR) aware may be more likely to report this change as a contraction and expansion of the two STRs.
This representation generates a sequence that is still identical to the sequence from the single SNV.

When scored, both Hap.py and aardvark-GT label the truth variant as a TP SNV, and the two query variants as TP indels.
This creates a weighting bias in the results: the form in `repr_bias_003a` assigned the **1 query TP** to **SNV**, whereas this form assigned **2 query TP** to **indels**.
Despite representing the same genomic changes, these two representations are scored differently.

In contrast, the ALL basepair scoring is identical to the results of repr_bias_002a because the variants represent the same genomic changes.

This example was generated manually based on a real event in a tandem repeat within the human genome: `chr1:192,369,881-192,369,920`.
