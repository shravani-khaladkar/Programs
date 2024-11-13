# Name: SHRAVANI KHALADKAR
#Roll No.: 35
#PRN - F23112040
#Class: SE Comp 2
#Batch - Q

"""
Problem Statement: 
Write a python program to store second year percentage of students in array. Write function for sorting array of floating point
numbers in ascending order using 
a) Insertion sort
b) Shell sort and display top five scores
"""

def accept(arr, n):
    for i in range(n):
        per = float(input("Enter percentage: "))
        arr.append(per)
    print("\nUnsorted array is: ")
    print(arr)

def insertion_sort(arr, n):
    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def shell_sort(arr, n):
    gap = n // 2
    while gap>0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j>= gap and arr[j-gap]>temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr


def main():
    while True:
        print("\n")
        print("\t1: Insertion sort")
        print("\t2: Shell sort")
        print("\t3: Exit")

        ch = int(input("Enter choice: "))

        if ch == 1:
            n = int(input("Enter number of students: "))
            arr = []
            accept(arr, n)
            a = insertion_sort(arr, n)
            print("Sorted array using insertion sort: ")
            print(a)
            print("\nTop five scores: ")
            for i in range(1, 6):
                print(a[n-i], end=" ")

        if ch == 2:
            n = int(input("Enter number of students: "))
            arr = []
            accept(arr, n)
            a = shell_sort(arr, n)
            b = insertion_sort(a, n)
            print("Sorted array using shell sort: ")
            print(b)
            print("\nTop five scores: ")
            for i in range(1, 6):
                print(b[n-i], end=" ")


        elif ch >= 3:
            print("End of Program")
            break


main()

"""
OUTPUT:
	1: Insertion sort
	2: Shell sort
	3: Exit
Enter choice: 1
Enter number of students: 10
Enter percentage: 50.8
Enter percentage: 36
Enter percentage: 73
Enter percentage: 84.2
Enter percentage: 44.8
Enter percentage: 26
Enter percentage: 60
Enter percentage: 17.4
Enter percentage: 93
Enter percentage: 53

Unsorted array is: 
[50.8, 36.0, 73.0, 84.2, 44.8, 26.0, 60.0, 17.4, 93.0, 53.0]
Sorted array using insertion sort: 
[17.4, 26.0, 36.0, 44.8, 50.8, 53.0, 60.0, 73.0, 84.2, 93.0]

Top five scores: 
93.0 84.2 73.0 60.0 53.0 

	1: Insertion sort
	2: Shell sort
	3: Exit
Enter choice: 2
Enter number of students: 10
Enter percentage: 94
Enter percentage: 82.8
Enter percentage: 36
Enter percentage: 74
Enter percentage: 26
Enter percentage: 60.5
Enter percentage: 47.4
Enter percentage: 33
Enter percentage: 55
Enter percentage: 100

Unsorted array is: 
[94.0, 82.8, 36.0, 74.0, 26.0, 60.5, 47.4, 33.0, 55.0, 100.0]
Sorted array using shell sort: 
[26.0, 33.0, 36.0, 47.4, 55.0, 60.5, 74.0, 82.8, 94.0, 100.0]

Top five scores: 
100.0 94.0 82.8 74.0 60.5 

	1: Insertion sort
	2: Shell sort
	3: Exit
Enter choice: 3
End of Program

"""

