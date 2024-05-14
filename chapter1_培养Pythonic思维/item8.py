# 用zip函数同时遍历两个迭代器
import itertools
names = ["A", "B", "C"]
ages = [23, 45, 67]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# 如果两个列表长度不一致，建议使用zip_longest
# fillvalue用来填补空缺的值，默认为None
names = ["A", "B", "C", "D"]
ages = [23, 45, 67, 5, 3]
for name, age in itertools.zip_longest(names, ages, fillvalue="Unknown"):
    print(f"{name} is {age} years old")
