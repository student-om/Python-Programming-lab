#l=1 ->          +
#              + * +
#                -

import math
#print("  "*(middle-i-2) + "* " + "  "*(i+n-1)+ "* ") 

def print_pattern(n):
  q=n*2+3
  count=0
  middle=(q+1)//2

  for i in range(n):
    if i==0:
      print("  "*(middle-1) + "+ ")

    else:
      print("  "*(middle-i-1)+"+ " +  "  "*(i-1)+"  "*i+"+ ") 

  
  for i in range(n):
    if i==0:
      
        print("  "*(middle-n+i-1) + "+ " + "  "*(n-i-1) + "* "+ "  "*(n-i-1)+"+ ")  #len(str(n)) used because for 10 is 2 digit no so spacing would be different(last star of i=0 would not be in its position).

        

    else:
      print("  "*(middle-n+i-1) + "- " + "  "*(n-i-1) + "  "*(n-i)+"- ")   
    
    
  print("  "*(middle-1) + "- ")

    


  

# Input value
n = int(input("Enter a number: "))

# Print the pattern
print_pattern(n)

