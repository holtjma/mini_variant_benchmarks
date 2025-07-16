## Notes
### Auto-generated metadata
* Sample type: HG002
* Benchmark: T2TQ100-V1.1
* Sample: HG002_revio
* Coordinates: chr1:7284066-7284246

### Manual notes
This example shows a region where Hap.py has grouped relatively distant variants into a single region, whereas Aardvark has them split into two with default parameters.
Of course, this leads to different results since the two tools are considering different sets of variants.
Increasing the window parameter of Aardvark (`--min-variant-gap 60`) will merge the two regions into one, changing the overall GT metrics to recall=1.0, precision=0.5, and f1=0.6666.
