print("WORK WITH STRINGS\n")

num_str = 125
str=str(num_str)
print(type(str))


message = 'Hi, my name is Python!' 
mess_1=message.replace('y','0')
mess_1=mess_1.replace('i','1')

print(mess_1)


split_test = 'This is a split test' 
split=split_test.split(' ')
print(split)

join=' '.join(split)
print(join)

print(len(join))