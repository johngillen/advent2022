#!/bin/bash

while true; do
    if echo $(TZ='ETC' date +'%d') | grep -q $1; then
        $2
        exit 0
    fi
    sleep 1
done
