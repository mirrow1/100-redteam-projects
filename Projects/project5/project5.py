#!/usr/bin/env python3

import sys

def shift_four(string):
	chars = "abcdefghijklmnopqrstuvwxyz"
	output = ""
	for c in string:
		output += chars[(chars.find(c)+4)%26]
	print(output)

print("Enter text to encode: ")

for line in sys.stdin:
	line = line.strip("\n")
	shift_four(line)
