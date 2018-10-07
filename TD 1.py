

#Problème 16

#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#ameli.aussel@univ-lorraine
#What is the sum of the digits of the number 2**1000?

def solve16(n):
    S = 0
    for i in str(2**n):
        S += int(i)
    return S

assert solve16(1000) == 1366
print(solve16(1000))

#pb 22
def solve22():
    f = open("p022_names.txt", "r")
    alphabet=list('"ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    fnew=sorted(f.read().split(",")) #split est une methode pour str
    print(fnew)
    S=0
    for i in fnew:
        for j in i:
            sum=0
            sum+=alphabet.index(str(j))
            S+=sum*(fnew.index(i)+1)

    return S

assert solve22() ==871198282
print(solve22())
   
    
#Problème 55(composé avec 2 fonctions auxiliares
    
def construit_palindrome(a):  #a est un int
    return int("".join(list(str(a))[::-1]))


def palindrome_boolean(a): #b est un int et la fct renvoie true si palindrome il y a
    b=list(str(a))
    if len(b)%2==0:
    	return b[:len(b)//2]== b[len(b)//2:][::-1]
    else:
    	return b[:len(b)//2]== b[len(b)//2+1:][::-1]
        

def solve55(n):
    lychrelNumber=0
    for i in range(n):
        k=1
        h =construit_palindrome(i)
        while not palindrome_boolean(h) :
            h=construit_palindrome(h)+h
            k+=1
            if k==51:
                lychrelNumber+=1
                break
            
    return lychrelNumber

#assert solve55()==?
print(solve55(10000))
            
    

        
