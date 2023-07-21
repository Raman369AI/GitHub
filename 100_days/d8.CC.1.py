import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction,text, shift):
  cipher_text = ""
  plain_text = ""
  for i in range(len(text)):
        if direction=='encode' and text[i] not in alphabet:
            cipher_text=text[i]
        elif direction=='decode' and text[i] not in alphabet:
            plain_text=text[i]
        if text[i] in alphabet:
            position= alphabet.index(text[i])
            if direction=='encode':
              new_position=position+shift
              if new_position<27:
                 new_position=position+shift
              else:
                  new_position=new_position-26
              cipher_text=cipher_text+alphabet[new_position]
            if direction=='decode':
                new_position=position-shift
                plain_text = plain_text+alphabet[new_position]
  if direction=='encode':
      print(cipher_text)
  else:
      print(plain_text) 


print(art.logo)

while True:
    user=input('Do you want to continue\n').lower()
    if user=='no':
      break
    else:
      pass
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    #Hint: Think about how you can use the modulus (%).
    
    caesar(direction,text, shift)
