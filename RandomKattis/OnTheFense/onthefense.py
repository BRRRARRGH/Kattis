import math

pCoord = input().split()
px = int(pCoord[0])
py = int(pCoord[1])
qCoord = input().split()
qx = int(qCoord[0])
qy = int(qCoord[1])
distance = int(input())
total = ((px - qx)**2) + ((py - qy)**2)
if(total == distance):
    print("on the fence")
if(total > distance):
    print("against")
if(total < distance):
    print("for")