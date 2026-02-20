import socket

HOST = '127.0.0.1'
PORT = 12345


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((HOST, PORT))
        print("Connected to server. Type LIST or a seat"
              "(e.g., A1). CTRL+C to quit.")

        while True:
            choice = input('> ')
            if not choice.strip():
                break

            # senden
            client_socket.sendall((choice + "\n").encode("utf-8"))

            # empfangen
            data = client_socket.recv(1024)
            response = data.decode("utf-8").strip()

            # anzeigen
            print("Server:", response)

    except KeyboardInterrupt:
        print("\nBeendet durch Benutzer.")
    except Exception as e:
        print("Fehler:", e)
    finally:
        client_socket.close()
        print("Connection closed.")


if __name__ == "__main__":
    main()
