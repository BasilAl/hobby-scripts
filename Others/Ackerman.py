def ackermann(m,n):
    """computes the value of the Ackermann function for the input integers m and n.
       the Ackermann function being:
       A(m,n)=n+1               if m=0
             =A(m-1,1)          if m>0 and n=1
             =A(m-1,A(m,n-1)    if m>0 and n>0"""
    if m==0:
        print (n+1)
        return n+1
    elif m>0 and n==0:
        print ("ackermann(",m-1,",",1,")")                                          #just 2 chk intrmdt val. and no. of steps invlvd.can be dltd if necessary
        return ackermann(m-1,1)
    elif m>0 and n>0:
        print ("Ackermann(",m-1,",","Ackermann(",m,",",n-1,")",")")                  #just 2 chk intrmdt val. and no. of steps invlvd.can be dltd if necessary
        return ackermann(m-1,ackermann(m,n-1)) 


ackermann(4,2)
