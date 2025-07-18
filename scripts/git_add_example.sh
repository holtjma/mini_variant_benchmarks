
if [[ $# -eq 0 ]]; then
    echo 'ERROR: specify example folder to add:'
    git status
    exit 1
fi

git add ../pipeline/examples/$1/inputs
git add ../pipeline/examples/$1/preprocessing
git add ../pipeline/examples/$1/aardvark
git add ../pipeline/examples/$1/aardvark_debug
git add ../pipeline/examples/$1/happy
git add ../pipeline/examples/$1/README.md
git add ../pipeline/examples/$1/msa_viz
git add ../pipeline/examples/$1/notes.md

# will auto-remove anything that is gone now
git add -u ../pipeline/examples/$1