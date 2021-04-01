#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("Please enter the IP you want to scan: ")
port = int(input("Please enter the Port you want to scan: "))
s.settimeout(5)


def portScanner(port):
    if s.connect_ex((host, port)):
        print("the port is closed")
    else:
        print("The port is open")


portScanner(port)
