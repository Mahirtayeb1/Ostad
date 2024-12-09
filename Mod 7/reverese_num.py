n = int(input())
g = ''
while(n!=0):
    g+=str(n%10) 
    n//=10
print(int(g))