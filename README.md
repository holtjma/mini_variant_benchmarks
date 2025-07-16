# mini_variant_benchmarks
This repository contains several miniaturized variant benchmark examples comparing the outputs of [Hap.py](https://github.com/Illumina/hap.py) to [Aardvark](https://github.com/PacificBiosciences/aardvark).
The examples are a mixture of A) artificially generated variant sets to demonstrate a key difference between the tools and B) real examples that are usually more complicated.
This repo also contains the various scripts and snakemake processes required to reproduce the analysis.

## Repo layout
* `bin` - Binary files we distribute for reproducibility
* `conda_envs` - All conda environments required to re-run this pipeline
* `pipeline/examples` - Each example has a sub-folder within this folder with all the automatically generated outputs. The README in the sub-folder contains a summary of the comparisons and notes for each specific example.
* `rules` - Rules that snakemake uses to run the pipeline
* `scripts` - A collection of (mostly) Python3 scripts that are necessary for running the pipeline

## Running the pipeline yourself
All outputs for the pipeline are distributed as part of this repo.
However, if you wish to run it yourself, the following steps will guide you through setting up and running the pipeline:

1. Clone this repository to your local compute infrastructure:
```bash
git clone https://github.com/holtjma/mini_variant_pipeline.git
cd mini_variant_pipeline
```
2. Create and activate the provided conda environment:
```bash
create --name mini_variant_pipeline --file ./conda_envs/mini_variant_pipeline.yaml
# follow prompts to install the environment
conda activate mini_variant_pipeline
```
3. Set up the run conditions for snakemake. Set up a snakemake profile for your compute environment. Several templates are provided on [snakemake submission profile](https://snakemake.readthedocs.io/en/stable/executing/cli.html#profiles). This is provided via the `--profile {SNAKEMAKE_PROFILE}` option, and passed through to the snakemake invocation.
4. Run the full pipeline, which will execute several steps per example:
```
# dry-run of the pipeline
python3 ./scripts/RunCohortPipeline.py --profile {SNAKEMAKE_PROFILE} -A
# executes the commands
python3 ./scripts/RunCohortPipeline.py --profile {SNAKEMAKE_PROFILE} -Ax
```
