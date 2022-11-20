M,N = map(int,input().split())
if M % 2 == 0 or N % 2 == 0:
    print (round(M * N / 2))
else:
     print(round((M * (N - 1) / 2) + (M - 1) / 2))
