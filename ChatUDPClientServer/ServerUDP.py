import socket
import threading

# Definisce l'indirizzo IP e la porta del server
server_ip = "127.0.0.1"  # Cambia in "localhost" se necessario
server_port = 12346
buffer_size = 4092
server_address = (server_ip, server_port)

# Crea un socket UDP
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Associa l'indirizzo e la porta al socket
udp_server_socket.bind(server_address)

client_address = None

# Funzione che aspetta la ricezione del messaggio dal client
def riceviMessaggi():
    global client_address
    while True:
        try:
            data, client_address = udp_server_socket.recvfrom(buffer_size)  # Bloccante
            print(f"Client: {data.decode()}")
            print("Server: ")
        except Exception as e:
            print(f"Errore1: {e}")

# Funzione che invia i messaggi 
def inviaMessaggi():
    while True:
        try:
            if client_address:
                messaggio = input("Server: ")
                udp_server_socket.sendto(messaggio.encode(), client_address)
        except Exception as e:
            print(f"Errore2: {e}")

# Creo i threads
thread_ricevitore = threading.Thread(target=riceviMessaggi)
thread_inviatore = threading.Thread(target=inviaMessaggi)

# Avvio i threads
thread_ricevitore.start()
thread_inviatore.start()

# Aspetto che i thread finiscano (questo potrebbe non accadere mai in questo caso)
thread_ricevitore.join()
thread_inviatore.join()

# Chiusura del socket
udp_server_socket.close()
