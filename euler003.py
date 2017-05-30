def main():
    n=600851475143
    p=3
    while p<n:
        if n%p==0:
            n=n/p
        else:
            p+=2
        print n