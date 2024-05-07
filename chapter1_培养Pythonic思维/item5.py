# 用辅助函数取代复杂的表达式
from urllib.parse import parse_qs
my_values = parse_qs('red=S&blue=0&green=',keep_blank_values=True)
print(repr(my_values))