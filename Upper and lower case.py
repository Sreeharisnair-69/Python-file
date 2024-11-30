def letters():
    string = input("Enter a string: ")
    upper_count = 0
    lower_count = 0

    for i in string:
        if i.isupper():
            upper_count += 1
        if i.islower():
            lower_count += 1
    print(f"Upper count is {upper_count}")
    print(f"Lower count is {lower_count}")

letters()