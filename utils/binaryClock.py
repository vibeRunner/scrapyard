# by m81v4n
# Simple clock displaying binary values on LED's
# connected together with cables and resistors
# can provide photos of the circuit, just hmu

import RPi.GPIO as GPIO
import time as t

# TODO! MAKE IT CHANGE MINUTES WHEN MINUTES CHANGE IRL
# TODO! simplify code, get rid of repetition

# UWAGA! nie numeracja procesorowa, tylko po kolei! patrz sciaga
# just resets all diodes each minute

hourPins = [37, 40, 38, 36, 32]
minutePins = [22, 18, 12, 16, 33, 35]

GPIO.setmode(GPIO.BOARD)

for pin in hourPins + minutePins:
	GPIO.setup(pin, GPIO.OUT)


try:
	while True:

		time = t.localtime()

		binaryHour = bin(time.tm_hour + 1)[2:] # that +1 cuz module doesn't work that well
		if len(binaryHour) != 5:
			binaryHour = '0' * (5 - len(binaryHour)) + binaryHour

		binaryMinutes = bin(time.tm_min)[2:]
		if len(binaryMinutes) != 6:
			binaryMinutes = '0' * (6 - len(binaryMinutes)) + binaryMinutes

		index = 0
		for state in binaryHour:
			GPIO.output(hourPins[index], int(state))
			index += 1

		index = 0
		for state in binaryMinutes:
			GPIO.output(minutePins[index], int(state))
			index += 1

		t.sleep(60)

except KeyboardInterrupt:

	for pin in hourPins + minutePins:
		GPIO.output(pin, 0)

	GPIO.cleanup()
	exit()
