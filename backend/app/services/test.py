import socket

# 定义源 IP 和端口
src_ip = "192.168.169.2"
src_port = 50656

# 定义目标 IP 和端口
dst_ip = "192.168.169.1"
dst_port = 8800

# 数据部分（从 Wireshark 数据包提取）
data = bytes.fromhex(
    "ef0258000202000100000000d5000000140066148080b38000020000000000000000000031990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000"
)
data2 = bytes.fromhex("ef0258000202000100000000d7000000140066148080ff800002000000000000000000007d990000000000000000000000000000000000000000000000000000000000000000000000000000000000000000324b142d0000")

# 创建原始套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定到源地址（可选）
sock.bind((src_ip, src_port))

# 发送 UDP 数据包
sock.sendto(data, (dst_ip, dst_port))
sock.sendto(data2, (dst_ip, dst_port))

print(f"数据包已发送到 {dst_ip}:{dst_port}")

# 关闭套接字
sock.close()