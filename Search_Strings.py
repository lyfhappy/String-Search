str_input = input("Enter a String:")
# given List of strings
str_list = ["apple", "grapes", "bananas"]
str_filter = list(filter(lambda x: str_input in x, str_list))
if(len(str_filter)):
    print(f"Sub String:{str_input} is present in String: {str_filter}")

else:
    print(f"No Strings matches the string ")