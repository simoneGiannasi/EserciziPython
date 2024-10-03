import socket
import threading

# Definisce l'indirizzo IP e la porta del server a cui connettersi
server_ip = "127.0.0.1"  # Cambia in "localhost" se necessario
server_port = 12346
server_address = (server_ip, server_port)
buffer_size = 4092

# Crea un socket UDP
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client_socket.connect(server_address) #PER CLIENT



def main(): 
    print("1 - forward\n2 - backward\n3 - right\n4 - left\nvelocita - 0/100\nUSAGE: movimento, velocita")
    while True:
        input_utente = input("")
        tcp_client_socket.send(input_utente.encode("utf-8"))









if __name__ == "__main__":
    main()