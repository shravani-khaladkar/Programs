# Name: SHRAVANI KHALADKAR
#Roll No.: 35
#PRN - F23112040
#Class: SE Comp 2
#Batch - Q

"""
Problem Statement:
Write a python program to store second year percentage of students in array. Write function for sorting array of floating point
numbers in ascending order using 
a) Selection sort
b) Bubble sort and display top five scores
"""
  
def selection_sort(arr, n):
    for i in range(n):
        min_ind = i
        for j in range(i+1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr

def bubble_sort(arr, n):
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr [j], arr[j+1] = arr[j+1], arr[j]
    return arr

def accept(arr, n):
    for i in range(n):
        per = float(input("Enter percentage of student: "))
        arr.append(per)
    print("Array of percentage: ")
    print(arr)
    return arr

def main():
    while True:
        print("\n")
        print("\t1: Selection sort")
        print("\t2: Bubble sort")
        print("\t3: Exit")

        ch = int(input("Enter choice: "))


        if ch == 1:
            n = int(input("\nEnter number of students: "))
            arr = []
            accept(arr, n)
            a = selection_sort(arr, n)
            print("Sorted array using selection sort: ")
            print(a)
            print("\nTop five scores: ")
            for i in range(1, 6):
                print(a[n-i], end=" ")
        
        elif ch == 2:
            n = int(input("\nEnter number of students: "))
            arr = []
            accept(arr, n)
            a = bubble_sort(arr, n)
            print("Sorted array using bubble sort: ")
            print(a)
            print("\nTop five scores: ")
            for i in range(1, 6):
                print(a[n-i], end=" ")

        elif ch >= 3:
            print("End of Program")
            break

main()

"""
OUTPUT:
	1: Selection sort
	2: Bubble sort
	3: Exit
Enter choice: 1

Enter number of students: 10
Enter percentage of student: 33
Enter percentage of student: 45
Enter percentage of student: 68
Enter percentage of student: 25
Enter percentage of student: 87
Enter percentage of student: 28
Enter percentage of student: 40
Enter percentage of student: 55
Enter percentage of student: 92
Enter percentage of student: 86
Array of percentage: 
[33.0, 45.0, 68.0, 25.0, 87.0, 28.0, 40.0, 55.0, 92.0, 86.0]
Sorted array using selection sort: 
[25.0, 28.0, 33.0, 40.0, 45.0, 55.0, 68.0, 86.0, 87.0, 92.0]

Top five scores: 
92.0 87.0 86.0 68.0 55.0 

	1: Selection sort
	2: Bubble sort
	3: Exit
Enter choice: 2

Enter number of students: 10
Enter percentage of student: 56
Enter percentage of student: 99
Enter percentage of student: 34
Enter percentage of student: 100
Enter percentage of student: 69
Enter percentage of student: 75
Enter percentage of student: 48
Enter percentage of student: 63
Enter percentage of student: 80
Enter percentage of student: 72
Array of percentage: 
[56.0, 99.0, 34.0, 100.0, 69.0, 75.0, 48.0, 63.0, 80.0, 72.0]
Sorted array using bubble sort: 
[34.0, 48.0, 56.0, 63.0, 69.0, 72.0, 75.0, 80.0, 99.0, 100.0]


Top five scores: 
100.0 99.0 80.0 75.0 72.0 

	1: Selection sort
	2: Bubble sort
	3: Exit
Enter choice: 3
End of Program
"""