import math
import re

def is_single(vect):
	try:
		int(vect)
	except:
		return False
	else:
		return True
def getSign(vector):
	vect = vector.split(" ")
	if len(vect) == 1:
		return (None, None)
	elif len(vect) == 2
		return (vect[1], None)
	else:
		return (vect[1], vect[3])

def first_second_sign(vector_list, first_sign, second_sign):
	li = list()
	for item in vector_list:
		#print(f"the item number is {item[0]}, the length of the item is {len(item)}")
		if is_single(item):
			if counter == 1:
				li.append(int(first_sign + item))
			elif counter == 2:
				li.append(int(second_sign + item))
		else:
			if len(item) == 1:
				if counter == 1:
					li.append(int(first_sign + "1"))
				elif counter == 2:
					li.append(int(second_sign + "1"))
				else:
					li.append(item[:-1])
			else:
				if counter == 1:
					li.append(int(first_sign + item[:-1]))
				elif counter == 2:
					li.append(int(second_sign + item[:-1]))
				else:
					li.append(int(item[:-1]))
		counter += 1
		#else:
			#if len(item) != 1: 
				#li.append(int(item[0]))
	return li

def get_first_sign(vector_list, first_sign):
	li = list()
	for item in vector_list:
		#print(f"the item number is {item[0]}, the length of the item is {len(item)}")
		if is_single(item):
			if counter == 1:
				li.append(int(first_sign + item))
		else:
			if len(item) == 1:
				if counter == 1:
					li.append(int(first_sign + "1"))
				else:
					li.append(item[:-1])
			else:
				if counter == 1:
					li.append(int(first_sign + item[:-1]))
				else:
					li.append(int(item[:-1]))
		counter += 1
		#else:
			#if len(item) != 1: 
				#li.append(int(item[0]))
	return li

def getList(vector_list, first_sign, second_sign):
	result = None
	counter = 0
	if first_sign is not None and second_sign is not None:
		result = first_second_sign(vector_list, first_sign, second_sign)
	elif first_sign is not None:
		result = get_first_sign(vector, first_sign)
	elif second_sign is not None:
		result = get_second_sign(vector, second_sign)
	else:
		result = get_no_sign(vector)
	return result

def getNum(li, vect):
	try:
		num = li[vect]
		return num
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

def addVectors(firs, seco):
	res_list = list()
	for i in range(3):
		if i == 0:
			#vect = str(firs[i] + seco[i]) + "i"
			#print(f"The number is {num} and the type is {type(num)}")
			vect = str(getNum(firs, i) + getNum(seco, i)) + "i"
			
		elif i == 1:
			#vect = str(firs[i] + seco[i]) + "j"
			vect = str(getNum(firs, i) + getNum(seco, i)) + "j"
		elif i == 2:
			#vect = str(firs[i] + seco[i]) + "k"
			vect = str(getNum(firs, i) + getNum(seco, i)) + "k"
		res_list.append(vect)
	return res_list

def getPM(vector):
	vect_list = vector.split("+")
	lit = list()
	for v in vect_list:
		if "-" in v:
			#r = v.split("-")
			lit.extend(v.split("-"))
			#li.append(r[0])
			#li.append(r[1])
		else:
			lit.append(v)
	return lit
		

def getVector(vector):
	vect = vector.strip()
	num_plus = vector.count("+")
	vect = vect.replace(" ", "")
	if num_plus == 2:
		res = vect.split("+")
	elif num_plus == 1:
		res = getPM(vect)
	else:
		res = vect.split("-")
	return res

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

def main():
	first = "2i - 3j"
	second = "5i +j + 2k"

	first = sanitize_input(first)
	second = sanitize_input(second)
	print("################## ADDITION OF TWO VECTORS ####################### \n\n")
	#first = input("Enter the first vector => ")
	#second = input("Enter the second vector => ")
	first_list = getVector(first)
	second_list = getVector(second)
	(first_sign1, second_sign1) = getSign(first)
	(first_sign2, second_sign2) = getSign(second)
	print(f"{first_sign1} and {second_sign1}")
	fir_li = getList(first_list, first_sign1, second_sign1)
	sec_li = getList(second_list, first_sign2, second_sign2)
	#print(fir_li)
	result = addVectors(fir_li, sec_li)
	print(result)
	print(convert_string(result))

if __name__ == "__main__":
	main()

