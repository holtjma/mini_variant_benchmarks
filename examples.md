# Examples
All examples are hosted in the [pipeline/examples](./pipeline/examples/) folder, each with its own subdirectory.
This page contains additional details on the naming conventions and may assist in navigating to specific types of examples.

## Where to start?
The best starting example is [simple_snv_het](./pipeline/examples/simple_snv_het/), which contains a simple heterozygous SNV in both the truth and query sets.
The splash page includes some additional notes which may help the reader orient themselves to the outputs generated by the pipeline.

## Categories by content

* [simple_snv_het](./pipeline/examples/simple_snv_het/) - Relatively simple example with notes on the output layout
* [zygosity_error_001](./pipeline/examples/zygosity_error_001/) - A simple example where the truth and query zygosities are different, highlighting how errors are counted differently between Hap.py and Aardvark for this scenario.
* `homopolymer_XXX` - Example: [homopolymer_001](./pipeline/examples/homopolymer_001/). Artificial examples where homopolymers are nearly correct, highlighting the differences in scoring when using genotype-centric v. basepair-centric scoring.
* [half_correct](./pipeline/examples/half_correct/) - An artificial example demonstrating a ``half-correct" variant as detected by BASEPAIR scoring
* `representation_match_XXX` - Example: [representation_match_001](./pipeline/examples/representation_match_001/). Artifical examples where the representations in the truth are query are different, but can be resolved to exactly match.
* `representation_mismatch_XXX` - Example: [representation_mismatch_001](./pipeline/examples/representation_mismatch_001/). Artifical examples where the representations in the truth are query are different, and one or more mismatches (FP/FN) are present.
* `null_variants_XXX` - Example: [null_variants_001](./pipeline/examples/null_variants_001/). Artifical examples where null variants are present, creating churn in the output.
* `real_example_XXX` - Example: [real_example_001](./pipeline/examples/real_example_001/). Examples derived from real observed regions from our comparisons. The first six were manually miniaturized, but the remaining were constructed via script from complex regions. These examples are quite complex, difficult to analyze by hand, and often include some amount of variant churn. They also tend to have the greatest level of discordance between Hap.py and Aardvark, likely due to their complexity.
