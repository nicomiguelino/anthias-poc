#!/bin/bash

set -euo pipefail

services=(
    base
    publisher
    narnia
    subscriber
)
boards=(
    pi4
)

TARGET_PLATFORM="linux/arm/v7"
PI_VERSION=""

BUILD_CONTEXT="$(readlink -f .)"

for board in ${boards[@]}; do
    for container in ${services[@]}; do
        path=$(readlink -f "Dockerfile.${container}")

        if [[ ! -f "${path}" ]]; then
            continue
        fi

        echo "Building container ${container} for ${board}..."

        docker buildx build \
            --platform "${TARGET_PLATFORM}" \
            --output "type=image" \
            --build-arg "BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ')" \
            -f "${path}" \
            -t "nicomiguelino/ci-ex-${container}:latest" .
    done

    echo ""
done
