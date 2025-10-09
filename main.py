import os
import socket

username = os.getlogin()
hostname = socket.gethostname()
key_exit = False

def emulation(command):
        key = False
        global key_exit
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
                key_exit = True
                break

            elif not key:
                print("Invalid command")
                break

with open("vfs.txt", "r") as f:
    for line in f.readlines():
        if line.startswith("#"):
            continue
        if not key_exit:
            print("vfs@", line.rstrip())
            print(emulation(line))