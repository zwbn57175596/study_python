import hashlib

# 1.1 计算 md5
string = '123456'

m = hashlib.md5()       # 创建md5对象
str_bytes = string.encode(encoding='utf-8')
print(type(str_bytes))
m.update(str_bytes)     # update 方法只接受bytes类型数据作为参数
str_md5 = m.hexdigest() # 得到散列后的字符串

print('MD5散列前：' + string)
print('MD5三列后：' + str_md5)

# 1.2 二进制读写文件
f = open('data', 'wb')
text = '二进制写文件'
text_bytes = text.encode('utf-8')
f.write(text_bytes)
f.close()

f = open('data', 'rb')
data = f.read()
print(data, type(data))
str_data = data.decode('utf-8')
print(str_data)
f.close()


