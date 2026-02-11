## Notes
This example was generated in conjunction with [repr_bias_002a](../repr_bias_001a) to demonstrate how variant representation can bias GT scoring.
In this example, the query variants are represented as a single complex indel.
When scored, both Hap.py and aardvark-GT label that event as a FP, and all truth variants as FN.

In contrast, the basepair scoring is identical to the results of repr_bias_002a because the variants represent the same genomic changes.