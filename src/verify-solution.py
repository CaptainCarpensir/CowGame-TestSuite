from cowgame import CowGame
import sys

def normalized(tile: str) -> str:
    if tile == 'C':
        return '.'
    return tile

if __name__ == "__main__":
    MIN_COW_SCORE = 7

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    unsolved_game = CowGame(input_file)
    solved_game = CowGame(output_file)

    score = solved_game.score_game()

    for m in range(len(unsolved_game.grid)):
        for n in range(len(unsolved_game.grid[m])):
            orig_char = unsolved_game.grid[m][n]
            new_char = solved_game.grid[m][n]
            assert normalized(new_char) == orig_char, "{}: solution makes illegal changes to grid at pos ({},{}): {} -> {}".format(output_file, m, n, orig_char, new_char)

    assert score >= MIN_COW_SCORE, "{}: solution does not meet the minimum score: {} < {}".format(output_file, score, MIN_COW_SCORE)
