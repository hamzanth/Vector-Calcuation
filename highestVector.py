import math
import re

def get_pm(vector):
	num = vector.split("+")
	#print(f"num is {num}") "4i-10j+14k" 
	res = list()
	for index, n in enumerate(num):
		if index == 0:
			if len(n.split("-")) == 1:
				res.append(n)
			elif len(n.split("-")) == 3:
				for ind, su in enumerate(n.split("-")[1:]):
					if ind == 0:
						res.append("-" + su)
					else:
						res.append(su)
			else:		
				spleft = n.split("-")
				if spleft[0] == "":
					res.append(n)
				else:
					for wh in spleft:
						res.append(wh)
		else:
			for it in n.split("-"): #"-4i - 6j + 2k" 
				res.append(it)
	return res

def get_single_list(vector_list):
	if vector_list[0] == "":
		vector_list = vector_list[1:]
		vector_list[0] = "-" + vector_list[0]
	result = list()
	#print(f"vector is {vector_list}")
	for vec in vector_list:
		result.append(int(vec[:-1]))
	return result

def get_vector1(vector1):
	str_vect = vector1.replace(" ", "")
	num_plus = str_vect.count("+")
	if num_plus == 2:
		sub_res = str_vect.split("+")
	elif num_plus == 1:
		sub_res = get_pm(str_vect)
	else:
		sub_res = str_vect.split("-")
	final_res = get_single_list(sub_res)
	return final_res

def get_vector2(vector):
	strp_vect = vector.replace(" ", "")
	res = list()
	vect_list = strp_vect.split(",")
	for vec in vect_list:
		res.append(int(vec))
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

def get_vector_sign(vector):
	vect = vector.split(" ")
	return (vect[1], vect[3])

def is_single(vect):
	try:
		int(vect)
	except:
		return False
	else:
		return True

def first_second_sign(vector_list, first_sign, second_sign):
	li = list()
	for counter, item in enumerate(vector_list):
		#print(f"the item number is {item[0]}, the length of the item is {len(item)}")
		if is_single(item):
			if counter == 1:
				li.append(int(first_sign + str(item)))
			elif counter == 2:
				li.append(int(second_sign + str(item)))
			else:
				li.append(int(item))
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
		#counter += 1
		#else:
			#if len(item) != 1: 
				#li.append(int(item[0]))
	return li

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

def get_user_input():
	qlist = list()
	while True:
		vect = input("Enter the vector ==> ")
		qlist.append(vect)
		prompt = input("any other vector ?. press y for yes or  n for no ==> ")
		if "y" in prompt or "Y" in prompt:
			continue
		else:
			break
	return qlist

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
		#print("The 2 if condition")
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


def san_all_vectors(vector_list):
	res = list()
	for vect in vector_list:
		res.append(sanitize_input(vect))
	return res

def get_strp_list(sanit_question):
	res = list()
	for item in sanit_question:
		res.append(get_vector1(item))
	return res
def get_final_list(vector_lists):
	result = list()
	for lis in vector_lists:
		vect_sum = sum(pow(num, 2) for num in lis)
		vect_sqrt = math.sqrt(vect_sum)
		result.append(vect_sqrt)	
	return result


def main():
	print(############ A PROGRAM TO CALCULATE THE HIGHEST VECTORS ################)
	question_list = get_user_input()
	sanit_question = [sanitize(sanitize_input(quest)) for quest in question_list]
	print(f"sanit_question is {sanit_question}")
	
	strp_list = get_strp_list(sanit_question)
	
	fresult = get_final_list(strp_list)
	highest_num = max(fresult)
	highest_index = fresult.index(highest_num)
	highest_vector = question_list[highest_index]

	print(f"question_list is {fresult}")
	print(f"Highest vector is {highest_vector}")

if __name__ == "__main__":
	main()