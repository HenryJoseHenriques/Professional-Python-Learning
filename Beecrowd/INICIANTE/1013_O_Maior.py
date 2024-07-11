#https://judge.beecrowd.com/pt/problems/view/1013

a,b,c = map(int,input().split())

x = (a+b+abs(a-b))/2
y = (x+c+abs(c-x))/2

print(f"{y:.0f} eh o maior")