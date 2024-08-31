
def intToRoman(num: int) -> str:
          
    val = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    
    roman_numeral = ''

   
    for (i, numeral) in val:
        
        while num >= i:
           
            roman_numeral += numeral
         
            num -= i

    return roman_numeral

def number_reverser(num):
    res=0
    while num>0:
        res=res*10+num%10
        num//=10
    return res    


def rom(num_str,base):
    if base==10:
        return intToRoman(num_str,base)
    if base==8:
        if num_str.startswith('0o') or num_str.startswith('0O'):
            integer_value = 0
    
    
            
            num_str=num_str[2:]
            length = len(num_str)
  
            for i in range(length):
        
                digit = int(num_str[length - 1 - i])
        
     
                integer_value += digit * (8 ** i)
    
            return intToRoman(integer_value)
        else:
            print('please prover proper prefix for given base')        

    
    elif base==2:
        
        if num_str.startswith('0b') or num_str.startswith('0B'):
            integer_value = 0
    
 
            
            num_str=num_str[2:]
            length = len(num_str)
   
            for i in range(length):
       
                digit = int(num_str[length - 1 - i])
        
      
                integer_value += digit * (2 ** i)
    
            return intToRoman(integer_value)
        else:
            print('please prover proper prefix for given base')


    elif base==16:
        
        if num_str.startswith('0x') or num_str.startswith('0X'):
            integer_value = 0
    
  
            
            num_str=num_str[2:]
            length = len(num_str)
            for i in range(length):
        
                char = num_str[length - 1 - i]
        
        
                if '0' <= char <= '9': 
                    digit = int(char)
                elif 'A' <= char <= 'F': 
                    digit = 10 + (ord(char) - ord('A'))
                elif 'a' <= char <= 'f':  
                    digit = 10 + (ord(char) - ord('a'))
                else:
                    print("Invalid hexadecimal digit")
        
      
        integer_value += digit * (16 ** i)
    
    return intToRoman(integer_value)   

            
                  





