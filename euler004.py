def mm(a):
    v=str(a)
    b=len(v)
    y=0
    z=-1
    for i in range (b/2):#회문은 대칭이니까 계산하는 횟수를 반 나눈다.
        if not v[y]==v[z]:#v값의 맨 첫 자리와 맨 끝 자리가 일치하는지 확인한다.
            return False#위에서 일치하지 않았다면 이미 볼 필요도 없다(단호).
        y+=1#첫 번째 이후에는 두 번째, 세 번째... 순으로 검사한다.
        z-=1#맨 끝 자리 이후에는 끝에서 두 번째, 세 번째...순으로 검사한다.
    return a#그렇게 걸러낸 a를 반환.

large=0
for i in range (100, 1000):
    for j in range (100, 1000):
        a=i*j
        if large<mm(a):#mm함수에서 받은 a 값이 large보다 크면
            large=mm(a)#large에 그 값을 넣는다.(이 값은 조건이 끝날 때까지 교체된다.)
print large