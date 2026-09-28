for n in range(7,1001,2):
    bit_l = (n**2-1).bit_length()-1
    if (n**2-(1<<bit_l))<n*2-1:
        print(n,n**2-1,(1<<bit_l))