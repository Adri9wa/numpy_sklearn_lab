from labwork4 import task_a, task_b, task_c, task_d, task2, task3


divider = '\n-------------------------------------------------\n'

a = task_a()
print(a)
print(divider)

a_inserted = task_b(a)
print(a_inserted)
print(divider)

print(task_c(a_inserted))
print(divider)

print(task_d(a))
print(divider)

task2()

task3()
