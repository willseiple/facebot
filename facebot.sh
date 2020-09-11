#!/bin/sh

fileId=16S6IvJlvc8JOq-qh3-BDYIC67VjAQEJH
fileName=data.zip

if [ ! -d 'reader/data' ]
then
    printf 'Fetching files from Google Drive\n'
    curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${fileId}" > /dev/null
    code="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"
    printf 'Downloading...\n'
    curl -sLb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${code}&id=${fileId}" -o ${fileName}
    printf 'Unzipping files...\n'
    unzip data.zip -d reader
    rm data.zip
    printf 'Installation complete\n'
fi

python3 cli.py
