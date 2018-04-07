# -*- coding: utf-8 -*-
import socket
import thread


class MultiTCPServer(object):
    def __init__(self, port_number=7800):
        self.server_socket = socket.socket()
        self.port_number = port_number
        self.buffer_size = 1024

    def bind_the_server(self):
        self.server_socket.bind(('0.0.0.0', self.port_number))

    def listen(self, number_of_waiting_clients=5):
        self.server_socket.listen(number_of_waiting_clients)

    def accept_and_run(self):
        client_socket, client_address = self.server_socket.accept()
        thread.start_new_thread(self.management_with_client, (client_socket, client_address))

    def management_with_client(self, client_socket, client_address):
        data = client_socket.recv(self.buffer_size)
        print data
        client_socket.send("Ofek Haim ... ")

    def close_the_server(self):
        self.server_socket.close()

def main():
    s = MultiTCPServer(7800)
    s.bind_the_server()
    s.listen()
    while 1:
        s.accept_and_run()
    s.close_the_server()


if __name__ == '__main__':
    main()