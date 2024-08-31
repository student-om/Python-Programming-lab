from rom import *
def base_changer(text,output_base):
    
    # Step 1: Remove the '0d' or '0D' prefix
    number_string = text[2:]
    
    # Step 2: Convert the string to a decimal integer without using int()
    decimal_number = 0
    for char in number_string:
        decimal_number = decimal_number * 10 + (ord(char) - ord('0'))
    
    # Step 3: Define characters for bases up to 36 (0-9, a-z)
    characters = '0123456789abcdefghijklmnopqrstuvwxyz'
    
    # Check if the output_base is valid
    if output_base < 2 or output_base > 36:
        return "Output base must be between 2 and 36."
    
    # Special case for base 10 to return the same number (since it's already in decimal)
    if output_base == 10:
        return number_string
    
    # Step 4: Convert decimal to the specified output base
    output_digits = []
    while decimal_number > 0:
        remainder = decimal_number % output_base
        output_digits.append(characters[remainder])
        decimal_number = decimal_number // output_base
    
    # Reverse the output digits to get the correct order
    output_digits.reverse()
    
    # Join the digits to form the final output string
    output_string = ''.join(output_digits)
    
    # Return the result
    return output_string




def base(text, text_base):
    
    text = text.lower()

    
    characters = '0123456789abcdefghijklmnopqrstuvwxyz'

   
    if text_base < 2 or text_base > 36:
        return "Base must be between 2 and 36."

   
    decimal_number = 0

    
    length = len(text)

    
    for i in range(length):
        
        char = text[i]
        if char in characters[:text_base]:
            char_value = characters.index(char)
        else:
            return f"Invalid character '{char}' for base {text_base}."

       
        power = length - i - 1
        decimal_number += char_value * (text_base ** power)

    return decimal_number



def romanToInt(s: str) -> int:
    # Define the Roman numeral values
        roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
    
    
        total = 0
    
    
        for i in range(len(s)):
       
            if i < len(s) - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
           
                total -= roman_values[s[i]]
            else:
           
                total += roman_values[s[i]]
    
        return total


# print(base('1100100', 2))  
# print(base('64', 16))      
# print(base('2s', 36))      


def change_base(text,text_base,output_base):
    if text_base==10:
        if text.startswith('0d') or text.startswith('0D'):
            return base_changer(text,10,output_base)
        else:
            print('please provide proper prefix for given base')
            return

    if text_base=='rom':
        if text.startswith('0r') or text.startswith('0R'):
            k=romanToInt(text[2:])
            return base_changer('0d'+str(k),output_base)
            
        else:
            print('please provide proper prefix for given base')

    if output_base=='rom':
        
        k=base(text,text_base)
        return intToRoman(k)        
        
    if text_base>=2 and text_base<=36:
        p= base(text,text_base)   
        return base_changer('0d'+str(p),output_base) 
    
    
      

# print(change_base('0d100',10,2))            
# print(rom('0b1010',2))
print(change_base('10',16,'rom'))
