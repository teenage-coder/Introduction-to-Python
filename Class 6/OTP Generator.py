import random

otp = random.randint(100000,999999)


print(otp)

user = int(input("Enter the OTP: "))

if (user == otp):
    print("Welcome!")
    
else:
    print("Incorrect OTP")


