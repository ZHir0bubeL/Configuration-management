import os
import socket

username = os.getlogin()
hostname = socket.gethostname()

while True:
    command = input(f"\n{username}@{hostname}:~$ ")
    for name in os.environ:
        command = command.replace("$" + name, os.environ[name])
    command = command.split()

    if command[0] == "cd":
        print(command[0] + ':', end=' ')
        for i in range(1, len(command)):
            if command[i] != "ls" and command[i] != "cd" and command[i][0] != "$":
                print(command[i], end=' ')
            else:
                continue

    elif command[0] == "ls":
        print(command[0] + ':', end=' ')
        for i in range(1, len(command)):
            if command[i] != "ls" and command[i] != "cd" and command[i][0] != "$":
                print(command[i], end=' ')
            else:
                continue

    elif command[0] == "exit":
        print("Exit")
        break

    else:
        print("Invalid command")