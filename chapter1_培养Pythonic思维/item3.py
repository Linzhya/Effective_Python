a = b'h\x65llo'
print(list(a))
print(a)

a = 'a\u0300 propos'
print(list(a))
print(a)
      


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

with open('data.bin', 'wb') as f:
    f.write(b'\xf1\xf2\xf3')
with open('data.bin', 'rb') as f:
    data = f.read()
    print(data)