#  project 8 : Caesar Chipher 

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']



logo = '''
 ███████╗ █████╗ ███████╗███████╗ █████╗ ██████╗      ██████╗██╗  ██╗██╗██████╗ ██╗  ██╗███████╗██████╗ 
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗    ██╔════╝██║  ██║██║██╔══██╗██║  ██║██╔════╝██╔══██╗
███████╗███████║███████╗███████╗███████║██████╔╝    ██║     ███████║██║██████╔╝███████║█████╗  ██████╔╝
╚════██║██╔══██║╚════██║╚════██║██╔══██║██╔═══╝     ██║     ██╔══██║██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
███████║██║  ██║███████║███████║██║  ██║██║         ╚██████╗██║  ██║██║██║     ██║  ██║███████╗██║  ██║
╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝          ╚═════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

═════════════════════════════════════════════════════════════════════
                    Well Come to caesar chipher Project
═════════════════════════════════════════════════════════════════════
'''
print(logo)


def caesar(Original_Text,shift_amount,encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
                 shift_amount *= -1

    for letter in Original_Text:

        if letter not in alphabet:
            output_text += letter
        else:
             Shifted_Position = alphabet.index(letter) - shift_amount;
             Shifted_Position %= len(alphabet)
             output_text += alphabet[Shifted_Position]
    print(f"Hear is the {encode_or_decode}d result : {output_text}")

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt , type 'decode' to decrpyt : ")
    text = input("Type your message : ").lower()
    shift = int(input("Type  the shift number :  "))

    caesar(Original_Text=text,shift_amount=shift,encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again . Otherwise ,Type 'no' .").lower()

    if restart == "no" :
        should_continue = False
        print("Goodbye")

# Author swapnilmortale@gmail.com