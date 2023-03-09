from utils import Board, Player
from tkinter import *
from tkinter import messagebox


# def clicked():
# 	btn.configure(text="Отлично, сохранено")
#
#
# window = Tk()
# window.title('Добро пожаловать в игру крестики-нолики')
# window.geometry('700x450')
#
#
# user_1 = Label(window, text="Введите имя первого игрока: ", font=("Verdana", 10))
# user_1.grid(column=0, row=1)
# user_2 = Label(window, text="Введите имя второго игрока: ", font=("Verdana", 10))
# user_2.grid(column=0, row=2)
# input_1 = Entry(window, width=20)
# input_1.grid(column=1, row=1)
# input_2 = Entry(window, width=20)
# input_2.grid(column=1, row=2)
# btn = Button(window, text="Сохранить", command=clicked)
# btn.grid(column=1, row=3)
#
# u_1 = Player(input_1.get())
# u_2 = Player(input_2.get())
#
#
# board = Board()
# board_window = Label(window, text='ghbdtn')
# board_window.grid(column=0, row=4)
#
#
# window.mainloop()

board = Board()
board.print_board()
user_1 = Player(input("Введите имя первого игрока: "))
user_2 = Player(input("Введите имя второго игрока: "))

start_play = input("Хотите сыграть в крестики/нолики? (да/нет) ").lower()
if start_play == 'да':
	while True:
		action_1 = input(f"{user_1.name} выберите номер клетки: ")
		if action_1 in board.board:
			for index, num in enumerate(board.board):
				if num == action_1:
					user_1.action.append(num)
					board.board.remove(num)
					board.board.insert(index, "x")
		elif action_1 not in board.board:
			print("Данная клетка занята, выберите другую")
		if len(user_1.action) == 3 and sorted(user_1.action) in Board.winning_combinations:
			print('\nПобедитель {}'.format(user_1.name))
			board.print_board()
			break
		if len(user_1.action) == 3 and sorted(user_1.action) not in Board.winning_combinations:
			user_1.action = []
		if not any(sym.isdigit() for sym in board.board):
			print("Победила дружба")
			break
		print()
		board.print_board()
		action_2 = input(f"{user_2.name} выберите номер клетки? ")
		if action_2 in board.board:
			for index, num in enumerate(board.board):
				if num == action_2:
					user_2.action.append(num)
					board.board.remove(num)
					board.board.insert(index, "o")
		elif action_2 not in board.board:
			print("Данная клетка занята, выберите другую")
		if len(user_2.action) == 3 and sorted(user_2.action) in Board.winning_combinations:
			print('\nПобедитель {}'.format(user_2.name))
			board.print_board()
			break
		if len(user_2.action) == 3 and sorted(user_2.action) not in Board.winning_combinations:
			user_2.action = []
		if not any(sym.isdigit() for sym in board.board):
			print("Победила дружба")
			break
		print()
		board.print_board()
else:
	print("Ну в другой раз!")
