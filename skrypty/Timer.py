#by M81V4N
import subprocess as s
import time as t
import sys

sTarget = input("TIME IN SECONDS TO SAY: ")
print("\nSeconds left: "+str(float(sTarget - t.clock()))),
while True:
	sys.stdout.flush()
	print("\rSeconds left: "+str(float(sTarget - t.clock()))),
	if t.clock() >= sTarget:
		print("\n\n============\n\nWAKE UP!\n\n============")
		s.call(["say", "-v", "Alex", "Wake up, you lazy potato! This is army, not some kindergarden! Do something with your life! You've got lots of work to do!"])
		break

input()
