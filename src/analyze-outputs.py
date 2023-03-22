import sys

if __name__ == "__main__":
    error_filepath = sys.argv[1]
    time_filepath = sys.argv[2]

    with open(error_filepath) as error_file:
        errors = error_file.readlines()
    
    assert len(errors) == 0, "errors present, read error file \"{}\" for more information".format(error_filepath)

    with open (time_filepath) as time_file:
        times = time_file.readlines()
    
    times = [int(time.strip()) for time in times]

    times.sort()
    mid = len(times) // 2
    median = (times[mid] + times[~mid]) / 2
    print("median: " + "%.3f" % (median / 1000) + "s")
