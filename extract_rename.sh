#!/bin/bash

for file in 2020_tweets/*.json.bz2; do
    echo "Extracting $file"
    bzip2 -d $file
done

i=0
for file in 2020_tweets/*.json; do
    echo "Renaming $file to $i.json"
    mv $file 2020_tweets/$i.json
    i=$((i+1))
done

rm 2020_tweets/*.json.bz2