## Notes
This captures a real example that is found in `chr1:6401103-6401205` in GIAB v4.2.1.
The query variants are pulled from a HiFi sequencing run for HG001.
In this example, the HiFi variant calling is partially correct.
It correctly identifies the SNP (which is represented as 52:CA>AA), but deletes the wrong base (51:AC>A instead of 52:CA>C).
Aardvark assigns partial credit to the allele that is observed, whereas Hap.py marks the entire call as incorrect.
