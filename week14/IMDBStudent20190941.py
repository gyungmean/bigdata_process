#!/usr/bin/python3

import sys

input_file = sys.argv[1]
output_file = sys.argv[2] 

result = {}

f = open(input_file, 'r')
while True:
	line = f.readline()
	if not line: break
	movie = line.split('::')
	genre_list = movie[2].split('|')

	for genre in genre_list:
		genre = genre.strip()
		if result.get(genre) != None :
			continue
		result[genre] = 0

	for genre in genre_list:
		genre = genre.strip()
		if result[genre] == 0:
			result[genre] = 1
		else:
			count = result[genre] + 1
			result[genre] = count


#print(result)
f.close()

f = open(output_file, 'w')
for key, value in result.items():
	f.write(key + " " +  str(value) + "\n")

f.close()
