#note:python does not have a switch case
def change_case(string,style):
    if(style=='c' or style=='C'):      
        print(capital_case(string))
    elif style=='s' or style=='S':
        print(small_case(string))
    elif style=='r' or style=='R':
        print(reverse_case(string))
    elif style=='u' or style=='U':
        print(alternate_case(string))
    else:
        print("Please Provide a Valid style")    


def capital_case(string):
    length_of_string=len(string)
    s=""
    for i in range(len(string)):
        if(string[i]>=chr(65) and string[i]<=chr(90)):
            s+=string[i]

        elif(string[i]>=chr(97) and string[i]<=chr(122)):
            temp=chr(ord(string[i])-32)
            s+=temp

        else:
            s+=string[i]
        

    return s    
        

def small_case(string):
    length_of_string=len(string)
    s=""
    for i in range(len(string)):
        if(string[i]>=chr(97) and string[i]<=chr(122)):
            s+=string[i]

        elif(string[i]>=chr(65) and string[i]<=chr(90)):
            temp=chr(ord(string[i])+32)
            s+=temp

        else:
            s+=string[i]

    return s


def reverse_case(string):
    length_of_string=len(string)
    s=""
    for i in range(len(string)):
        if(string[i]>=chr(97) and string[i]<=chr(122)):
            temp=chr(ord(string[i])-32)
            s+=temp

        elif(string[i]>=chr(65) and string[i]<=chr(90)):
            temp=chr(ord(string[i])+32)
            s+=temp

        else:
            s+=string[i]
    return s


def is_small(a):
    if (ord(a)>=97 and ord(a)<=122):
        return True


#case can be ignnored
def alternate_case(string):
    s=""
    if(string[0]>=chr(97) and string[0]<=chr(122)):
        for i in range(len(string)):
            if(i%2==0):
                if(is_small(string[i])==True):
                    s+=string[i]
                else:
                    temp=chr(ord(string[i])+32)
                    s+=temp

            else:
                if(is_small(string[i])==True):
                    temp=chr(ord(string[i])-32)
                    s+=temp
                else:
                    s+=string[i]

    elif(string[0]>=chr(65) and string[0]<=chr(90)):
        for i in range(len(string)):
            if(i%2==0):
                if(is_small(string[i])==True):
                    temp=chr(ord(string[i])-32)
                    s+=temp
                else:
                    s+=string[i]

            else:
                if(is_small(string[i])==True):
                    s+=string[i]
                else:
                    temp=chr(ord(string[i])+32)
                    s+=temp 

    else:
        s+=string[i]                       
    return s      

    
  


change_case("Abcd",'u')