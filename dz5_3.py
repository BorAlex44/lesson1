from itertools import zip_longest
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Саша', 'Маша']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

if len(tutors) >= len(klasses):
    gen = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses))
else:
    gen = ((tutor, klass) for tutor, klass in zip(tutors, klasses))

print(gen)
#print(*gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))