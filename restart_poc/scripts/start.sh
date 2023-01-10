#!/bin/bash

counter=0

while [[ "$counter" -lt 10 ]]; do
    echo "counter: $counter"
    ((counter++))
    sleep 1
done

# TODO: Uncomment the line below when ready.
# bash /usr/bin/balena-idle --silent

# TODO: Comment the line below after debug.
exit 1
