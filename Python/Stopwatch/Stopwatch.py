# 🛠️ Project: Super Stopwatch
#! python3
# Stopwatch.py - A simple stopwatch program.

import time

print(
    'Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.'
)
input()  # Wait for user to start
startTime = time.time()  # Store the overall start time
print("Started.")
lastTime = startTime  # For tracking laps
lapNum = 1
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print("Lap #%s: %s (%s)" % (lapNum, totalTime, lapTime), end="")
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print("\nDone.")