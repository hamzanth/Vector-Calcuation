import math
import re

def sanitize_input(vector):
	locs = re.findall("[+,-][1-9]*[i,j,k]", vector)
	if len(locs) == 0:
		return vector
	else:
		vect_dict = dict()
		for vect in locs:
			vect_dict[vect] = vect[0] + " " + vect[1:]
		result = vector
		for key, value in vect_dict.items():
			result = result.replace(key, value)
		return result

def sanitize(vector):
	splt = vector.split(" ")
	if len(splt) == 1:
		if "i" in vector:
			vect = vector + " + 0j + 0k" 
		elif "j" in vector:
			if "-" in vector:
				vect = "0i - " + vector[1:] + " + 0k"
			else:
				vect = "0i + " + vector + " + 0k"
		elif "k" in vector:
			if "-" in vector:
				vect = "0i + 0j - " + vector[1:]
			else:
				vect = "0i + 0j + " + vector
	elif len(splt) == 3:
		print("The 2 if condition")
		if "i" not in vector:
			if vector.split(" ")[0][0] == "-":
				vect = "0i - " + vector[1:]
			else:
				vect = "0i + " + vector
		elif "j" not in vector:
			vect = ""
			for index, ve in enumerate(vector.split(" ")):
				if index == 0:
					vect += ve + " +"   #"3i + 4k"
				elif index == 1:
					vect += "0j"
				else:
					vect += vector.split(" ")[1] + " " + vector.split(" ")[2]
				vect += " "
		elif "k" not in vector:
			vect = vector + "+ 0k"
	else:
		vect = vector
	return vect

def get_unit(vect, index):
	try:
		res = int(vect[index][:-1])
		return res
	except:
		return 0

def getsigned_unit(vect, index):
	try:
		res = int(vect[index-1] + vect[index][:-1])
		return res
	except:
		return 0

def convert_string(res):
	result = ""
	for index, vect in enumerate(res):
		if index == 0:
			result = result + str(vect)
		else:
			if "-" in vect:
				result = result + "-" + " " + str(vect)[1:]
			else:
				result = result + "+" + " " + str(vect)
				
		result = result + " "
	return result

vector1 = "4j"
vector2 = "3i - 6j + 3k" 
vector3 = "2i + j -8k" 
result = list()

vector1 = sanitize(sanitize_input(vector1))
vector2 = sanitize(sanitize_input(vector2))

for i in range(0, 5, 2):
	splt_vect1 = vector1.split(" ")
	splt_vect2 = vector2.split(" ")
	if i == 0:
		res = get_unit(splt_vect1, i) + get_unit(splt_vect2, i)
		res = str(res) + "i"
	elif i == 2:
		res = getsigned_unit(splt_vect1, i) + getsigned_unit(splt_vect2, i)
		res = str(res) + "j"
	else:
		res = getsigned_unit(splt_vect1, i) + getsigned_unit(splt_vect2, i)
		res = str(res) + "k"
	result.append(res)

print(convert_string(result))