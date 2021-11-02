s = int(input())
sh = 5
ot = 0
for i in range(1, 6):
    ot += s // sh
    s = s%sh
    sh -= 1
print(ot)
    
    
