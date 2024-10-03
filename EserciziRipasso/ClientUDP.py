import socket

# Definisce l'indirizzo IP e la porta del server a cui connettersi
server_ip = "192.168.141.150"
server_port = 12345
server_address = (server_ip, server_port)
buffer_size = 1024


# Crea un socket UDP
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# Messaggio da inviare al server
message = "Ciao server, questo è un messaggio UDP!".encode()

for i in range(0,10):
    try:
        udp_client_socket.sendto(message, server_address)
        data, address = udp_client_socket.recvfrom(buffer_size)
        print(f"Risposta dal server: {data.decode()}")

    except:
        print("Errore")


udp_client_socket.close()
