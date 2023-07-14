def binDec(n):
    bin = str(n)
    l = len(bin)
    dec = 0
    for i in range(l):
        if bin[i] != '0':
            dec = 2**(l-i-1) + dec 
    return dec

def octDec(n):
    oct = str(n)
    l = len(oct)
    dec = 0
    for i in range(l):
        if oct[i] != '0':
            dec += 8**(l-i-1) * int(oct[i]) 
    return decHex(dec)

def decHex(n):
    hexa = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    hex_n = " "

    while n > 0:
        rem = n%16
        hex_n = hexa[rem]+hex_n
        n = n//16
    
    print("Hexadecimal value = ",hex_n)

def main():
    ch = int(input("Enter 1:for bin to dec 2:for oct to hex "))
    n = int(input("Enter the number "))

    if ch == 1:
        print(binDec(n))
    elif ch ==2:
        octDec(n)

main()