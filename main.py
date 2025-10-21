

Alphabets = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(Start_text, Shift_amount, ciper_direction):
    Text_res = ""
    for letter in Start_text:
        position = Alphabets.index(letter)
        if ciper_direction == "decode":
            Shift_amount *= -1
            # 5 * -1  = -5
        new_positon = Shift_amount + position
        Text_res += Alphabets[new_positon]
    print(f"The {ciper_direction} text is {Text_res}")  
            

direction = input("""Type 'encode' to encrypt, Type 'decode' to Decrypt : """)
text = input("Type your Message : ").lower()
shift = int(input("Type Your Shift Number : "))

ceaser(Start_text= text, Shift_amount= shift, ciper_direction= direction)
