import re

one = 'abc 123'
patter = re.compile('\d+')
# match 从头匹配 匹配一次

result = patter.match(one)

# search 从任意位置 , 匹配一次
result = patter.search(one)

# findall  查找符合正则的 内容 -- list
result = patter.findall(one)

# sub  替换字符串
result = patter.sub('#',one)

# split  拆分
patter = re.compile(' ')
result = patter.split(one)



print(result)
