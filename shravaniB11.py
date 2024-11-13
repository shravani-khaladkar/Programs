# Name: SHRAVANI KHALADKAR
#Roll No.: 35
#PRN - F23112040
#Class: SE Comp 2
#Batch - Q

"""
Problem Statement: 
a) Write a Python program to store roll numbers of students in array who attended training program in random order.
   Write function for searching whether particular student attended training program or not, using Linear and Sentinal Search.

b) Write a python program to store roll numbers of students in array who attended training program in sorted order.
   Write function for searching whether particular student attended training program or not, using Binary and Fibonacci Search.
"""

def linear_search(target, lst1):
    flag = 0
    i = 0
    for i in range(len(lst1)):
        if target == lst1[i]:
            flag = 1
            location = i
            break
    if flag == 1:
        print("Student with roll number", target, "attended the training program at location", location)
    else:
        print("Student with roll number", target, "did not attend the training program")
    return flag

def sentinal_search(arr, key):
    n = len(arr)
    last = arr[n-1]
    arr[n-1] = key
    i = 0
    
    while arr[i] != key:
        i += 1

    arr[n-1] = last
    
    if i < n - 1 or arr[n-1] == key:
        print("Student with roll number", key, "attended the training program at location", i)
    else:
        print("Student with roll number", key, "did not attend the training program")
    return i

def binary_search(arr, key):
    n = len(arr)
    flag = 0
    low = 0
    high = n-1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            position = mid
            flag = 1
            break
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1

    if flag == 1:
        print("Student with roll number", key, "attended the training program at location", position)
    else:
        print("Student with roll number", key, "did not attend the training program")
    return flag

def fibonacci_Search(arr, x, n): 
  
    fibMMm2 = 0 
    fibMMm1 = 1  
    fibM = fibMMm2 + fibMMm1  
  
    while (fibM < n): 
        fibMMm2 = fibMMm1 
        fibMMm1 = fibM 
        fibM = fibMMm2 + fibMMm1 
  
    offset = -1
  
    while (fibM > 1): 
        i = min(offset+fibMMm2, n-1) 
        if (arr[i] < x): 
            fibM = fibMMm1 
            fibMMm1 = fibMMm2 
            fibMMm2 = fibM - fibMMm1 
            offset = i 

        elif (arr[i] > x): 
            fibM = fibMMm2 
            fibMMm1 = fibMMm1 - fibMMm2 
            fibMMm2 = fibM - fibMMm1 

        else: 
            return i 
  
    if(fibMMm1 and arr[n-1] == x): 
        return n-1
    return -1

    
def main():
    while True:
        print("\t1: Unsorted Array")
        print("\t \t1: Linear Search")
        print("\t \t2: Sentinal Search")
        print("\t2: Sorted array")
        print("\t \t1: Binary Search")
        print("\t \t2: Fibonacci Search")
        print("\t3: Exit")

        ch = int(input("Enter your choice: "))
        if ch >= 3:
            print("End of program")
            break

        elif ch == 1:
            n = int(input("Enter the number of students in array: "))
            lst1 = []
            for i in range(n):
                roll = int(input("Enter roll number of student: "))
                lst1.append(roll)

            target = int(input("Enter roll number of student to search: "))
            ch2 = int(input("Enter your choice of search: "))

            if ch2 == 1:
                linear_search(target, lst1)

            elif ch2 == 2:
                sentinal_search(lst1, target)

        elif ch == 2:
            print("Enter sorted array")
            n = int(input("Enter the number of students in array: "))
            lst1 = []
            for i in range(n):
                roll = int(input("Enter roll number of student: "))
                lst1.append(roll)

            target = int(input("Enter roll number of student to search: "))

            ch2 = int(input("Enter your choice of search: "))

            if ch2 == 1: 
                binary_search(lst1, target)

            elif ch2 == 2:
                ind = fibonacci_Search(lst1, target, n) 
                if ind>=0: 
                    print("Found at index:",ind) 
                else: 
                    print(target,"isn't present in the array")

main()

"""
OUTPUT:
1: Unsorted array
	1: Linear Search
	2: Sentinel Search
2: Sorted Array
	1: Binary Search
	2: Fibonacci Search
Enter your choice: 1	
Enter the number of students in array: 5
Enter roll number of students: 8
Enter roll number of students: 4
Enter roll number of students: 6
Enter roll number of students: 0
Enter roll number of students: 12
Enter target: 4
Enter your choice of search: 1
Student with roll number 4 attended the training program at location 1

1: Unsorted array
	1: Linear Search
	2: Sentinel Search
2: Sorted Array
	1: Binary Search
	2: Fibonacci Search
Enter your choice: 1	
Enter the number of students in array: 5
Enter roll number of students: 4
Enter roll number of students: 0
Enter roll number of students: 6
Enter roll number of students: 9
Enter roll number of students: 3
Enter target: 4
Enter your choice of search: 2
Student with roll number 4 attended the training program at location 0

1: Unsorted array
	1: Linear Search
	2: Sentinel Search
2: Sorted Array
	1: Binary Search
	2: Fibonacci Search
Enter your choice: 2	
Enter the number of students in array: 5
Enter roll number of students: 2
Enter roll number of students: 4
Enter roll number of students: 7
Enter roll number of students: 9
Enter roll number of students: 13
Enter target: 13
Enter your choice of search: 1
Student with roll number 13 attended the training program at location 4
1: Unsorted array
	1: Linear Search
	2: Sentinel Search
2: Sorted Array
	1: Binary Search
	2: Fibonacci Search
Enter your choice: 2	
Enter the number of students in array: 5
Enter roll number of students: 3
Enter roll number of students: 7
Enter roll number of students: 9
Enter roll number of students: 11
Enter roll number of students: 15
Enter target: 9
Enter your choice of search: 2
Student with roll number 9 attended the training program at location 2

1: Unsorted array
	1: Linear Search
	2: Sentinel Search
2: Sorted Array
	1: Binary Search
	2: Fibonacci Search
Enter your choice: 3
End of program
"""


        