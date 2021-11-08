"""Что будет напечатано и почему?"""

""" ответ: 
1. Упарвление будет передано в корутину main;
т.к это задача на параллельное исполнение
--> 2. для  значения i = 2 в цикле for соответственно 
     напечатаются Task {name}: Compute factorial({2})... для какжого функции  factorial с соответственным именем 
     т.е: Task A: Compute factorial(2)...
          Task B: Compute factorial(2)...
          Task C: Compute factorial(2)...
    3. Управление будет передано в корутину sleep;
    4. В течении одной секунды программа "спит"; 
    5. значение f = f*2
    6. Напечатается  Task A: factorial(2) = 2
7/. далее , т.к range(2, number+1), поэтому 
  для  значения i = 3 в цикле for только функции factorial("B", 3) и factorial("C", 4) реализуются аналогично выше
  тогда , напечатаются  Task B: Compute factorial(3)...
                        Task C: Compute factorial(3)...
     7/3. Управление будет передано в корутину sleep;
     7/4. В течении одной секунды программа "спит"; 
     7/5. значение f = f*3
     7/6. Напечатается  Task B: factorial(3) = 6
8/ далее , т.к range(2, number+1), поэтому 
  для  значения i = 4 в цикле for только функции factorial("C", 4) реализуются аналогично выше
  тогда , напечатаются  Task C: Compute factorial(4)...
     7/3. Управление будет передано в корутину sleep;
     7/4. В течении одной секунды программа "спит"; 
     7/5. значение f = f*4
     7/6. Напечатается  Task C: factorial(4) = 24

***в итоге: напечатются: 

Task A: Compute factorial(2)...
Task B: Compute factorial(2)...
Task C: Compute factorial(2)...
Task A: factorial(2) = 2
Task B: Compute factorial(3)...
Task C: Compute factorial(3)...
Task B: factorial(3) = 6
Task C: Compute factorial(4)...
Task C: factorial(4) = 24

"""

import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

async def main():
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

