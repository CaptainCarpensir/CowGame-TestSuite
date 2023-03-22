#!/bin/bash

# Create output filestructure
mkdir src/output
mkdir src/tests/output
> src/output/times.txt
> src/output/errors.txt

for i in {0..499}
do
    # Take current time in milliseconds via date command
    ts=$(date +%s%N)
    # Run given executable
    $1 "src/tests/input/test"$i".txt" "src/tests/output/test"$i"-sol.txt"
    # Output time taken into file
    echo "$((($(date +%s%N) - $ts)/1000000))" >> src/output/times.txt
    # Verify solution correctness
    python3 src/verify-solution.py "src/tests/input/test"$i".txt" "src/tests/output/test"$i"-sol.txt" 2>> src/output/errors.txt
done

python3 src/analyze-outputs.py src/output/errors.txt src/output/times.txt