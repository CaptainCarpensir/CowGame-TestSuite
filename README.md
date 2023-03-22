# CowGame-TestSuite

A test suite for the cow game created by Dr. Morales that students can use to compare algorithm run-times

## Using the test-suite:

1. SSH into a campus linux machine
2. Write your code for the cow game specified in Dr. Morale's assignment document
3. Compile your code into a binary
4. Clone this git repository
5. Execute the `run.sh` with with the argument pathed to your binary: `./run.sh /home/acarpenter102/Assignments/CS-5400/2023-SP-1-puzzle3-amctyg/target/release/puzzle3`
6. Compare your runtime!

---

## Notes

I have a couple small issues with this test-suite that you can help fix if you'd like:
1. The verification process is a little slow, and doesn't verify that a solution is done with minimum cow placements
2. The tests are generated poorly, and they could have more intelligent properties
3. Using the output statistic for the median is a good way to rank speed, but doesn't give the full picture of how fast your algorithm is