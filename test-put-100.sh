#!/bin/bash
for obj in {0..99}; do
    t0=`date +%s.%N`
    curl -s -X PUT -d "..." http://127.0.0.1:9000/hello/$obj.bin
    t1=`date +%s.%N`
    printf "%d, %s\n" $obj `bc <<< "$t1 - $t0"`
done
printf "\n"
