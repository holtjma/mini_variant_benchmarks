## Notes
This captures a real example that is found in `chr1:1743494-1743636` in T2TQ100-V1.1.
The query variants are pulled from a HiFi sequencing run for HG002.

This particle example includes many confounding factors that make it difficult to match the variants up correctly.
First, the truth set contains multi-allelic variants and haploid genotypes, the latter of which does not seem to be supported by Hap.py.
Additionally, the truth set representations tend to squish multiple changes together into a single variant, while the query set representation is more discretized.
All of these complication result in Hap.py only identifying one TP call in the entire collection.
In constrast, Aardvark's sequence-centric view allows it to find most of the variants in both the truth and query sets despite the confounding factors, leading to much higher precision and recall.
