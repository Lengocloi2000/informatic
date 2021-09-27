def decorator_swap(func):
    def wrapper(*args,**kwargs):
            new_args = []
            for i in range(len(args)):
                new_args.append(args[len(args)-1-i])
            return func(*new_args,**kwargs )
    return wrapper

@decorator_swap
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res

div(2, 4, show=True)

