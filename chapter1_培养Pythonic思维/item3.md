# 了解bytes和str的区别
- bytes 是字节序列，用于表示二进制数据。
- str 是字符串，用于表示文本数据。Unicode
- bytes 中的每个元素是单个字节的值，范围从 0 到 255。
- str 中的每个元素是 Unicode 字符的编码，通常是一个多字节序列。
- bytes 可以由 str 解码得到，但 str 不一定可以由 bytes 解码得到。
- bytes 主要用于处理二进制数据，如网络通信、文件操作等。
- str 主要用于处理文本数据，如显示在屏幕上、保存到文件中等。

```
a = b'h\x65llo'
print(list(a))
print(a)

a = 'a\u0300 propos'
print(list(a))
print(a)
```
#### 把二进制数据转换成Unicode数据，必须调用bytes的decode方法，把Unicode数据转换成二进制数据，必须调用str的encode方法。调用这些方式时，可以明确指定编码格式，也可以使用默认的编码格式。

+操作符可以用于连接字符串或者字节序列

```
print(b'hello' + b' world')
print('hello' + ' world')

print(b'hello' + ' world') # This is wrong
print(b'hello' + ' world'.encode('utf-8')) # This is right
```
==, >的操作特性和+操作符类似

### 从文件中读取二进制数据（或者把二进制数据写入文件）时，应该用'rb'（'wb'）这样的二进制模式打开文件

```
with open('data.bin', 'wb') as f:
    f.write(b'\x00\x01\x02')
with open('data.bin', 'rb') as f:
    data = f.read()
    print(data)
```

### 如果要从文件中读取（或者要写入文件之中）的是Unicode数据，那么必须注意系统默认的编码格式，在打开文件时，应该明确指定'r'（'w'）模式打开文件，或者在调用open函数时，明确指定'encoding'参数的值。
```
执行一下命令查看默认编码方式
python3 -c 'import locale; print(locale.getpreferredencoding())'
``` 