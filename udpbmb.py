#!/usr/bin/python
import sys
import os
import time
import datetime
import argparse
import signal
import threading
import platform
import socket


def signal_handler(signal, frame):
    config.operation_status = False
    loop = 0
    print("\nStopping connection tester. Thanks for using.")
    print("Please visit https://github.com/timgold81/")
    print("contact timgold@gmail.com\n")

signal.signal(signal.SIGINT, signal_handler)

class server_worker(threading.Thread):
    port_nu = 0;
    def __init__(self, p):
        threading.Thread.__init__(self)
        self.port_nu = p

    def run(self):
        if (self.port_nu == 0):
            print("No port number , cannot start")
            exit(-1)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setblocking(0)
        sock.bind((config.dest_ip, self.port_nu))
        while config.operation_status:
            for i in range(1, config.interval):
                time.sleep(1)
                if (not config.operation_status):
                    break;
            try:
                data, addr = sock.recvfrom(1024)
            except socket.error:
                sock.close()
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.setblocking(0)
                sock.bind((config.dest_ip, self.port_nu))


class client_worker(threading.Thread):
    port_nu = 0;

    def __init__(self, p):
        threading.Thread.__init__(self)
        self.port_nu = p

    def run(self):
        if (self.port_nu == 0):
            print("No port number , cannot start")
            exit(-1)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while config.operation_status:
            sock.sendto("1".encode(), (config.dest_ip, self.port_nu))
            for i in range(1, config.interval):
                time.sleep(1)
                if (not config.operation_status):
                    break;

class configuration:
    operation_mode = ""
    dest_ip = ""
    start_port = 0
    number_of_ports = 0
    operation_status = True
    interval = 5


parser = argparse.ArgumentParser(description="Performs stress test: generates UDP connections.\nThis tool is used to generate a lot of UDP connections")
parser.add_argument("-s", "--server", help="Start as a server, and listen on specified address")
parser.add_argument("-c", "--client", help="Start as a client, and start sending from specified address")
parser.add_argument("-p", "--port", help="Starting port. Default: 2000")
parser.add_argument("-n", "--number_of_ports", help="Number of sequential ports to open. Default: 1")
parser.add_argument("-i", "--interval",
                    help="Interval in seconds between reading or writing to or from a port. Default: 5 sec")
args = parser.parse_args()

config = configuration()

if (args.interval):
    config.interval = int(args.interval)

if (args.server):
    config.operation_mode = "server"
    config.dest_ip = args.server

if (args.client):
    config.operation_mode = "client"
    config.dest_ip = args.client

if ((not args.server) and (not args.client)):
    print("Must specify if client or server")
    print("Use --help for help")
    exit(-1)

if (args.server and args.client):
    print("Cant be a client and a server at the same time\n")
    print("Use --help for help")
    exit(-1)

if (args.port):
    config.start_port = int(args.port)
else:
    config.start_port = 2000

if (args.number_of_ports):
    config.number_of_ports = int(args.number_of_ports)
else:
    config.number_of_ports = 1

if (config.operation_mode == "server"):
    # threads=[]
    for t in range(config.start_port, (config.number_of_ports + config.start_port)):
        thread = server_worker(t)
        thread.start()
else:
    for t in range(config.start_port, (config.number_of_ports + config.start_port)):
        thread = client_worker(t)
        thread.start()

print("Running. Press CTRL+C to stop")
while config.operation_status:
    time.sleep(0.2)
