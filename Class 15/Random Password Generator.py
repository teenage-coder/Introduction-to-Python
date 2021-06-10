import random

length = int(input("Enter the length of password: "))
password = ""

for i in range(length):

    prob = random.randint(0,2)
    
    if prob == 0:
        password = password + str(random.randint(0,9))      # 0-9
        
    if prob == 1:
        password  = password + chr(random.randint(97,122))  # a-z

    if prob == 2:
        password  = password + chr(random.randint(65,90))   # A-Z

print(password)
