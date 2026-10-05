
email = str
x ="ABabcd@123"
def valida_email(a:str):
    return a.endswith('@puc.com')

def valida_senha(b):
    s8 = len(b) >=8
    sMa = b.islower()
    sMi = b.isupper()
    sNum = b.isalpha()
    print(s8)
    print(sMa)
    print(sMi)
    print(sNum)
    if s8 == True and sNum == False and sMa == False and sMi == False:
        return True

def criptografa(j):
    ns=""
    for i in j:
        if ord(i)>=97:
            sI=ord(i)-ord('a')
            sInter=(sI+3)%26+ord('a')
            sF=chr(sInter)
            ns += sF
        elif ord(i)<97:
            sI=ord(i)-ord('A')
            sInter=(sI+3)%26+ord('A')
            sF=chr(sInter)
            ns += sF
    return ns

print(criptografa(x))