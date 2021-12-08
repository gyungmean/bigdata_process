#!/usr/bin/python3

import sys
import calendar

def get_day(y, m, d):
	str = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']
	return str[calendar.weekday(y, m, d)]

input_file = sys.argv[1]
output_file = sys.argv[2]

f1 = open(input_file, 'r')
data = {}
while True:
	line = f1.readline()
	if not line: break
	info = line.split(',')
	info[3] = info[3].strip()

	if data.get(info[0]) != None:
		data[info[0]][info[1]] = [info[2], info[3]]
		continue
	

	data[info[0]] = {info[1] : [info[2], info[3]]}


#print(data)
f1.close()

result = {}
f2 = open(output_file, 'w')
for base_num, value in data.items():
	if result.get(base_num) == None:
		result[base_num] = {}

	for date, value2 in value.items():
		date2 = date.split('/')
		day = get_day(int(date2[2]), int(date2[0]), int(date2[1]))
		if result[base_num].get(day) != None:
			result[base_num][day][0] = int(result[base_num][day][0]) + int(value2[0]) 
			result[base_num][day][1] = int(result[base_num][day][1]) + int(value2[1])
		else:
			result[base_num][day] = [value2[0], value2[1]]
		

for base_num, value in result.items():
	for day, value2 in value.items():
		f2.write(base_num + "," + day + " " + str(value2[0]) + "," + str(value2[1]) + "\n")
	
f2.close()
