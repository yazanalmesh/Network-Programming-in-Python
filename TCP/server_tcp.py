import socket

tcp_port = 1672
tcp_ip = 'localhost'
buf_size = 30

print("[INFO] Creating Socket...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[INFO] Socket Successfully created")

s.bind((tcp_ip, tcp_port))
print("[INFO] Binding to port %d" % tcp_port)
s.listen(1)
print("[INFO] Socket is listening")

c, addr = s.accept()
print("[INFO] connection address from", addr)

print("[INFO] Receiving Data from Client...")
data = c.recv(buf_size)

print("[INFO] Decoding received data")
data = data.decode('utf-8')

print("[INFO] Received Data from Client:", data)

msg = data.upper()
print("[INFO] Encoding data...")
msg = msg.encode('utf-8')

print("[INFO] sending data to Client...")
c.send(msg)
print("[INFO] Data sent successfully to Client")

print("[INFO] Disconnecting Client connection...")
c.close()

print("[INFO] Disconnecting Socket...")
s.close()
print("[INFO] Socket disconnected successfully")
