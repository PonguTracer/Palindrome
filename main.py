input_str = input("Is your word a palindrome?: ")
remove_whitespace = input_str.replace(" ", "")

if remove_whitespace == remove_whitespace[::-1]:
    print(f"{input_str} is a palindrome")
else:
    print(f"{input_str} is not a palindrome")
