import socket

HOST = '127.0.0.1'
PORT = 12345

# Datenzugriffsschicht: Sitzplätze und Status
SEATS = {
    'A1': False, 'A2': False, 'A3': False,
    'B1': False, 'B2': False, 'B3': False
}


def handle_message(client_socket, message: str):
    """Logikschicht: verarbeitet eine Nachricht und sendet Antwort zurück."""
    message = message.strip().upper()

    # LIST → freie Plätze
    if message == "LIST":
        free_seats = [seat for seat, reserved in SEATS.items() if not reserved]
        if free_seats:
            response = ",".join(free_seats)
        else:
            response = "No seats available!"

    # Sitz reservieren
    elif message in SEATS:
        if not SEATS[message]:
            SEATS[message] = True
            response = "Seat reserved successfully!"
        else:
            response = "Seat already reserved!"

    # Fehler
    else:
        response = "Invalid seat number!"

    client_socket.sendall((response + "\n").encode("utf-8"))


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print('Server started. Waiting for connections...')

    while True:
        client_socket, addr = server_socket.accept()
        print('Connected to', addr)

        with client_socket:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                message = data.decode('utf-8')
                handle_message(client_socket, message)


if __name__ == "__main__":
    main()
