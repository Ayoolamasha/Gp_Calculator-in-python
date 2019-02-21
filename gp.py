# CREATING A G.P/CGPA CALACULATOR
# 1. VARIABLES: SEMESTER TO ASK FOR THE SEMESTER THE STUDENT IS IN, SUBJECTS, UNIT,GRADE,GRADE COMPUTATION:WHICH WILL BE
# THE TOTAL GRADE AFTER MULTIPLYING THE GRADES AND THW UNITS TOGETHER. TOTAL UNIT: WILL BE THE TOTAL UNIT
# MULTIPLIED BT THE GRADE COMPUTATION
# 2. ADVICE: THIS VARBLE WILL CHECK FOR THE COURSES WITH THE LOWEST SCORE AND ADVICE THE STUDENT TO WORK ON IT 
# 3. GOALS: THIS VARIBLE WILL LIST THE KIND OF RESULTS A STUDENT CAN COME OUT WITH RANGING FROM FIRST CLAA TO PASS
# 4. THERE WILLL BE AN IMPLEMENTATION THAT WILL CHECK YOUR CURRENT GRADE WITH YOUR GOALS. IF IT IS NOT UP TO PAR 
# IT WILL TELL YOU HOW MUCH GP YOU NEED TO ADD. THIS COMPUTATION WILL BE AVAILABLE WHEN YOU WANT TO CHECK YOUR CURRENT CGPA 

total_grade_1 = 0
total_grade_2 = 0
while True:
	# name = input("Enter your name: ")
	# matric_no = input("Enter your matric number: ").upper()
	# if "U" in matric_no:
	# 	department = input("Enter Your Department: ")
	# else:
	# 	print("You are not a student of OUI")
	# 	break
	# print ("\n")
	semester = int(input('Which Semester\'s Gp do you want to? \nEnter 1 if First Semester \nEnter 2 Second Semester \nEnter 3 to calculate CGPA \nEnter 0 to exit program: \n'))

	if semester == 1:
		x = int(input("How many courses are you offering: "))
		total_unit = int(input("What is your total unit: "))
		print ("input your %d courses" % (x))
		for i in range(x):
			subject = input('Enter Subjects: ')
			unit = int(input('Enter unit: '))
			grade = int(input('Enter grade: '))
			if i == i:
				if grade >=70 and grade <= 100:
					grade = unit * 5
					print ("You got an A which is: ",grade)
				elif grade >= 60 and grade <=69:
					grade = unit * 4
					print("You got a B which is: ",grade)
				elif grade >=50 and grade <=59:
					grade = unit * 3
					print("You got a C which is: ",grade)
				elif grade >=45 and grade <= 50:
					grade = unit * 2
					print("You got a D which is: ",grade)
				elif grade >= 0 and  grade <= 45:
					grade = unit * 0
					print ("You got an F which is: ",grade)

				# total_grade += grade
				# print(total_grade)
				total_grade_1 += grade
		y=int(input("Press 4 to calculate: "))
		if y == 4:
			print("Your First Semester GP is: ",total_grade_1 / total_unit)
			print('\n\n')
		break
	
	if semester == 2:
		x = int(input("How many courses are you offering: "))
		total_unit = int(input("What is your total unit: "))
		print ("input your %d courses" % (x))
		for i in range(x):
			subject = input('Enter Subjects: ')
			unit = int(input('Enter unit: '))
			grade = int(input('Enter grade: '))
			if i == i:
				if grade >=70 and grade <= 100:
					grade = unit * 5
					print ("You got an A which is: ",grade)
				elif grade >= 60 and grade <=69:
					grade = unit * 4
					print("You got a B which is: ",grade)
				elif grade >=50 and grade <=59:
					grade = unit * 3
					print("You got a C which is: ",grade)
				elif grade >=45 and grade <= 50:
					grade = unit * 2
					print("You got a D which is: ",grade)
				elif grade >= 0 and  grade <= 45:
					grade = unit * 0
					print ("You got an F which is: ",grade)

				# total_grade += grade
				# print(total_grade)
				total_grade_2 += grade
		y=int(input("Press 4 to calculate: "))
		if y == 4:
			print("Your Second Semester GP is: ",total_grade_2 / total_unit)
			print('\n\n\n')
		break
	if semester == 3:
		print("Input Your First Semester Results \n")
		x = int(input("How many courses are you offering: "))
		total_unit = int(input("What is your total unit: "))
		print ("input your %d courses" % (x))
		for i in range(x):
			subject = input('Enter Subjects: ')
			unit = int(input('Enter unit: '))
			grade = int(input('Enter grade: '))
			if i == i:
				if grade >=70 and grade <= 100:
					grade = unit * 5
					print ("You got an A which is: ",grade)
				elif grade >= 60 and grade <=69:
					grade = unit * 4
					print("You got a B which is: ",grade)
				elif grade >=50 and grade <=59:
					grade = unit * 3
					print("You got a C which is: ",grade)
				elif grade >=45 and grade <= 50:
					grade = unit * 2
					print("You got a D which is: ",grade)
				elif grade >= 0 and  grade <= 45:
					grade = unit * 0
					print ("You got an F which is: ",grade)

				# total_grade += grade
				# print(total_grade)
				total_grade_1 += grade
		y=int(input("Press 4 to calculate: "))
		if y == 4:
			grade_1 = total_grade_1 / total_unit
			print("Your First Semester GP is: ", grade_1)

			# print("Your First Semester GP is: ",total_grade_1 / total_unit)
			print('\n\n')

		print ("Input your Second Semester Results \n")

		x = int(input("How many courses are you offering: "))
		total_unit = int(input("What is your total unit: "))
		print ("input your %d courses" % (x))
		for i in range(x):
			subject = input('Enter Subjects: ')
			unit = int(input('Enter unit: '))
			grade = int(input('Enter grade: '))
			if i == i:
				if grade >=70 and grade <= 100:
					grade = unit * 5
					print ("You got an A which is: ",grade)
				elif grade >= 60 and grade <=69:
					grade = unit * 4
					print("You got a B which is: ",grade)
				elif grade >=50 and grade <=59:
					grade = unit * 3
					print("You got a C which is: ",grade)
				elif grade >=45 and grade <= 50:
					grade = unit * 2
					print("You got a D which is: ",grade)
				elif grade >= 0 and  grade <= 45:
					grade = unit * 0
					print ("You got an F which is: ",grade)

				# total_grade += grade
				# print(total_grade)
				total_grade_2 += grade
		y=int(input("Press 4 to calculate: "))
		if y == 4:
			grade_2= total_grade_2 / total_unit
			print("Your Second Semester GP is: ",grade_2)
			# print("Your Second Semester GP is: ",total_grade_2 / total_unit)
			print('\n\n')
			cgpa= grade_1 + grade_2
			cgpa /=2
			print ("Your CGPA is: ", cgpa)
			if cgpa >=4.50 and cgpa<=5.00:
				print ("You are on First Class")
			elif cgpa >=3.50 and cgpa<=4.49:
				print ("You are on Second Class Upper")
			elif cgpa >=2.40 and cgpa<=3.49:
				print ("You are on Second Class Lower")
			elif cgpa >=1.50 and cgpa<=2.39:
				print ("You are on Third Class")
			elif cgpa >=1.00 and cgpa<=1.49:
				print ("You are on Pass")
			elif cgpa >=0.00 and cgpa<=0.90:
				print ("Fail")
			break

	if semester == 0:
		break
