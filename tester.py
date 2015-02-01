#!/usr/bin/env python3

import os
import time

startTime = time.time()
print("Running tests...")
os.system("./RunCollatz.py < RunCollatz.in.txt > result.txt")
print("Took " +  str(time.time() - startTime) + " seconds")

print("Checking validity...")
os.system("diff result.txt RunCollatz.out.txt")
