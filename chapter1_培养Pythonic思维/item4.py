key = "my_var"
value = 1.234
formatted = '%s=%f' % (key, value)
print(formatted)

formatted = f"{key} = {value:.2}"
print(formatted)
