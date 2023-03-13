#!/bin/bash
for i in {0..499}
do
    python3 src/verify-solution.py src/tests/input/7x7test$i.txt "src/tests/output/7x7test$i-sol.txt"
done