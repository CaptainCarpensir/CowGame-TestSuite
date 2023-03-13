#!/bin/bash
for i in {0..499}
do
    ./your-code-goes-here/can-o-worms/target/release/can-o-worms "src/tests/input/7x7test$i.txt" "src/tests/output/7x7test$i-sol.txt" 1
done