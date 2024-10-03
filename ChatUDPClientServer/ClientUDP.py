import socket
import threading

# Definisce l'indirizzo IP e la porta del server a cui connettersi
server_ip = "127.0.0.1"  # Cambia in "localhost" se necessario
server_port = 12346
server_address = (server_ip, server_port)
buffer_size = 4092
messaggio = ""

# Crea un socket UDP
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Provo un associazione in modo che il server sappia che sono il client (altrimenti da un errore in ricezione del client)
udp_client_socket.sendto("CollegamentoAvvenuto".encode(), server_address)

# Funzione che riceve i messaggi
def riceviMessaggi():
    while True:
        try:
            data, address = udp_client_socket.recvfrom(buffer_size)  # E' BLOCCANTE
            print(f"Server: {data.decode()}")
            print("Client: ")
        except Exception as e:
            print(f"ErroreRicezione: {e}")

# Funzione che invia i messaggi
def inviaMessaggi():
    while True:
        try:
            messaggio = input("Client: ")
            udp_client_socket.sendto(messaggio.encode(), server_address)
        except Exception as e:
            print(f"ErroreInvio: {e}")

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
udp_client_socket.close()
