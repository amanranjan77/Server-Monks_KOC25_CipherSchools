count=0
c=0
p=0
for i in range(7,11):
    for j in range(2,i):
        if i %j== 0:
            count=count+1
    if count==0:
        print(i,"is prime")
        count=0
        p=p+1
    else:
        print(i,"is composite")
        count=0
        c=c+1
print("Count:",p,"prime and",c,"composite numbers in the range.")