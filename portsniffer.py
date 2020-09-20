import socket
import subprocess
import sys
from datetime import datetime

def read_config(cfgfile):
    """
    Takes the path to the config file as argument and returns the 
    a dictionary with process names as keys and port numbers as 
    values. Note that the values are integers, not numeric strings.
    """
    pass


def sniff_ports(hostname, process_dict):
    """
    Takes the hostname/IP address of the target host and the dict
    object returned by "read_config" as arguments and returns a
    list containing the process names that are running on the 
    target host.
    """
    pass

"""
if __name__ == "__main__":
    subprocess.call('clear', shell=True)
    hostname = ""
    if sys.argv.__len__() < 2:
        hostname    = raw_input("Enter a remote host to scan: ")
    else:
        hostname = sys.argv[1]
    ip_pattern = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1, 3}$")
    if not re.search(ip_pattern, hostname): # This is a hostname, not an IP.
        hostname  = socket.gethostbyname(hostname)
    process_dict = read_config("conf/processes.cfg")
    running_processes = sniff_ports(hostname, process_dict)
"""




# Clear the screen
subprocess.call('clear', shell=True)

# Ask for input
remoteServer    = raw_input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print "-" * 60
print "Please wait, scanning remote host", remoteServerIP
print "-" * 60

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)

# We also put in some error handling for catching errors

try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}: 	 Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total


