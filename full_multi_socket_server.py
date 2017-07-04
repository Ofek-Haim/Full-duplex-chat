# -*- coding: utf-8 -*-
"""
This code was written by Ofek Haim.
Python - TCP server.
v = 0.0.2
Last edit: 27.6.2017
"""

import socket
import select

MAX_NUMBER_OF_CONNECT_CLIENTS = 10
STATIC_ROUTING_IP = '0.0.0.0'
PORT_NUMBER = 660


class Server(object):
    def __init__(self, port_number):
        self.open_client_socket = []
        self.massages_to_send = []
        self.server_socket = None
        self.port_number = port_number

    def send_waiting_messages(self, w_list):
        for message in self.massages_to_send:
            (client_socket, data) = message
            if client_socket in w_list:
                client_socket.send(data)
                self.massages_to_send.remove(message)

    def run(self):
        """
        This function get data from clients.
        This function checking the request and return
        answer to connect client.
        """
        while 1:
            r_list, w_list, x_list = select.select([self.server_socket] + self.open_client_socket,
                                                   self.open_client_socket, [])
            for current_socket in r_list:
                if current_socket is self.server_socket:
                    (new_socket, address) = self.server_socket.accept()
                    self.open_client_socket.append(new_socket)
                else:
                    data = current_socket.recv(1024)
                    if data == "":
                        self.open_client_socket.remove(current_socket)
                        print "The connection with client  (" + str(current_socket) + ")  closed..."
                    else:
                        self.massages_to_send.append((current_socket, 'Add by the server, ' + data))
            self.send_waiting_messages(w_list)

    def up(self):
        """
        This function up the server online.
        """
        self.server_socket = socket.socket()
        self.server_socket.bind((STATIC_ROUTING_IP, self.port_number))
        self.server_socket.listen(MAX_NUMBER_OF_CONNECT_CLIENTS)


def main():
    server = Server(PORT_NUMBER)
    server.up()
    server.run()


if __name__ == '__main__':
    main()