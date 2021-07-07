x=[]

print('How many elements? ',end='')
n=int(input())

for i in range(n):
    print('Enter elements: ',end='')
    x.append(int(input()))

print('The list is: ',x)
big=x[0]
small=x[0]

for i in range(1,n):
    if x[i]>big:
        big=x[i]
    if x[i]<small:
        small=x[i]

print('Maximum is: ',big)
print('Minimum is: ',small)
