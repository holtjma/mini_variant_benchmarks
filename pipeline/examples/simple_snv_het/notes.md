## Notes
This is the simplest benchmark example one can expect: a single heterozygous SNV in a relatively isolated region.
On this page, we provide the core input information to understand each of these examples including:

* The reference genome sequence
* The truth VCF file entries
* The query VCF file entries
* A table showing the scoring outcomes from Hap.py, Aardvark-GT, and Aardvark-Basepair. This table is subdividing by variant type (SNV/indel), and "ALL" is also provided from Aardvark.

The scoring schemes for Hap.py and Aardvark-GT are analogous, and will often (though not always) be identical throughout these examples.
In contrast, the basepair scoring scheme is based on sequence-level differences between the reference genome, the truth haplotype sequenes, and the query haplotype sequences.
Additionally, the basepair scoring scheme has some interesting cases where partial credit for an individual base is possible (see [half_correct](../half_correct)).
Thus, all values are doubled for basepair to remove floating point calculations.
For example, there is only one affected base in this example, yet the Aardvark-Basepair recall is (2/2).

Given this simple example that is an exact match, we see that recall, precision, and F1 scores are all 1.0 across all assessments.
