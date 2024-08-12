#note:python does not have a switch case
def change_case(string,style):
    if style in ['c','C']:      
        print(capital_case(string))
    elif style in ['s','S']: 
        print(small_case(string))
    elif style in ['r','R']: 
        print(reverse_case(string))
    elif style in ['u','U']: 
        print(alternate_case(string))
    else:
        print("Please Provide a Valid style")    

def is_small(a):
    if (ord(a)>=97 and ord(a)<=122):
        return True
    
def is_capital(a):
    if(ord(a)>=65 and ord(a)<=90):
        return True    

def capital_case(string):
    s=""
    for i in string:
        if(is_small(i)==True):
            s+=chr(ord(i)-32)
        else:
            s+=i
    return s    
        

def small_case(string):
    s=""
    for i in string:
        if(is_capital(i)==True):
            s+=chr(ord(i)+32)
        else:
            s+=i
    return s

def reverse_case(string):
    s=""
    for i in string:
        if(is_small(i)==True):
            s+=chr(ord(i)-32)
        elif(is_capital(i)==True):
            s+=chr(ord(i)+32)
        else:
            s+=i
    return s


def convert_to_capital(a):
    if(is_small(a)):
        return chr(ord(a)-32)
    else:
        return a

def convert_to_small(a):
    if(is_capital(a)):
        return chr(ord(a)+32)
    else:
        return a

#dir(enumerate) -> conatins (__next__) method which will invoke automatically when used in for loop 
#enumerate(string) -> will return a tuple with (index,character)
#symbols can be ignnored 
def alternate_case(string):
    s=""
    if (is_capital(string[0])==True):
        for index,character in enumerate(string):
            if(index%2==0):
                s+=convert_to_capital(character)
            else:
                s+=convert_to_small(character)    

    else:
        for index,character in enumerate(string):
            if(index%2==0):
                s+=convert_to_small(character)     

            else:
                s+=convert_to_capital(character)           

    return s      
change_case("Abcd",'u')