answer = []
retu = ['Fizz','Buzz']
for i in range(1,n+1):
    if i % 5 == 0 and i % 3 == 0:
        answer.append(retu[0] + retu[1])
    elif i % 5 == 0:
        answer.append(retu[1])
    elif i % 3 == 0:
        answer.append(retu[0])
    else:
        answer.append(f'{i}')
return answer
