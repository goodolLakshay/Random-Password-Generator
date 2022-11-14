import random
n=int(input())
s=""
for i in range(1,n+1):
    a=chr(random.randint(65,90))
    b=chr(random.randint(97,122))
    c=str(int(random.random()*10))
    d=[a,b,c,"#","@","$","&"]
    s+=random.choice(d)
print(s)