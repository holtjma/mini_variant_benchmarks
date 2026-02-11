## Notes
This example was generated in conjunction with [repr_bias_001b](../repr_bias_001b) to demonstrate how variant representation can bias GT scoring.
In this example, the query variants are represented as individual small variants (SNP/indel).
When scored, both Hap.py and aardvark-GT detect the SNP as a TP and the indel as a FP.
