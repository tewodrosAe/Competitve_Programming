n,m,a = map(int, input().split())
column = int(n/a)
row = int(m/a)
if n % a != 0:
    column = int(n/a) + 1
if m % a != 0:
    row = int(m/a) + 1
theatre = column * row
print(theatre)
