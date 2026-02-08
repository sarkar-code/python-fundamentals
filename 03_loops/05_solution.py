input_Str = "tomaato"

for char in input_Str:
    print(char)
    if input_Str.count(char) == 1:
        print("char is: ", char)
        break