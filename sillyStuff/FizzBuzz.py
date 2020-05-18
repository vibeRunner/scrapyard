# by m81v4n

# muliple of 3: Fizz
# multiple of 5: Buzz
# multiple of both: FizzBuzz

counter = 1

while True:

	out = ''
	if counter % 3 == 0:
		out += 'Fizz'
	if counter % 5 == 0:
		out += 'Buzz'

	if out != '':
		print(out)
	else:
		print(counter)

	counter += 1 # or just make a FOR i IN RANGE() loop i guess
