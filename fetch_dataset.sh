#!/bin/bash

if [ -d "data" ]; then
  echo "Dataset already cloned"
else
  git clone https://huggingface.co/datasets/ai4bharat/Aksharantar data
fi

cd data

for zipFile in *.zip; do
  if [ -f "$zipFile" ]; then
    folderName="${zipFile%.*}"
    mkdir -p "$folderName"
    unzip "$zipFile" -d "$folderName"
    rm "$zipFile"
  fi
done

