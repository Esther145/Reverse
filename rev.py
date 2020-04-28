def reverse(x):
    num=0
    while x>0:
        l=x%10
       
        num=(num*10)+l
        
        x=int(x/10)
       
    return num