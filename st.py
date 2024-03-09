s=input("enter the string=")
c=0
a=0
for i in s:
    if i == '*':
        c=c+1
    if i == '#':
        a=a+1

if c==a:
    print("*=#, its a valid string")
elif c>a:
    print("number of *>#, string is not vaild")
else:
    print("number of #>*, string is not vaild")