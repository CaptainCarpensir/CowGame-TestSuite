class CowGame:
	def __init__(self, input_filepath):
		with open(input_filepath, "r") as input_file:
			num_lines = int(input_file.readline().strip())
			self.grid = []

			for i in range(num_lines):
				grid_row = input_file.readline()
				self.grid.append(grid_row)

	def count_tiletype(self, type: str) -> int:
		count = 0
		for row in self.grid:
			for chr in row:
				if chr == type:
					count += 1
		return count

	def score_game(self) -> int:
		score = 0

		for m in range(len(self.grid)):
			for n in range(len(self.grid[m])):
				if self.grid[m][n] == "C":
					score += self.score_cow(m, n)

		return score

	def in_bounds(self, m, n) -> bool:
		if m < 0 or m >= len(self.grid) or n < 0 or n >= len(self.grid[m]):
			return False
		return True

	def check_adj(self, m: int, n: int, type: str, allow_diag: bool) -> bool:
		diag_bounds = [(-1,-1),(-1,1),(1,-1),(1,1)]
		adj_bounds = [(-1,0),(1,0),(0,-1),(0,1)]

		if allow_diag:
			for bound_tuple in diag_bounds:
				(off_m, off_n) = bound_tuple
				if self.in_bounds(m + off_m, n + off_n):
					if self.grid[m + off_m][n + off_n] == type:
						return True

		for bound_tuple in adj_bounds:
			(off_m, off_n) = bound_tuple
			if self.in_bounds(m + off_m, n + off_n):
				if self.grid[m + off_m][n + off_n] == type:
					return True

		return False

	def score_cow(self, m: int, n: int) -> int:
		score = 0

		adj_to_cow = self.check_adj(m, n, "C", True)
		adj_to_hay = self.check_adj(m, n, "@", False)
		adj_to_water = self.check_adj(m, n, "#", False)

		if adj_to_cow: score -= 3
		if adj_to_hay: score += 1
		if adj_to_hay and adj_to_water: score += 2

		return score

