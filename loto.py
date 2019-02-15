import random


class Card:
	def __init__(self, name):
		bag = [i for i in range(1, 91)]
		self.card = [__class__.tab_cell(bag), __class__.tab_cell(bag), __class__.tab_cell(bag)]
		self.name = name
		self.barrels = 15

	def tab_cell(bag):
		cell = ['' for _ in range(9)]
		for x in range(8, 3, -1):
			numbr = random.randint(0, x)
			while cell[numbr] != '':
				numbr += 1
			cell[numbr] = bag.pop(random.randint(0, len(bag) - 1))
		return cell

	def __str__(self):
		table = '{:^18}\n'.format(self.name)
		for x in range(3):
			table += '{} {} {} {} {} {} {} {} {}'.format(*self.card[x]) + '\n'
		return table


player = Card(' Игрок ')
computer = Card(' Компьютер ')

bag = [x for x in range(1, 91)]
while True:
	if len(bag) < 1:
		print('Результат:\n'
		      'у компьютера осталось {} полей,\n'
		      'у игрока осталось {} полей.'.format(
		          computer.barrels, player.barrels))
		break
	barrel = bag.pop(random.randint(0, len(bag) - 1))
	print('Текущий бочонок: {}, осталось {}'.format(barrel, len(bag)))
	print(computer)
	print(player)
	answer = input('Зачеркнуть цифру? (q для выхода) (y/n/q)')
	while answer not in 'ynq':
		print('Новый бочонок: {} (осталось {})'.format(barrel, len(bag)))
		print(computer)
		print(player)
		answer = input('Зачеркнуть цифру? (q для выхода) (y/n/q)')

	if answer == 'q':
		break
	elif answer == 'y':
		test = False
		for i in range(3):
			if barrel in player.card[i]:
				test = True
				player.card[i][player.card[i].index(barrel)] = 'X'
				player.barrels -= 1
			if barrel in computer.card[i]:
				computer.card[i][computer.card[i].index(barrel)] = 'X'
				computer.barrels -= 1
		if test:
			if player.barrels < 1:
				print('Победа за Вами!')
				break
			elif computer.barrels < 1:
				print('Победил компьютер!')
				break
		else:
			print('Вы проиграли!')
			break
	elif answer == 'n':
		test = False
		for i in range(3):
			if barrel in player.card[i]:
				print('Вы проиграли!')
				test = True
				break
			if barrel in computer.card[i]:
				computer.card[i][computer.card[i].index(barrel)] = 'X'
				computer.barrels -= 1
		if test:
			break
		if player.barrels < 1:
			print('Победа за Вами!')
			break
		elif computer.barrels < 1:
			print('Победил компьютер!')
			break

