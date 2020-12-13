import hashlib
import socket

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

# 1.3 socket 编程
url = 'www.zhangdongshengtech.com'
port = 80
# 创建TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 链接服务器
sock.connect((url, port))
# 创建请求消息头
request_url = 'GET /article-types/6/ HTTP/1.1\r\nHost: www.zhangdongshengtech.com\r\nConnection:close\r\n\r\n'
print(request_url)
# 发送请求
sock.send(request_url.encode())
response = b''
# 接受返回数据
rec = sock.recv(1024)
while rec:
    response += rec
    rec = sock.recv(1024)

print(response.decode())
print(type(response))
# 使用socket类型试，不论是发送还是接受数据，都需要使用bytes类型数据。


# 2.字符串与bytes类型数据转换
# 将字符串转成bytes类型数据需要使用encode方法，将bytes类型数据转换成字符串，需要使用decode方法，转换方法可以指定编码
string = '爱我中华'
bstr = string.encode(encoding='utf-8')
print(bstr, type(bstr))

string = bstr.decode(encoding='utf-8')
print(string, type(string))


