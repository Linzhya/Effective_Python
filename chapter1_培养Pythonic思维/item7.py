# 尽量用enumerate取代range
flavor_list = [1,2,3]
for i, flavor in enumerate(flavor_list):
    print(f"{i+1} {flavor}")
# 不要通过range指定下标的取值范围，然后用下标去访问序列，而是应该直接用enumrate函数迭代
# 可以通过enumerate的第二个参数指定起始序号（默认为0）