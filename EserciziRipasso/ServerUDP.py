import socket

# Definisce l'indirizzo IP e la porta del server
server_ip = "192.168.141.164"
server_port = 12345
buffer_size = 1024
server_address = (server_ip, server_port)



# Crea un socket UDP
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #SOCK_DGRAM = socket UDP
# Associa l'indirizzo e la porta al socket
udp_server_socket.bind(server_address)


for i in range(0,10):
    print(f"Server in ascolto su {server_ip}:{server_port}...")
    data, client_address = udp_server_socket.recvfrom(buffer_size) #bloccante
    print(f"Messaggio ricevuto: {data.decode()} da {client_address}")
    response = "Messaggio ricevuto"
    udp_server_socket.sendto(response.encode(), client_address)


udp_server_socket.close() #chiude la trasmissione (devo togliere il while true)











