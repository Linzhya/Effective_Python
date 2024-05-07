# 用支持差值的f-string取代C风格的格式字符串与str.format()
在Python 3.6中，你可以使用f-strings来代替C风格的格式字符串。f-strings是一种新的字符串格式化方式，它允许你直接在字符串中嵌入变量，并使用f前缀来标识它。
# 内置的format函数与str类的format方法
可以在{}里面写个冒号，然后把格式说明符写在冒号的右边，用以规定format方法所接受的这个值应该按怎么样的格式来调整。
```
formatted = '{:02d}'.format(number)
```

```
formatted = '{0:.2f}'.format(number)
```
# 插值格式字符串
```
key = 'my_var'
value = 1.234
formatted = f"{key} = {value}"