"""Основний модуль. Запускає сервер"""


import server


if __name__ == "__main__":
    print("AChat server, запуск")

    try:
        ip = input("Введіть IP: ")
        port = int(input("Введіть порт: "))

        if port >= 0 and port <= 65535:
            try:
                try:
                    print()
                    server.Server(ip, port)

                except KeyboardInterrupt:
                    print("Сервер вимкнений")
                    exit()

            except Exception as error:
                print("\nПомилка під час запуску сервера")
                print("Перевірте IP та порт")

        else:
            print("\nПорт повиннен бути числом від 0 до 65535 та доступним на вказаному IP")

    except ValueError:
        print("\nПорт повиннен бути числом")
