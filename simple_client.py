# -*- coding: utf-8 -*-
"""
This code was written by Ofek Haim.
Python - TCP client.
v = 0.0.2
Last edit: 27.6.2017
"""

import socket
import sys

SERVER_IP = '127.0.0.1'
SERVER_PORT = 660
ERROR_MASSAGE_SERVER_OFFLINE = "The server is offline ... :("


class Client(object):
    """
    This class include functions for TCP client.
    """
    def __init__(self):
        self.my_socket = None

    def connect(self, server_ip, server_port):
        """
        This function connect to the server.
        This function get server ip and port number.
        """
        self.my_socket = socket.socket()
        try:
            self.my_socket.connect((server_ip, server_port))
        except socket.error:
            sys.exit(ERROR_MASSAGE_SERVER_OFFLINE)

    def send_data(self, data):
        """
        This function send data to connect server.
        """
        self.my_socket.send(data)

    def get_data(self):
        """
        This function return data that sent from the server,
        by reading him from the buffer.
        """
        return self.my_socket.recv(1024)

    def close_connection(self):
        """
        This function close the connection whit the server.
        """
        self.send_data('')
        self.my_socket.close()


def main():
    client = Client()
    client.connect(SERVER_IP, SERVER_PORT)
    client.send_data("---")
    print client.get_data()
    client.close_connection()


if __name__ == '__main__':
    main()