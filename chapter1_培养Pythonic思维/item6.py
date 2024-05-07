# 把数据结构直接拆到多个变量里，不要专门通过下标访问
# unpakcking机制，使得变量的交换不需要中间变量temp来做传递
a =1 
b =2
temp = a
a = b
b = temp
print(a,b)
a, b = b, a # unpacking机制
print(a,b)

# 针对for循环或者类似操作的使用
snacks = [('a', 'apple'), ('b', 'banana')]
for rank, (key,value) in enumerate(snacks, 1): #不需要通过下标逐层访问
    print(f"{rank}. Key: {key}, Value: {value}")

# unpacking是一种特殊的python语法，可以通过一行代码，就能把数据结构里的多个值分别赋给相应的变量