# Name: SHRAVANI KHALADKAR
#Roll No.: 35
#PRN - F23112040
#Class: SE Comp 2
#Batch - Q

"""
Problem Statement:
Write a python program to compute following operations on string:
a) To display word with the longest length
b) To determine the frequency of occurrence of particular character in the string
c) To check whether given string is palindrome or not
d) To display index of first appearance of the substring
e) To count the occurrences of each word in a given string
"""

def display_longest_word():
    string = input("Enter the main string: ")
    i = 0
    max_word = ""

    while i < len(string):
        words = ""

        while string[i] != ' ':
            words += string[i]
            i = i + 1
            if i == len(string):
                break
        if i != len(string):
            while string[i] == " ":
                i += 1

        if len(max_word) < len(words):
            max_word = words

    print("Word with longest length is: ", max_word)
    print("Length of longest string is: ", len(max_word))
    return max_word


def char_frequency():
    string = str(input("Enter the main string: "))
    char = str(input("Enter the character: "))
    count = 0
    for i in range(len(string)):
        if string[i] == char:
            count += 1
    print("Frequency of character is: ", count)
    return count

def check_palindrome():
    string = str(input("Enter the string: "))
    b = 0
    e = len(string) - 1
    while b < e:
        if string[b] != string[e]:
            break
        else:
            b += 1
            e -= 1
    if b<e:
        print("The string is not a palindrome")
    else:
        print("The string is a palindrome")
    return

def first_apperance():
    string = str(input("Enter the main string: "))
    substring = str(input("Enter the substring: "))
    L1 = len(string)
    L2 = len(substring)
    if L1>=L2:
        for i in range(L1-L2+1):
            flag = 1
            for j in range(L2):
                if string[i+j]!=substring[j]:
                    flag = 0
                    break
            if flag==1:
                print("First appearance of the substring is at index: ", i)
                break
        if flag==0:
            print("Substring is not found")
    else:
        print("Substring is greater than main string")

def count_occurences():
    string = str(input("Enter the main string: "))
    i=0
    word_list = []
    count = []
    while i < len(string):
        words = ""
        while string[i] != ' ':
            words += string[i]
            i = i + 1
            if i == len(string):
                break
        if i != len(string):
            while string[i] == ' ':
                i += 1
        if len(word_list)==0:
            word_list.append(words)
            count.append(1)
        else: 
            flag = 1
            for j in range(len(word_list)):
                if word_list[j] == words:
                    count[j] += 1
                    flag = 0
                    break
            if flag == 1:
                word_list.append(words)
                count.append(1)

    for i in range(len(word_list)):
        print(word_list[i], ":", count[i])

        
def main():
    while True:
        print("\t1: To display word with longest length")
        print("\t2: To determine the frequency of occurrence of particular character in the string")
        print("\t3: To check whether given string is palindrome or not")
        print("\t4: To display index of first appearance of the substring")
        print("\t5: To count the occurrences of each word in a given string")
        print("\t6: Exit")

        ch = int(input("Enter your choice: "))
        if ch >= 6:
            print("End of program")
            break

        elif ch == 1:
            display_longest_word()

        elif ch == 2:
            char_frequency()

        elif ch == 3:
            check_palindrome()
        
        elif ch==4:
            first_apperance()

        elif ch==5:
            count_occurences()

main()

"""
OUTPUT:
1: To display word with longest length
2: To determine the frequency of occurrence of particular character in the string
3: To check whether given string is palindrome or not
4: To display index of first appearance of the substring
5: To count the occurrences of each word in a given string
6: Exit
Enter your choice: 1
Enter the main string: This is python programming
Word with longest length is: programming
Length of longest string is: 11

1: To display word with longest length
2: To determine the frequency of occurrence of particular character in the string
3: To check whether given string is palindrome or not
4: To display index of first appearance of the substring
5: To count the occurrences of each word in a given string
6: Exit
Enter your choice: 2
Enter the main string: This is python programming
Enter the character: i
Frequency of character is: 3

1: To display word with longest length
2: To determine the frequency of occurrence of particular character in the string
3: To check whether given string is palindrome or not
4: To display index of first appearance of the substring
5: To count the occurrences of each word in a given string
6: Exit
Enter your choice: 3
Enter the string: malayalam
This string is a palindrome

1: To display word with longest length
2: To determine the frequency of occurrence of particular character in the string
3: To check whether given string is palindrome or not
4: To display index of first appearance of the substring
5: To count the occurrences of each word in a given string
6: Exit
Enter your choice: 4
Enter the main string: This is operation in python program
Enter the substring: python
First appearance of the substring is at index: 21

1: To display word with longest length
2: To determine the frequency of occurrence of particular character in the string
3: To check whether given string is palindrome or not
4: To display index of first appearance of the substring
5: To count the occurrences of each word in a given string
6: Exit
Enter your choice: 5
Enter the main string: python programming is very very exciting
python: 1
programming: 1
is: 1
very: 2
exciting: 1

1: To display word with longest length
2: To determine the frequency of occurrence of particular character in the string
3: To check whether given string is palindrome or not
4: To display index of first appearance of the substring
5: To count the occurrences of each word in a given string
6: Exit
Enter your choice: 6
End of program
"""