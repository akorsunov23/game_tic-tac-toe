class Board:
	"""
	Класс, отрисовывающий доску для игры в крестики-нолики
	с указанием номеров клеток.
	"""
	board = [str(ceil) for ceil in range(9)]
	winning_combinations = (['0', '1', '2'], ['3', '4', '5'],
							['6', '7', '8'], ['0', '3', '6'],
							['1', '4', '7'], ['2', '5', '8'],
							['0', '4', '8'], ['2', '4', '6'])

	@staticmethod
	def print_board():
		print(Board.board[0], '|', Board.board[1], '|', Board.board[2])
		print('----------')
		print(Board.board[3], '|', Board.board[4], '|', Board.board[5])
		print('----------')
		print(Board.board[6], '|', Board.board[7], '|', Board.board[8])


class Player:

	def __init__(self, name):
		self.name = name
		self.action = []
