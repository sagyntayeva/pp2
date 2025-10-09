#task1
n=int(input)
res=1
for i in range(1,n+1):
    res=i*i
print(res, end=" ")
#task2
n=int(input)
for i in range(0, n+1):
    if i%2==0:
        print(i, end=",")
#task3
def div(n):
    for i in range(0,n+1):
        if i%3==0 and i%4==0:
            print(i, end=",")

n=int(input)
div(n)
#task4
def squares(a, b):
    for i in range(a, b + 1):
        print( i ** 2)


a = int(input())
b = int(input())

squares(a,b)
#task5
def down(n):
    for i in range(n,-1,-1):
        print(i,end=",")

n=int(input())
down(n)
#task6
from datetime import date, timedelta
print(date.today(), date.today()-timedelta(5))
#task7
from datetime import date, timedelta
a=date.today()
b=date.today()+timedelta(1)

c=date.today()-timedelta(1)
print(c,a,b)
#task8
from datetime import datetime

a = datetime.now()
b = a.replace(microsecond=0)

print(a,b)
#task9
from datetime import datetime

d1 = input()
d2 = input()


a = datetime.strptime(d1)
b = datetime.strptime(d2)


c = abs((d1 - d2).total_seconds())

print(c)
#task10
import math
n=int(input())
print(math.radians(n))
#task11
h, f, с = map(int, input().split())
s=((f+c)/2)*h
print(s)
#task12
n, l = map(int, input().split())
s=(n*l*l)/(4*math.tan(math.pi/n))
print(s)
#task13
a=int(input())
b=int(input())
s=float(a*b)                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
print(s)
#task14
import json

f = open("list.json")      
data = json.load(f)              
f.close()                        

for a in data["anime"]:         
    print(a["title"], a["genre"], a["rating"])  
