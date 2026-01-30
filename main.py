from logo import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter in alphabet:
           shifted_position = alphabet.index(letter) + shift_amount
           shifted_position %= len(alphabet)
           output_text += alphabet[shifted_position]
        elif letter not in alphabet:
            output_text += letter
    return output_text

if __name__ == "__main__":
   should_continue = True
   while should_continue:

      direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
      text = input("Type your message:\n").lower()
      shift = int(input("Type the shift number:\n"))
      caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

      stop = input("Do you wish to continue - Type yes or no?: ").lower()
      if stop == "no":
         should_continue = False