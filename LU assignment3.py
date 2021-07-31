import  random as r
import string
length = 10
OTP = ' '
charecters = string.ascii_letters + string.digits
for i in range(length):
    OTP = OTP+r.choice(charecters)
print('OTP:',OTP)
