# 用赋值表达式减少重复代码
# 使用海象表达式,注意只能使用在while/if条件中
if (count := True) != False:
    print(count)
# 遇到多层嵌套的结构，可以思考一下是否可以用海象表达式来改写
bottles = []
fruits = [{'A': 3, 'B': 5}, {'C': 2, 'D': 4}]
def get_fruit(fruit):
    if fruit != []:
        count = fruit[-1]
        fruit.pop()
        return count
    else:
        return False

while fresh_fruit := get_fruit(fruits):
    for fruit, count in fresh_fruit.items():
        bottles.append((fruit, count))
print(bottles)
