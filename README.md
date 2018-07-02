# UDP-bomber
Performs stress test: generates UDP connections. This tool is used to generate a lot of UDP connections
<pre>

usage: udpbmb.py [-h] [-s SERVER] [-c CLIENT] [-p PORT] [-n NUMBER_OF_PORTS]
                 [-i INTERVAL]

Performs stress test: generates UDP connections. This tool is used to generate a lot of UDP connections

optional arguments:
  -h, --help            show this help message and exit
  -s SERVER, --server SERVER
                        Start as a server, and listen on specified address
  -c CLIENT, --client CLIENT
                        Start as a client, and start sending from specified
                        address
  -p PORT, --port PORT  Starting port. Default: 2000
  -n NUMBER_OF_PORTS, --number_of_ports NUMBER_OF_PORTS
                        Number of sequential ports to open. Default: 1
  -i INTERVAL, --interval INTERVAL
                        Interval in seconds between reading or writing to or
                        from a port. Default: 5 sec

</pre>