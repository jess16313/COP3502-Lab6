def coding():
    password=input("what is your password?")
    finpassword=list(password)

    for i in range(0,8):
        finpassword[i]=int(finpassword[i])+3
        finpassword[i]=str(finpassword[i])

    finpassword=''.join(finpassword)
    print(finpassword)


if __name__ == "__main__":
    coding()