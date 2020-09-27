#codding=utf-8
import socket
import psutil

def do_memory():
    memory_status = psutil.virtual_memory()
    data = 'total=' + str(memory_status.total)
    data = data + ',aviliable:' + str(memory_status.available)
    data = data + ',percent:' + str(memory_status.percent) + '%'
    data = data + ',used:' + str(memory_status.used)
    data = data + ',free:' + str(memory_status.free)
    data = data + ',inactive:' + str(memory_status.inactive)
    data = data + ',buffer:' + str(memory_status.buffers)
    data = data + ',cached:' + str(memory_status.cached)
    data = data + ',shared:' + str(memory_status.shared)
    return data

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#udp
s.bind(('127.0.0.0',8091))
while True:
    (info,addr) = s.recvfrom(1024)
    data = do_memory()
    s.sendto(data.encode('utf-8',addr))


