import logo
Alphabets = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(Start_text, Shift_amount, ciper_direction):
    Text_res = ""
    if ciper_direction == "decode":
            Shift_amount *= -1
    for letter in Start_text:
        if letter in Alphabets:
            position = Alphabets.index(letter)
            new_positon = position + Shift_amount
            Text_res += Alphabets[new_positon]
        else:
             Text_res +=letter
            
    print(f"The {ciper_direction} text is {Text_res}")  
            
print(logo.l)
flag = True
while flag:
    direction = input("""Type 'encode' to encrypt, Type 'decode' to Decrypt : """)
    text = input("Type your Message : ").lower()
    shift = int(input("Type Your Shift Number : "))

    shift %= 26
    ceaser(Start_text= text, Shift_amount= shift, ciper_direction= direction)
    r = input("Do you want to Run is again 'Yes' or 'No' : " ).lower()
    if r == "no":
         flag = False
         print("GoodBye !")
