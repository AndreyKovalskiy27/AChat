"""Тестовий клієнт для сервера"""


from connection import connection


connection_socket = connection.Connection("127.0.0.1", int(input()), "Andrey")

while True:
    print("saad")
    message = input("Enter message: ")

    if message == "exit":
        connection_socket.exit()
        exit()

    else:
        connection_socket.send_message({"type": "message", "message": message})
