
if [[ $# -eq 0 ]]; then
    echo 'ERROR: specify example name to create'
    exit 1
fi

# get the project folder
PROJECT=$(dirname $(dirname $(realpath $BASH_SOURCE)))

TEMPLATE="${PROJECT}/pipeline/examples/empty"
NEW_EXAMPLE="${PROJECT}/pipeline/examples/$1"

if [ -d ${NEW_EXAMPLE} ]; then
    echo "ERROR: example already exists: ${NEW_EXAMPLE}"
    exit 1
fi

mkdir ${NEW_EXAMPLE}
cp -r ${TEMPLATE}/inputs ${NEW_EXAMPLE}/inputs
echo "New example created at: ${NEW_EXAMPLE}"
