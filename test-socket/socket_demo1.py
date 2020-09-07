#coding = utf-8

"""
1.引入socket模块
2.构建socket对象,IPV4/IPV6,连接方式
3.连接地址，端口
4.发送数据报文报文
try catch抛出异常，接受异常
超时策略，服务端限流
5.关闭连接
生成器改造
迭代器改造
...
"""
import socket
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(time.time())
s.connect(('www.czur.com',80))
s.send(b'GET/HTTP/1.1\:\nhost:www/czur.com\r\nConnection:close\r\n\r\n')

buffer = []

while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
s.close()

data = b''.join(buffer)
header,html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('/home/oubingkun/桌面/1train.html','wb')as f:
    f.write(html)
