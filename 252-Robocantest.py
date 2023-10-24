def odd(n):
    k = str(n)
    sum = (5 ** (len(k)) - 1) // 4 - 1
    for i in range(len(k)):
        if (k[i] == "0"):
            break;
        
        else:
        
            if (i == (len(k) - 1)):
                sum +=((int(k[i]) + 1)//2)
                break
            if((int(k[i]))% 2 == 0):
                sum += 5 ** (len(k) - i - 1) * (int(k[i]) //  2)
                break
            else:
                sum += 5 ** (len(k) - i - 1) * (int(k[i]) //  2)
            
    return sum;




def check(a):
    k = str(a)
    h = True
    for i in range(len(k)):
        if(int(k[i]) % 2 == 0):
            h = False
            break
    return h
    
    
    
    
    
l = 20
r = 1000000000000000000
j = int(input())
if j < 10: 
    print(2*j)
elif j < 20:
    print(10 + j)  
else:
    while(r>=l):
        m = (l + r) // 2
        s = odd(m)
        if (m - s) == j:
            if(check(m)):
                m -= 1
            print(m)
            break
        elif(m - s) > j:
            r = m
        elif(m - s) < j:
            l = m + 1