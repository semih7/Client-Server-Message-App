import socket


def client_program():
    host = "localhost"  # Localde çalışacağı için bilgisayarın ip adresini alacağı host değişkenini tanımladık.
    port = 8080                  # Bağlanacak soketin port numarası girişini sağladık.

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Client soketi oluşturduk
    client_socket.connect((host, port))                                # Client'ın server'a bağlanmasını sağladık.

    ad = print("Kullanıcı adı girin: ")

    message = input(" -> ")                         # Gönderilmek istenen mesajın girilmesi için bir input oluşturduk.

    while message.lower().strip() != 'exit':
        client_socket.send(message.encode())                # Mesajın gönderilmesini sağladık.
        data = client_socket.recv(1024).decode()            # Server tarafından gelen mesajın okunmasını sağladık.

        print('Received from server: ' + data)              #Server tarafından gelen mesajı yazdırdık.

        message = input(" -> ")                             #Sürekli mesajlaşmayı sağladık.

        if message.lower().strip() == 'exit' :
            client_socket.send(message.encode())

    client_socket.close()                                   # Bağlantıyı sonlandırdık.


if __name__ == '__main__':
    client_program()