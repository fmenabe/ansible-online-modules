#!/bin/bash

set -ex

ROLE_PATH=$(realpath $(dirname $(realpath $0))/..)
DOC_PATH=$ROLE_PATH/doc

# Build variables
BUILD_PATH="$DOC_PATH/build"
ANSIBLE_VERSION=v2.9.12
ANSIBLE_BUILD_PATH="$BUILD_PATH/ansible"
TEMPLATES_BUILD_PATH="$ANSIBLE_BUILD_PATH/docs/templates"
MODULE_UTILS_BUILD_PATH="$BUILD_PATH/module_utils"
MODULES_BUILD_PATH="$BUILD_PATH/modules"
MODULES_COLLECTION="cloud/online"
OUTPUT_BUILD_PATH="$BUILD_PATH/rst"

# Modules' elements paths
TEMPLATES_PATH="$DOC_PATH/templates"
MODULE_UTILS_PATH="$ROLE_PATH/module_utils"
MODULES_PATH="$ROLE_PATH/library"
DOC_FRAGMENTS_PATH="$ROLE_PATH/doc_fragments"

USAGE="Usage: ./gen_doc.sh clone|build|copy"


prepare() {
    mkdir -p $BUILD_PATH
}

clone() {
    rm -rf $ANSIBLE_BUILD_PATH
    # --depth 1 retrieve only the last commit message so it is quicker
    git clone --depth 1 --branch $ANSIBLE_VERSION https://github.com/ansible/ansible $ANSIBLE_BUILD_PATH

    # Clean files of the existing modules
    rm $ANSIBLE_BUILD_PATH/lib/ansible/module_utils/online.py
    rm -rf $ANSIBLE_BUILD_PATH/lib/ansible/modules/cloud/online/
    rm $ANSIBLE_BUILD_PATH/lib/ansible/plugins/doc_fragments/online.py
}

build() {
    # Replace Ansible templates by ours
    cp $TEMPLATES_PATH/* $TEMPLATES_BUILD_PATH/

    # Prepare our module_utils and modules
    cp -r $MODULE_UTILS_PATH $MODULE_UTILS_BUILD_PATH
    mkdir -p $MODULES_BUILD_PATH/$MODULES_COLLECTION
    cp $MODULES_PATH/* $MODULES_BUILD_PATH/$MODULES_COLLECTION

    # Build documentation
    export ANSIBLE_DOC_FRAGMENT_PLUGINS=$DOC_FRAGMENTS_PATH
    $ANSIBLE_BUILD_PATH/hacking/build-ansible.py \
        document-plugins \
        --module-dir $MODULES_BUILD_PATH \
        --template-dir $TEMPLATES_BUILD_PATH \
        --plugin-type module \
        -t rst \
        -o $OUTPUT_BUILD_PATH

    # Copy generated documentation
    for module in dns key os_info server_info server; do
        cp $OUTPUT_BUILD_PATH/online_"$module"_module.rst $DOC_PATH
    done
}

# Main
if [ $# -ne 1 ]; then
    echo $USAGE
    echo "invalid number of arguments"
    exit 1
fi

prepare

if [ $1 = "clone" ]; then
    clone
elif [ $1 = "build" ]; then
    build
else
    echo $USAGE
    echo "invalid command: $1"
fi
