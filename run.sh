#!/bin/bash

> src/output/times.txt
for i in {0..499}
do
    (/usr/bin/time -f '\t%U user' $1 "src/tests/input/7x7test"$i".txt" "src/tests/output/7x7test"$i".txt") 2>> src/output/times.txt
done