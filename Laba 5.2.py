n = int(input("n = "))

factorial=1

for i in range(1,n+1):
    factorial *=i

res = 1/factorial

print(res)