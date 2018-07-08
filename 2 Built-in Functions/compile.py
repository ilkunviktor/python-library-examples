c = compile('print("Hello world!")\n', '<string>', 'single')
print(c)

exec(c)