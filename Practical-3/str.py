def count(string,substring,overlap):
    start=0
    count=0
    sub_string_len=len(substring)
    while True:
      
      if string.find(substring,start)==-1:
         break

    
      if overlap==False:
        start=string.find(substring,start)
        start+=sub_string_len
        count+=1

      else:
        start=string.find(substring,start)
        start+=1
        count+=1

    return count

a="sggs"
print(count(a,"z",False))  

        
