#!/usr/bin/env python3

#Aurther: Bikesh Shrestha
#Auther ID: bshrestha24
#Date created: 2024/05/22

import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
