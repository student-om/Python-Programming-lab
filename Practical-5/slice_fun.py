#and b[1]+len(a)>0
def checker(a,b):
    s=''
    if b[0]>=0 and b[1]<0:
        if b[0]>=0 and b[0]<len(a) and b[1]+len(a)>0:
            for i in range(b[0],b[1]+len(a)):
                s+=a[i]
            return s   
        else:
            return s
    if b[0]>=0 and b[1]>0:
        if b[0]>=0 and b[0]<len(a) and b[1]>=0 and b[1]<=len(a):
            for i in range(b[0],b[1]):
                s+=a[i]
                return s   
        else:
            return s 
    if b[0]<0 and b[1]>0:
        if b[0]+len(a)>0 and b[1]>=0 and b[1]<=len(a):
            for i in range(b[0]+len(a),b[1]):
                s+=a[i]
            return s   
        else:
            return s  
    if b[0]<0 and b[1]<0:
        if b[0]+len(a)>0 and b[1]+len(a)>0 and b[0]<b[1]:
            for i in range(b[0]+len(a),b[1]+len(a)):
                s+=a[i]
            return s   
        else:
            return s     
    
def slice(a,b):
    
    if type(a)==str:
        s=''
        if len(b)==0:
            for i in a:
                s+=i 
        if len(b)==1:
            if b[0] > 0:
                if b[0]>=0 and b[0]<len(a):
                    for i in range(b[0],len(a)):
                        s+=a[i]
                    return s    
                else:
                    print('IndexError')        

            else:
                if b[0]+len(a)>0:
                    for i in range(b[0]+len(a),len(a)):
                        s+=a[i]
                    return s         
                else:
                    print('IndexError')           

        if len(b)==2:
            return checker(a,b)

        if len(b)==3:
            if b[2]==0:
                print('slice step cannot be zero')

            if b[2]>0:
                
                if b[0]>=0 and b[1]<0:
                    if b[0]>=0 and b[0]<len(a) and b[1]+len(a)>0:
                        for i in range(b[0],b[1]+len(a),b[2]):
                            s+=a[i]
                        return s   
                    else:
                        return s
                if b[0]>=0 and b[1]>0:
                    if b[0]>=0 and b[0]<len(a) and b[1]>=0 and b[1]<=len(a):
                        for i in range(b[0],b[1],b[2]):
                            s+=a[i]
                        return s   
                    else:
                        return s 
                if b[0]<0 and b[1]>=0:
                    if b[0]+len(a)>0 and b[1]>=0 and b[1]<=len(a):
                        for i in range(b[0]+len(a),b[1],b[2]):
                            s+=a[i]
                        return s   
                    else:
                        return s  
                if b[0]<0 and b[1]<0:
                    if b[0]+len(a)>0 and b[1]+len(a)>0 and b[0]<b[1]:
                        for i in range(b[0]+len(a),b[1]+len(a),b[2]):
                            s+=a[i]
                        return s   
                    else:
                        return s 
        if b[2]<0:
            if b[0]>=0 and b[1]<0:
                    for i in range(b[0],b[1]+len(a),b[2]):
                        s+=a[i]
                    return s   
            
           
            if b[0]>=0 and b[1]>=0:
                for i in range(b[0],b[1],b[2]):
                    s+=a[i]
                return s   
               
               
            if b[0]<0 and b[1]>=0:
                for i in range(b[0]+len(a),b[1],b[2]):
                    s+=a[i]
                return s   
              
            if b[0]<0 and b[1]<0:

                for i in range(b[0],b[1],b[2]):
                    if i+len(a)>=0:
                        s+=a[i]
                return s

    if type(a)==list:
        s=[]
        if len(b)==0:
            for i in a:
                s+=[i] 
        if len(b)==1:
            if b[0] > 0:
                if b[0]>=0 and b[0]<len(a):
                    for i in range(b[0],len(a)):
                        s+=[a[i]]
                    return s    
                else:
                    print('IndexError')        

            else:
                if b[0]+len(a)>0:
                    for i in range(b[0]+len(a),len(a)):
                        s+=[a[i]]
                    return s         
                else:
                    print('IndexError')           

        if len(b)==2:
            return checker(a,b)

        if len(b)==3:
            if b[2]==0:
                print('slice step cannot be zero')

            if b[2]>0:
                
                if b[0]>=0 and b[1]<0:
                    if b[0]>=0 and b[0]<len(a) and b[1]+len(a)>0:
                        for i in range(b[0],b[1]+len(a),b[2]):
                            s+=[a[i]]
                        return s   
                    else:
                        return s
                if b[0]>=0 and b[1]>=0:
                    if b[0]>=0 and b[0]<len(a) and b[1]>=0 and b[1]<=len(a):
                        for i in range(b[0],b[1],b[2]):
                            s+=[a[i]]
                        return s   
                    else:
                        return s 
                if b[0]<0 and b[1]>=0:
                    if b[0]+len(a)>0 and b[1]>=0 and b[1]<=len(a):
                        for i in range(b[0]+len(a),b[1],b[2]):
                            s+=[a[i]]
                        return s   
                    else:
                        return s  
                if b[0]<0 and b[1]<0:
                    if b[0]+len(a)>0 and b[1]+len(a)>0 and b[0]<b[1]:
                        for i in range(b[0]+len(a),b[1]+len(a),b[2]):
                            s+=[a[i]]
                        return s   
                    else:
                        return s 
            if b[2]<0:
                if b[0]>=0 and b[1]<0:
                    for i in range(b[0],b[1]+len(a),b[2]):
                        s+=[a[i]]
                    return s   
            
           
            if b[0]>=0 and b[1]>=0:
                for i in range(b[0],b[1],b[2]):
                    s+=[a[i]]
                return s   
               
               
            if b[0]<0 and b[1]>=0:
                for i in range(b[0]+len(a),b[1],b[2]):
                    s+=[a[i]]
                return s   
              
            if b[0]<0 and b[1]<0:

                for i in range(b[0],b[1],b[2]):
                    if i+len(a)>=0:
                        s+=[a[i]]
                return s

    if type(a)==tuple:
        s=()
        if len(b)==0:
            for i in a:
                s+=tuple([i]) 
        if len(b)==1:
            if b[0] > 0:
                if b[0]>=0 and b[0]<len(a):
                    for i in range(b[0],len(a)):
                        s+=tuple([a[i]])
                    return s    
                else:
                    print('IndexError')        

            else:
                if b[0]+len(a)>0:
                    for i in range(b[0]+len(a),len(a)):
                        s+=tuple([a[i]])
                    return s         
                else:
                    print('IndexError')           

        if len(b)==2:
            return checker(a,b)

        if len(b)==3:
            if b[2]==0:
                print('slice step cannot be zero')

            if b[2]>0:
                
                if b[0]>=0 and b[1]<0:
                    if b[0]>=0 and b[0]<len(a) and b[1]+len(a)>0:
                        for i in range(b[0],b[1]+len(a),b[2]):
                            s+=tuple([a[i]])
                        return s   
                    else:
                        return s
                if b[0]>=0 and b[1]>=0:
                    if b[0]>=0 and b[0]<len(a) and b[1]>=0 and b[1]<=len(a):
                        for i in range(b[0],b[1],b[2]):
                            s+=tuple([a[i]])
                        return s   
                    else:
                        return s 
                if b[0]<0 and b[1]>=0:
                    if b[0]+len(a)>0 and b[1]>=0 and b[1]<=len(a):
                        for i in range(b[0]+len(a),b[1],b[2]):
                            s+=tuple([a[i]])
                        return s   
                    else:
                        return s  
                if b[0]<0 and b[1]<0:
                    if b[0]+len(a)>0 and b[1]+len(a)>0 and b[0]<b[1]:
                        for i in range(b[0]+len(a),b[1]+len(a),b[2]):
                            s+=tuple([a[i]])
                        return s   
                    else:
                        return s 
            if b[2]<0:
                if b[0]>=0 and b[1]<0:
                    for i in range(b[0],b[1]+len(a),b[2]):
                        s+=tuple([a[i]])
                    return s   
            
           
            if b[0]>=0 and b[1]>=0:
                for i in range(b[0],b[1],b[2]):
                    s+=tuple([a[i]])
                return s   
               
               
            if b[0]<0 and b[1]>=0:
                for i in range(b[0]+len(a),b[1],b[2]):
                    s+=tuple([a[i]])
                return s   
              
            if b[0]<0 and b[1]<0:

                for i in range(b[0],b[1],b[2]):
                    if i+len(a)>=0:
                        s+=tuple([a[i]])
                return s                           
               




 
print(slice([1,2,3,4,5],[-1,-4,-1] ))         