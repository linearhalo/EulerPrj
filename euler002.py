a=0
b=1
even=[]
for i in range (30):
c=a+b
if(c%2==0):
    even.append(c)
a,b=b,c
print even

#어째서인지 코드가 여기까지다.
#기억상... print even 해놓고 그 중에 제일 400만에 가까운 걸 찾아서 입력했던 것 같다.
#그러면 안 된다.