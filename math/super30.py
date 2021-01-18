import random as r
maximum = 30
operations = 3

# by viberunner

def check_if_valid(maximum, chain, new):
	test = new
	test += sum(chain)

	if test > maximum or test < 0: # comment "or test < 0" to allow negative results
		return False

	else:
		return True


def generate_task(maximum, operations):

	out = []
	for i in range(operations):

		while True:

			number = r.randint(0 - maximum, maximum)

			if check_if_valid(maximum, out, number) and number != 0:
				out.append(number)
				break

			else:
				pass

	return out


def printable_tasks(chain):
	
	out = ""
	for task in chain:

		if task > 0:
			out += f"+{task} "

		else:
			out += f"{task} "

	return f"{out}= "


def main():

	print('\nsuper30.py by viberunner\n\nTYPE "EXIT" TO QUIT.\n\n')
	
	while True:

		current_task = generate_task(maximum, operations)

		while True:

			answer = input(printable_tasks(current_task))

			if "e" in answer.lower():
				exit('\nThanks for playing!\n')

			else:

				try:
					if int(answer) == sum(current_task):
						print('CORRECT.\n')
						break
					else:
						print('TRY AGAIN...')

				except:
					print('INPUT ERROR, MAKE SURE THAT THERE ARE ONLY NUMBERS IN YOUR ANSWER')


if __name__ == "__main__":
    main()
