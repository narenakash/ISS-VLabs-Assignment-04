Questions = ["I.Inflectional morphemes change a noun’s gender, grammatical mood, number, etc. without changing the meaning of the word. Identify the inflectional morphological from the options below:","II.The following is a list of words and their oblique form. Identify the incorrect pair:","III.Figure out the number of morphemes in the word ‘insubordinate’:","IV.Choose the option which represents the incorrect standard morphological notation:"]
Option1 = ["1.Sad - Sadness ","1.जेबें - जेबों ","1.Four (4) ","1.ran : {run} + {-ed}"]
Option2 = ["2.Dog - Dogs ","2.ताले - तालों","2.Five (5) ","2.men : {man} + {-s} "]
Option3 = ["3.Sense - Nonsense ","3.हाथी - हाथी ","3.Three (3) ","3.Inconsistent : {in} + {consist} + {-ent} "]
Option4 = ["4.Quick - Quickly ","4.बिल्लियाँ - बिल्लियाँ ","4.Six (6) ","4.long : {long} "]
Answer = [2,4,2,3]
user_ans=[]
for i in range(4):
    print(Questions[i])
    print(Option1[i])
    print(Option2[i])
    print(Option3[i])
    print(Option4[i])
    temp=int(input("Enter Your Response :  "))
    user_ans.append(temp)
interator=-1
correct_answer=0
wrong_answer=''
for i in Answer:
    interator+=1
    if(i==user_ans[interator]):
        correct_answer+=1
    else:
        wrong_answer+=str(interator+1)+" "
print("Correct answered : "+ str(correct_answer))
print("Wrongly answered : "+ wrong_answer)