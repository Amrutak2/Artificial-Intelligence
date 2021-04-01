print("Water Jug Problem")
m=int(input("Enter size of jug 1:"))
n=int(input("Enter size of jug 2:"))
d=int(input("Enter the goal state:"))
x=int(input("Enter x:"))
y=int(input("Enter y:"))
while True:
    rno=int(input("Enter the Rule Number:"))
    if rno==1:
        if x<m:
            x=m
    if rno==2:
        if y<n:
            y=n
    if rno==3:
        if x>0:
            x-d, y
    if rno==4:
        if y>0:
            x, y-d
    if rno==5:
        if x>0:
            x=0
    if rno==6:
        if y>0:
            y=0
    if rno==7:
        if x+y<=m+n and  y>0:
            x, y=m, y-(m-x)
    if rno==8:
        if x+y<=m+n and x>0:
            x=n, x-(n-y), y
    if rno==9:
        if x+y<=m and y>0:
            x, y=x+y, 0
    if rno==10:
        if x+y<=n and x>0:
            x, y=0, x+y
    print("x=",x)
    print("y=",y)
    if(x==d):
        print("The result is goal state")
        break        