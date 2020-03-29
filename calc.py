def fractional(n):
    try:
         n=int(n)
    except:
        return "-->Error"

    if n==0:
        return 1

    ans=n
    while n>1:        
         ans=ans*(n-1)
         n-=1
    ans=str(ans)
    lenght=len(ans)
    if lenght>45:
        return "-->Answer will not fit on the screen!"
    else:
        return ans

def roman(n):
    try:
        n=int(n)
    except:
        return "-->Error"

    if n>1999999:         
        return "-->out of range"

    numberBreaks=(1000000,900000,500000,400000,100000,90000,50000,40000,10000,9000,5000,1000,900,500,400,100,90,50,40,10,9,5,4,1)
    letters={1000000:'M_ ',900000:'CM_ ',500000:'D_ ',400000:'CD_ ',100000:'C_ ',90000:'XC_ ',50000:'L_ ',40000:'XL_ ',10000:'X_ ',9000:'IX_ ',5000:'V_ ',1000:'M ',900:'CM ',500:'D ',400:'CD ',100:'C ',90:'XC ',50:'L ',40:'XL ',10:'X ',9:'IX ',5:'V ',4:'IV ',1:'I '}
    result=""
    for value in numberBreaks:
        while n >= value:
            result=result+letters[value]
            n-=value
    result=str(result)
    lenght=len(result)
    if lenght>45:
        return "-->Answer will not fit on the screen!"
    else:
        return result

def kwadrat(n):
     try:
         n=int(n)
     except:
         return "-->Error"
     ans=n
     ans1=1
     while ans1<n:
         ans*=n
         ans1+=1
     ans=str(ans)
     lenght=len(ans)
     if lenght>45:
         return "-->Answer will not fit on the screen!"
     else:
         return ans

def kwadrat2(n):
     try:
         n=int(n)
     except:
         return "-->Error"
     ans=n
     ans1=1
     while ans1<n:
         ans*=n
         ans1+=1
     ans=1/ans
     ans=str(ans)
     lenght=len(ans)
     if lenght>45:
         return "-->Answer will not fit on the screen!"
     else:
         return ans

def binary(n):
    try:
        n=int(n)
        return bin(n)[2:]
    except:
        return "-->Error"

def basic(n):
    try:
        return int(n,2)
    except:
        return "-->Error"

import math
def sqrt(ans):
    try:
        ans=int(ans)
    except:
        return "-->Error"
    ans=float(ans)
    ans=math.sqrt(ans)
    ans=str(ans)
    lenght=len(ans)
    if lenght>45:
        return "-->Answer will not fit on the screen!"
    else:
        return ans

def tan(ans):
    try:
        ans=int(ans)
    except:
        return "-->Error"
    ans=float(ans)
    ans=math.tan(ans)
    ans=str(ans)
    lenght=len(ans)
    if lenght>45:
        return "-->Answer will not fit on the screen!"
    else:
        return ans

def sin(ans):
    try:
        ans=int(ans)
    except:
        return "-->Error"
    ans=float(ans)
    ans=math.sin(ans)
    ans=str(ans)
    lenght=len(ans)
    if lenght>45:
        return "-->Answer will not fit on the screen!"
    else:
        return ans

def cos(ans):
    try:
        ans=int(ans)
    except:
        return "-->Error"
    ans=float(ans)
    ans=math.cos(ans)
    ans=str(ans)
    lenght=len(ans)
    if lenght>45:
        return "-->Answer will not fit on the screen!"
    else:
        return ans

    
    
