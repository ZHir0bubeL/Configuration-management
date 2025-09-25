import os
import socket

username = os.getlogin()
hostname = socket.gethostname()

while True:
    command = input(f"\n{username}@{hostname}:~$ ")
    key = False
    for name in os.environ:
        command = command.replace("$" + name, os.environ[name])
    command = command.split()

    for j in range(len(command)):
        if command[j] == "cd":
            print(command[j] + ':', end=' ')
            key = True
            for i in range(j + 1, len(command)):
                if command[i] != "ls" and command[i] != "cd" and command[i][0] != "$" and command[i] != "exit":
                    print(command[i], end=' ')
                else:
                    j = i
                    print("\n", end='')
                    break

        elif command[j] == "ls":
            key = True
            print(command[j] + ':', end=' ')
            for i in range(j + 1, len(command)):
                if command[i] != "ls" and command[i] != "cd" and command[i][0] != "$" and command[i] != "exit":
                    print(command[i], end=' ')
                else:
                    j = i
                    print("\n", end='')
                    break

        elif command[j] == "exit":
            print("Exit")
            break

        elif not key:
            print("Invalid command")

    break