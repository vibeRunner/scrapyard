import time as t
import subprocess as s

target = {"hour":input("hour: "), "minutes":input("minutes: ")}
print("Alarm set.")
while True:
    time = t.localtime()
    if time.tm_hour == target["hour"]:
        if time.tm_min == target["minutes"]:
            print("\nWAKE UP")
            s.call(["say", "-v", "Alex", "Wake up, you lazy potato! This is army, not some kindergarden! Do something with your life! You've got lots of work to do!"])
            break
    t.sleep(1)

input()
