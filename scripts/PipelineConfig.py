
import os

# constants that set up root for a lot of things
PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))

#anything derived from the root config
RULES_FOLDER = f'{PROJECT_DIR}/rules'
ENV_FOLDER = f'{PROJECT_DIR}/conda_envs'
PIPELINE_FOLDER = f'{PROJECT_DIR}/pipeline'
SCRIPTS_FOLDER = f'{PROJECT_DIR}/scripts'
SNAKEFILE = f'{RULES_FOLDER}/BenchmarkPipeline.smk'

# version we're testing with
MAIN_VERSION = 'v0.7.4-static'
AARDVARK_BINARY = f'{PROJECT_DIR}/bin/aardvark-{MAIN_VERSION}'
