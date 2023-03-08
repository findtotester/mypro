f = open(r'C:\\Users\\limm.JINHER\\Desktop\\脚本\\内蒙古风控.txt', mode='r', encoding='utf-8-sig')
next(f)
list = []
lines = f.readlines()  # 以行的形式进行读取文件
f.close()
for line in lines:
    line = line.strip('\n')
    line = line.split(',')
    list.append(line[0])
    # print(list)

print(list, len(list))

for i in range(len(list)):
    print(list[i])






