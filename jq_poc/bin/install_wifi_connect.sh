#!/bin/bash

if [[ "$TARGET_PLATFORM" = "linux/arm/v6" ]]; then
    architecture='rpi'
elif [[ "$TARGET_PLATFORM" = "linux/arm/v7" ]]; then
    architecture='armv7hf'
fi

jq_filter=".assets[] | select (.name|test(\"linux-$architecture\")) | .browser_download_url"
archive_url=$(curl -sL $WC_DL_URL | jq -r "$jq_filter")
archive_file=$(basename $archive_url)

wget $archive_url && \
tar -xvz -C /usr/src/app -f $archive_file
