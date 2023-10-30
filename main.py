def coding():
    password = input("Please enter your password to encode: ")
    finpassword = []

    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        finpassword.append(encoded_digit)

    finpassword = ''.join(finpassword)
    return finpassword


# Yiru Chen
def decoding(encoded_password):
    decoded_digits = []

    # Loop through each digit in the encoded password
    for digit in encoded_password:
        # Decode the digit by subtracting 3 and taking the modulus 10
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_digits.append(decoded_digit)

    # Join the decoded digits to form the decoded password
    decoded_password = ''.join(decoded_digits)
    return decoded_password


if __name__ == "__main__":
    encoded_password = ""  # Initialize the encoded_password variable as an empty string

    program = True
    while program:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        choice = input("Please enter an option: ")

        if choice == "1":
            # Encode the password and store it in encoded_password
            encoded_password = coding()
            print("Your password has been encoded and stored!")

        elif choice == "2":
            if encoded_password:
                # If an encoded password is available, decode it
                decoded_password = decoding(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            else:
                print("No encoded password available. Please choose option 1 to encode first.")

        elif choice == "3":
            program = False