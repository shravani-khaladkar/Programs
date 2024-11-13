# Name: SHRAVANI KHALADKAR
#Roll No.: 35
#PRN - F23112040
#Class: SE Comp 2
#Batch - Q

"""
Problem Statement: 
Write a Python program to store marks scored in subject “Fundamental of Data Structure” by N students in the class. 
Write functions to compute following:
a) The average score of class
b) Highest score and lowest score of class
c) Count of students who were absent for the test
d) Display mark with highest frequency
"""

i = 0

def accept(A):
	n = int(input("Enter the number of students: "))
	for i in range(n):
		marks = int(input("Enter marks of student (-1 if absent): "))
		A.append(marks)
		i +=1
	return A

def disply(A):
	for i in range(len(A)):
		if i == len(A)-1:
			print(A[i], end='\n')
		else:
			print(A[i], end=' ')
	return A

def average_marks(A):
	sum = 0
	count = 0 
	for i in range(len(A)):
		if A[i] > -1:
			sum = sum + A[i]
		count += 1
	if count == 0:
		return 0
	avg = sum/count
	return avg

def max_score(A):
	max = A[0]
	for i in range(len(A)):
		if A[i]>max:
			max = A[i]
	return max

def min_score(A):
	min = A[0]
	for i in range(len(A)):
		if A[i] != -1:
			if A[i] < min:
				min = A[i]
	return min

def absent(A):
	count = 0
	for i in range(len(A)):
		if A[i] == -1:
			count += 1
	return count

def high_freq(A):
	max_count = 0
	for i in range(len(A)):
		if A[i] != -1:
			count = 0
			for j in range (len(A)):
				if A[i] == A[j]:
					count += 1
			if count > max_count:
				max_count = count
				element = A[i]
	print("Marks with highest frequency is: ", element)
	print("Frequency is: ", max_count)
	return

def main():
	A = []
	
	while True:
		print()
		print("********** DISPLAY MENU **********")
		print("1. Accept and Display")
		print("2. The average score of class")
		print("3. Highest and lowest score of class")
		print("4. Count of absent students")
		print("5. Marks with highest freqency")
		print("6. Exit")

		ch = int(input("Enter choice: "))
		
		if ch == 1:
			accept(A)
			print("List of marks of students: ")
			disply(A)

		elif ch == 2:
			x = average_marks(A)
			print("Average marks of students is: ", x)

		elif ch == 3:
			y = max_score(A)
			z = min_score(A)
			print("Highest score is: ", y)
			print("Lowest score is: ", z)
			
		elif ch == 4:
			u = absent(A)
			print("Total number of students absent are: ", u)

		elif ch == 5: 
			v = high_freq(A)

		elif ch == 6:
			print("End of program")
			break

		else: 
			print("Invalid choice!!")

main()

"""
OUTPUT:
	1: Accept the information
	2: Average marks of the students
	3: Number of students absent
	4: Maximum and minimum marks
	5: Highest frequency marks scored
	6: Exit the program
Enter your choice: 1
Enter the number of students: 10
Enter the marks of student (or -1 for absent): 55
Enter the marks of student (or -1 for absent): -1
Enter the marks of student (or -1 for absent): 99
Enter the marks of student (or -1 for absent): 36
Enter the marks of student (or -1 for absent): 70
Enter the marks of student (or -1 for absent): 85
Enter the marks of student (or -1 for absent): 55
Enter the marks of student (or -1 for absent): 37
Enter the marks of student (or -1 for absent): -1
Enter the marks of student (or -1 for absent): 88
The marks of students are: 
55
-1
99
36
70
85
55
37
-1
88
	1: Accept the information
	2: Average marks of the students
	3: Number of students absent
	4: Maximum and minimum marks
	5: Highest frequency marks scored
	6: Exit the program
Enter your choice: 2
The average marks of students are: 
64.0
	1: Accept the information
	2: Average marks of the students
	3: Number of students absent
	4: Maximum and minimum marks
	5: Highest frequency marks scored
	6: Exit the program
Enter your choice: 3
The number of students absent are: 
2
	1: Accept the information
	2: Average marks of the students
	3: Number of students absent
	4: Maximum and minimum marks
	5: Highest frequency marks scored
	6: Exit the program
Enter your choice: 4
Minimum mark is: 36
Maximum mark is: 99
	1: Accept the information
	2: Average marks of the students
	3: Number of students absent
	4: Maximum and minimum marks
	5: Highest frequency marks scored
	6: Exit the program
Enter your choice: 5
Marks with highest frequency is 55 (2 times)
	1: Accept the information
	2: Average marks of the students
	3: Number of students absent
	4: Maximum and minimum marks
	5: Highest frequency marks scored
	6: Exit the program
Enter your choice: 6
End of program

"""