a=[]
c=0
n=int(input("Enter array length:"))
print("Enter numbers in new line: ") 
for i in range(n):
    x=int(input())
    a.append(x)
for i in a:
    if i%2 ==0:
        c+=1
print("No.of even elements: ",c)        
