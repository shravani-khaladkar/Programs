# Name: SHRAVANI KHALADKAR
#Roll No.: 35
#PRN - F23112040
#Class: SE Comp 2
#Batch - Q

"""
Problem Statement:
In second year computer engineering class, group A student's play cricket, group B students play 
Badminton and Group C students play football
Write a python program using functions to compute following:-
    a) List of students who play cricket and badminton 
    b) List of students who play either cricket or badminton but not both
    c) Number of students who play neither cricket nor badminton
    d) Number of students who play cricket and football but not badminton
"""

#INPUT:
i = 0
def accept_set(A, Str):
    n = int(input("Enter the number of students playing %s: "%Str))
    for i in range(n):
        A.append(input("Enter the name of students: "))
        i += 1
    return A

def display_set(A, X):
    print("The student playing %s are: " %X)
    for i in range(len(A)):
        if i == len(A) - 1:
            print(A[i], end='\n') 
        else:
            print(A[i], end=' ')
    return A

def search_set(A, X):
    for i in range(len(A)):
        if A[i] == X:
            return True
    return False
    
def union_set(A, B, C):
    for i in range(len(A)):
        C.append(A[i])
    for i in range(len(B)):
        flag4 = search_set(A, B[i])
        if flag4 == 0:
            C.append(B[i])
    return C

def intersection_set(A, B, C):
    for i in range(len(A)):
        flag = search_set(B, A[i])
        if flag == True:
            C.append(A[i])
    for i in range(len(B)):
        flag = search_set(A, B[i])
        if flag == True:
            flag2 = search_set(C, B[i])
            if flag2 == False:
                C.append(B[i])
    return C
    
def symm_diff(A, B, C):
    for i in range(len(A)):
        if search_set(B, A[i]) == False:
            C.append(A[i])
    for i in range(len(B)):
        if search_set(A, B[i]) == False:
            C.append(B[i])
    return C

def diff_set(A, B, C):
    for i in range(len(B)):
        if search_set(A, B[i]) == False:
            C.append(B[i])
    return C

def main():
    Group_A = []
    Group_B = []
    Group_C = []

    while True:
        print("\t1: Accept the information")
        print("\t2: List of students who play both Cricket and Badminton")
        print("\t3: List of students who play either Cricket or Badminton")
        print("\t4: Number of students who play neither Cricket nor Badminton")
        print("\t5: Number of students who play Cricket and Football but not Badminton")
        print("\t6: Exit")

        ch = int(input("Enter your choice: "))
        if ch >= 6:
            print("End of program ")
            break

        elif ch == 1:
            Group_A = accept_set(Group_A, "Cricket")
            Group_B = accept_set(Group_B, "Badminton")
            Group_C = accept_set(Group_C, "Football")

            A = display_set(Group_A, "Cricket")
            B = display_set(Group_B, "Badminton")
            C = display_set(Group_C, "Football")

        elif ch == 2:
            Group_R = []
            print("The students playing Cricket and Badminton are: ")
            value = intersection_set(Group_A, Group_B, Group_R)
            print(Group_R)

        elif ch == 3:
            Group_S = []
            print("The students playing either Cricket or Badminton but not both are: ")
            value2 = symm_diff(Group_A, Group_B, Group_S)
            print(Group_S)

        elif ch == 4:
            Group_T = []
            Group_U = []
            print("The students playing neither Cricket nor Badminton are: ")
            value3 = diff_set(Group_A, Group_C, Group_T)
            value4 = diff_set(Group_B, Group_T, Group_U)
            print(Group_U)
            print("Number of students playing neither Cricket nor Badminton are: ")
            print(len(Group_U))

        elif ch == 5:
            Group_V = []
            Group_W = []
            print("The students playing Football and Cricket but not Badminton are: ")
            value5 = union_set(Group_A, Group_C, Group_V)
            value6 = diff_set(Group_B, Group_V, Group_W)
            print(Group_W)
            print("The number of students playing Football and Cricket but not Badminton are: ")
            print(len(Group_W))

    return value, value2, value3, value4, value5, value6

main()


"""
OUTPUT
        1: Accept the information
        2: List of students who play both Cricket and Badminton
        3: List of students who play either Cricket or Badminton
        4: Number of students who play neither Cricket nor Badminton
        5: Number of students who play Cricket and Football but not Badminton
        6: Exit
Enter your choice: 1
Enter the number of students playing Cricket: 5
Enter the name of students: a
Enter the name of students: x
Enter the name of students: b
Enter the name of students: i
Enter the name of students: c
Enter the number of students playing Badminton: 6
Enter the name of students: i
Enter the name of students: x
Enter the name of students: y
Enter the name of students: z
Enter the name of students: w
Enter the name of students: t
Enter the number of students playing Football: 6
Enter the name of students: x
Enter the name of students: c
Enter the name of students: t
Enter the name of students: h
Enter the name of students: f
Enter the name of students: o
The student playing Cricket are: 
a x b i c
The student playing Badminton are:
i x y z w t
The student playing Football are:
x c t h f o
        1: Accept the information
        2: List of students who play both Cricket and Badminton
        3: List of students who play either Cricket or Badminton
        4: Number of students who play neither Cricket nor Badminton
        5: Number of students who play Cricket and Football but not Badminton
        6: Exit
Enter your choice: 2
The students playing Cricket and Badminton are: 
['x', 'i']
        1: Accept the information
        2: List of students who play both Cricket and Badminton
        3: List of students who play either Cricket or Badminton
        4: Number of students who play neither Cricket nor Badminton
        5: Number of students who play Cricket and Football but not Badminton
        6: Exit
Enter your choice: 3
The students playing either Cricket or Badminton but not both are: 
['a', 'b', 'c', 'y', 'z', 'w', 't']
        1: Accept the information
        2: List of students who play both Cricket and Badminton
        3: List of students who play either Cricket or Badminton
        4: Number of students who play neither Cricket nor Badminton
        5: Number of students who play Cricket and Football but not Badminton
        6: Exit
Enter your choice: 4
The students playing neither Cricket nor Badminton are: 
['h', 'f', 'o']
Number of students playing neither Cricket nor Badminton are:
3
        1: Accept the information
        2: List of students who play both Cricket and Badminton
        3: List of students who play either Cricket or Badminton
        4: Number of students who play neither Cricket nor Badminton
        5: Number of students who play Cricket and Football but not Badminton
        6: Exit
Enter your choice: 5
The students playing Football and Cricket but not Badminton are: 
['a', 'b', 'c', 'h', 'f', 'o']
The number of students playing Football and Cricket but not Badminton are:
6
        1: Accept the information
        2: List of students who play both Cricket and Badminton
        3: List of students who play either Cricket or Badminton
        4: Number of students who play neither Cricket nor Badminton
        5: Number of students who play Cricket and Football but not Badminton
        6: Exit
Enter your choice: 6
End of program

"""
