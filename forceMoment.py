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
def sub_vector(vect1, vect2):
	result = list()
	for i in range(3):
		result.append(vect1[i] - vect2[i])
	return result

def multiply_vector(vectnum2, vectnum1):
	first_calc = (vectnum2[1]  * vectnum1[2]) - (vectnum2[2] * vectnum1[1])
	second_calc = -1 * ((vectnum2[0] * vectnum1[2]) - (vectnum2[2] * vectnum1[0]))
	third_calc = (vectnum2[0] * vectnum1[1]) - (vectnum2[1] * vectnum1[0])
	final_answer_list = [first_calc, second_calc, third_calc]
	return final_answer_list

def get_ul(ov_list, vect_sqrt):
	inv_sqrt = 1/vect_sqrt
	res = list()
	for i in range(3):
		res.append(ov_list * inv_sqrt)
	return res

def main():
	r1 = "-4, 1, -5"
	r2 = "-2, -3, -4"
	force = "10i + 4j - 8k"
	force = sanitize_input(force)
	fsign, ssign = get_vector_sign(force)
	force_list = first_second_sign(get_vector1(force), fsign, ssign)
	pr1 = get_vector2(r1)
	pr2 = get_vector2(r2)
	rprime = sub_vector(pr1, pr2)
	mp = multiply_vector(rprime, force_list) 

	other_vector = "3i - 4j + 5k"
	other_vector = sanitize_input(other_vector)
	ofsign, ossign = get_vector_sign(other_vector)
	other_vector = get_vector1(other_vector)
	ov_list = first_second_sign(other_vector, ofsign, ossign)
	
	vect_sum = sum(pow(num, 2) for num in ov_list)
	vect_sqrt = math.sqrt(vect_sum)
	print(f"vect_sqrt is {vect_sqrt}"
	ul = get_ul(ov_list, vect_sqrt)
	

if __name__ == "__main__":
	main()