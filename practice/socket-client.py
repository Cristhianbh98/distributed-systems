import socket
import sys
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening

HOST = '10.0.0.16'
PORT = 50777  
mBuffer = 1024

print('Conectando con el servidor up on {} port {}'.format(HOST, PORT))

sock.connect((HOST, PORT))

try:
  # Send data
  message = ' '.join(sys.argv[1:]) or 'Hola soy Cristhian Bacusoy, probando conexión.'
  
  print('Enviando {!r}'.format(message))
  sock.sendall(str.encode(message))
  
  # Look for the response
  amount_received = 0
  amount_expected = len(message)
  print("Longitud del mensaje:",amount_expected )
  while amount_received < amount_expected:
    data = sock.recv(mBuffer)
    amount_received += len(data)
    print('received {!r}'.format(data))
    
finally:
  print('closing socket')
  sock.close()