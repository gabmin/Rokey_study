clovers = ['클로버1', '클로버2', '클로버3']

print(clovers)

del clovers[1]

print(clovers)

clovers.insert(1, '클로버4')

print(clovers)

clovers.extend(['클로버5', '클로버6'])

print(clovers)

subject = ['국어', '수학', '영어', '국사']

subject.insert(2, '사회')
subject.extend(['음악', '체육', '미술'])

print(subject)

week = ['월', '화', '수', '목', '금', '토', '일']

print(week[0:6:-1])