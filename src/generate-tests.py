import random
import numpy as np

# Seeding random so that everyone gets the same tests
random.seed(0)

NUM_TESTS = 500
TEST_SIZES = [7]

"""
TODO: TEST GENERATION SHOULD BE DEPRECATED FOR A BETTER SOLUTION
1. Tests should be verified to be correct (not unlikely to be impossible as they are now)
2. Tests should be able to be given a number which specifies the minimum cows placed to normalize 
"""

def generate_test(filepath: str, grid_size: int):
    test_grid = np.full(shape=(grid_size, grid_size), fill_value='.')

    num_haybales = [0]*random.randint(grid_size+1, grid_size*2)
    num_ponds = [0]*random.randint(2, grid_size//2)

    for _i in num_haybales:
        m = random.randint(0, grid_size-1)
        n = random.randint(0, grid_size-1)

        if test_grid[m][n] == '.':
            test_grid[m][n] = '@'
        else:
            num_haybales.append(0)

    for _i in num_ponds:
        m = random.randint(0, grid_size-1)
        n = random.randint(0, grid_size-1)

        if test_grid[m][n] == '.':
            test_grid[m][n] = '#'
        else:
            num_ponds.append(0)

    with open(filepath, 'w') as test:
        test.write(str(grid_size) + '\n')
        for row in test_grid:
            for char in row:
                test.write(char)
            test.write('\n')

# Generate tests
for size in TEST_SIZES:
    for test_num in range(NUM_TESTS):
        test_name = "src/tests/input/test{}.txt".format(test_num)
        generate_test(test_name, size)