import time

def output_file(path):
    def decorator_output_file(func):
        def wrapper(*args,**kwargs):
            start_time = time.perf_counter()
            val = func(*args,**kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time
            if val == None:
                val = '-'
            try:
                with open(path , 'w') as file:
                    file.write('\n'.join(list(map(str,[start_time, *args, *kwargs, val, end_time, run_time]))))
            except FileNotFoundError:
                print("No such directory, try again")
            except Exception:
                print("Unknown interrupt")
            return val
        return wrapper
    return decorator_output_file

@output_file(path="D:/PycharmProjects/dino pygame/lap trinh huong doi tuong/task4.txt")

def find_max(*A):
    max = A[0]
    for x in A:
        if x > max:
            max=x
    return max

try:
    A = list(map(int, input().split()))
    print(find_max(*A))
except ValueError:
    print("Invalid type of input")
except Exception:
    print("Unknown interrupt")






