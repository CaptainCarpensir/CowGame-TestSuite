import sys

"""
This analyzes the outputs to make sure there are no errors, and then gets the median of the times taken.

We should use a better statistic than median.

Currently median is used over mean because the mean would be heavily skewed by outliers. 
Due to the nature of this test, the minimum number of cows to be placed has the greatest impact on run-time, so tests will be inherently varied.
We need a way to take into account potential outliers in computation time, without skewing data by 
"""

if __name__ == "__main__":
    error_filepath = sys.argv[1]
    time_filepath = sys.argv[2]

    with open(error_filepath) as error_file:
        errors = error_file.readlines()
    
    assert len(errors) == 0, "errors present, read error file \"{}\" for more information".format(error_filepath)

    with open (time_filepath) as time_file:
        times = time_file.readlines()
    
    times = [int(time.strip()) for time in times]

    # TODO: create better statistical output for comparison than median
    times.sort()
    mid = len(times) // 2
    median = (times[mid] + times[~mid]) / 2
    print("median: " + "%.3f" % (median / 1000) + "s")
