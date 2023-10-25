password=input("what is your password?")
finpassword=list(password)

for i in range(0,8):
    finpassword[i]=int(finpassword[i])+3
    finpassword[i]=str(finpassword[i])

''.join(finpassword)
print(finpassword)
