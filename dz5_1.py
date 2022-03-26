def my_gen(n):
    for i in range(1, n+1, 2):
        yield i



gen_one = my_gen(17)
print(gen_one)
print(type(gen_one))
print(next(gen_one))
print(next(gen_one))
print(next(gen_one))
print(next(gen_one))
print(next(gen_one))
print(next(gen_one))
print(next(gen_one))
print(next(gen_one))
print(next(gen_one))
print(next(gen_one))
print(next(gen_one))