# S19CS6.201 Introduction to Software Systems
# Assignment 04 - Virtual Labs, IIIT Hyderabad 
# Natural Language Proessing Lab, Morphology 

import math
input_words = [ 'बच्चा', 'लड़का', 'घोड़ा', 'गधा', 'बच्ची', 'लड़की', 'नदी', 'गली', 'माला', ' लता', 'शाखा', 'गाथा', 'माली', 'जोहरी', 'कूली', 'आदमी']
ad_list = [ 'आ', 'आओं', 'आयें', 'इयाँ', 'इयों', 'ई', 'ए', 'ओं' ]

list1 = [ 'Singular', 'Plural', 'Singular', 'Plural' ]
list2 = [ 'Direct Case', 'Direct Case', 'Oblique Case', 'Oblique Case' ]

alist1 = [ '0', '0', '0', '6', '0', '6', '0' ,'7' ]
alist2 = [ '5', '5', '5', '3', '5', '5', '5' ,'4' ]
alist3 = [ '0', '0', '0', '2', '0', '0', '0' ,'1' ]
alist4 = [ '5', '5', '5', '5', '5', '5', '5' ,'4' ]
answer_list = []

# Function to evaluate the answers entered by the user

def checkAnswer(x):
    if x == 1:
        for x in range(0,8,2):
            if alist1[x] == answer_list[x] and alist1[x+1] == answer_list[x+1]:
                print("Add : ",ad_list[int(answer_list[x])]," Delete : ",ad_list[int(answer_list[x+1])]," Correct")
            else:
                print("Add : ",ad_list[int(answer_list[x])]," Delete : ",ad_list[int(answer_list[x+1])]," Incorrect")
    elif x == 2:
        for x in range(0,8,2):
            if alist2[x] == answer_list[x] and alist2[x+1] == answer_list[x+1]:
                print("Add : ",ad_list[int(answer_list[x])]," Delete : ",ad_list[int(answer_list[x+1])]," Correct")
            else:
                print("Add : ",ad_list[int(answer_list[x])]," Delete : ",ad_list[int(answer_list[x+1])]," Incorrect")
    elif x == 3:
        for x in range(0,8,2):
            if alist3[x] == answer_list[x] and alist3[x+1] == answer_list[x+1]:
                print("Add : ",ad_list[int(answer_list[x])]," Delete : ",ad_list[int(answer_list[x+1])]," Correct")
            else:
                print("Add : ",ad_list[int(answer_list[x])]," Delete : ",ad_list[int(answer_list[x+1])]," Incorrect")
    elif x == 4:
        for x in range(0,8,2):
            if alist4[x] == answer_list[x] and alist4[x+1] == answer_list[x+1]:
                print("Add : ",ad_list[int(answer_list[x])]," Delete : ",ad_list[int(answer_list[x+1])]," Correct")
            else:
                print("Add : ",ad_list[int(answer_list[x])]," Delete : ",ad_list[int(answer_list[x+1])]," Incorrect")

# Function to display the correct answers

def viewAnswer(x):
    if x == 1:
        for x in range(0,8,2):
            print("Add : ",ad_list[int(alist1[x])]," Delete : ",ad_list[int(alist1[x+1])])
    if x == 2:
        for x in range(0,8,2):
            print("Add : ",ad_list[int(alist2[x])]," Delete : ",ad_list[int(alist2[x+1])])
    if x == 3:
        for x in range(0,8,2):
            print("Add : ",ad_list[int(alist3[x])]," Delete : ",ad_list[int(alist3[x+1])])
    if x == 4:
        for x in range(0,8,2):
            print("Add : ",ad_list[int(alist4[x])]," Delete : ",ad_list[int(alist4[x+1])])


# Get the input word for the experiment
print(input_words)
n = input("Enter the input word index.   ")

# Error Handling (As an example)
if int(n) > 15 or int(n) < 0:
    print("Invalid Index. Try again!")
    exit()

# Get the answers from the user for the experiment (Assumed that the inputs will be correct)
for i in range(4):
    print("\n", ad_list)
    print(list1[i], list2[i])
    x = input("Choose the add word index.      ")
    answer_list.append(x)
    y = input("Choose the delete word index.   ")
    answer_list.append(y)

choice1 = input("Submit Answer Y/N ?   ")

# Call the corresponding function to evaluate user's answer
if choice1 == 'Y' or choice1 == 'y':
    print("\nAnswer List: ", answer_list)
    checkval = math.ceil( ( (int(n)+1)/4) )
    checkAnswer( checkval )

choice2 = input("\nView Answer Y/N ?   ")

# Call the corresponding function to show the solution for the user's word
if choice2 == 'Y' or choice2 == 'y':
    viewval = math.ceil( ( (int(n)+1)/4) ) 
    viewAnswer( checkval )
    

# Naren Akash, R J and Kowshik Vishwanadha
# April 07, 2019 - Sunday
# International Institute of Information Technology, Hyderabad



