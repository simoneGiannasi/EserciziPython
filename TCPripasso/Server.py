import socket
import threading

# Definisce l'indirizzo IP e la porta del server
server_ip = "127.0.0.1"  # Cambia in "localhost" se necessario
server_port = 12346
buffer_size = 4092
server_address = (server_ip, server_port)

# Crea un socket UDP
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind(server_address) #PER SERVER
tcp_server_socket.listen(1) #DIMENSIONE CODA CONNESSIONI

def main():
    while True:
        conn, address =  tcp_server_socket.accept()
        data = conn.recv(buffer_size)
        print(data.decode())



if __name__ == "__main__":
    main()