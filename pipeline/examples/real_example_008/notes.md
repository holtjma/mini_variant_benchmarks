## Notes
### Auto-generated metadata
* Sample type: HG002
* Benchmark: T2TQ100-V1.1
* Sample: HG002_revio
* Coordinates: chr1:6742048-6742172

### Manual notes
This an example where Hap.py annotates several of the variants as "halfcall", and then marks them as errors.
This has a cascading effect, such that only one truth variant is identified as a TP by Hap.py.
In constrast, Aardvark matches up each variant for an F1=1.0 for both GT and BASEPAIR.
