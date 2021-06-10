
questions = {1 : {"Q" : "Python is case-sensitive or not?" ,
                  "Op1" : "Yes" ,
                  "Op2" : "No",
                  "A" : "A"},
             
             2 : {"Q" : "Python is having variables?" ,
                  "Op1" : "Yes" ,
                  "Op2" : "No",
                  "A" : "A"},

             3 : {"Q" : "What is a list in Python?" ,
                  "Op1" : "Data-Type" ,
                  "Op2" : "Data-Strucutre",
                  "A" : "B"},
             
             4 : {"Q" : "What is a list in Python?" ,
                  "Op1" : "Data-Type" ,
                  "Op2" : "Data-Strucutre",
                  "A" : "B"},
             
             5 : {"Q" : "What is a list in Python?" ,
                  "Op1" : "Data-Type" ,
                  "Op2" : "Data-Strucutre",
                  "A" : "B"}}

score = 0

for question in questions.keys():
    
    print("Q", question, questions[question]["Q"])
    print("(A) ", questions[question]["Op1"])
    print("(B) ", questions[question]["Op2"])

    answer = input("Enter your option: ")

    if (answer  == questions[question]["A"]):
        score = score + 10
    else:
        score = score - 5
    
    print("***************************")


print("You have scored", score , 'Marks out of', len(questions.keys()) * 10)
print("Average: ", score / len(questions.keys()) * 10 )
