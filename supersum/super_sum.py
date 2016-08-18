def super_sum(*args):
	'''
	Takes in elements 
	in a list and returns
	total  sum
	'''
	#first make the total for all the list elements be 0
	list_total = 0 
	#first make the total for all integers be 0
	total_num = 0 
	# loops through all content passed in the list
	for content in args: 
		# condition for if the element found is a list
		if type(content) is list:
			for item in content:
				if type(item) is int:
					# adds the elements in an individual list
					list_total = item + list_total
				else:
					return ' You have entered a non integer'
		else:
			#checking to see if content passed is an integer
			if type(content) is int: 
				total_num = content + total_num
			else:
				return 'you entered a non integer item'
	# now find the sum of all elements
	sum_total = total_num + list_total 