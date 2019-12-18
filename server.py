import socket


def server_program():
    host = "localhost"      #host local bilgisayarın ip adresini alacaktır.
    port = 8080                      #Boş olduğunun garanti olması amacıyla 8080 değerini seçtik.

    print('Server created... Waiting for connection')

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # soket oluşturulmasını sağladık.
    server_socket.bind((host, port))  #ip adresi ve port numarası ile soketin eşleştirilmesini sağladık.

    # sunucunun aynı anda kaç istemciyi dinleyebileceğini yapılandırdık. 2 olarak ayarladık.
    server_socket.listen(2)
    conn, address = server_socket.accept()  # gelen bağlantının kabul edilmesini sağladık.
    print("Connection from: " + str(address))
    while True:
        # mesajlaşmak için veri akışının alınmasını sağladık. 1024 byte tan büyük olanları almadık.
        data = conn.recv(1024).decode()
        if not data:
            # eğer data elimize ulaşmamışsa break komutu ile çıkış yapılmasını sağladık.
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # server tarafından client'a mesaj gönderilmesini sağladık.

    conn.close()  # bağlantıyı sonlandırdık.


if __name__ == '__main__':
    server_program()