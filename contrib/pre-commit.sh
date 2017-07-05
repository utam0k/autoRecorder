#!/usr/bin/env bash

files=$(git diff --cached --name-status | grep -v ^D | awk '$1 $2 { print $2}' | grep -e .py$)
array=(${files/// })

for file in "${array[@]}"
do
    if [[ ${file} =~ "autoRecorder/test/" ]]; then
        flake8 --max-line-length=160 ${file}
    else
        flake8 ${file}
    fi
done
