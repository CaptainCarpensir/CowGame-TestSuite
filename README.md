# CowGame-TestSuite

A test suite for the cow game created by Dr. Morales that students can use to compare algorithm run-times

### Notes

Some considerations of what I want this to do:
1. A better test generator - we need it to generate valid tests. Also, I'd like to be able to test different grid sizes. I think preferably tests should be generated randomly as they're run instead of tests being pre-generated and then tested globally. I don't know if the variance between how hard a test is to solve would ruin the accuracy of data though. Maybe we could do some amount of data analytics and just throw out outliers.
2. Should the time analysis just be the runtime of the search algorithm, or should it include the time taken by input/output? If the test cases are sufficiently large, this shouldn't be too much of an issue because I/O will be a small enough factor in the time. However if our test cases are running really quickly (which we might want them to do so we can make thousands of tests) this could make it impossible to genuinely differentiate the faster algorithms.
3. Should this repo contain everyones code so we can have an automatic tester output ranks?