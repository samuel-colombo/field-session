import bluetooth
import argparse
import sensors
import numpy as np
import RPi.GPIO as GPIO

# use GPIO numbering
GPIO.setmode(GPIO.BCM)

CHUNK_SIZE = 1024

# Create an ArgumentParser to parse the command-line arguments
#parser = argparse.ArgumentParser(description='Bluetooth client script')
#parser.add_argument('server_address', type=str, help='Server Bluetooth device address')
# parser.add_argument('port', type=int, help='Port number to connect to')
# args = parser.parse_args()

# Retrieve the server address and port from the command-line arguments
server_address = "XX:XX:XX:XX:XX:XX"        # format: "XX:XX:XX:XX:XX:XX"
port = 4

client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

try:
    client_socket.connect((server_address, port))
except bluetooth.btcommon.BluetoothError as e:
    print(f"Bluetooth error: {e}")

# For each piece of data read from sensor, send the data
data_lists = sensors.readHeartData(30)
for data in data_lists:
    data_str = np.array2string(data,separator=",")
    bytes_to_send = data_str.encode()

    for i in range(0, len(bytes_to_send), CHUNK_SIZE):
        client_socket.send(bytes_to_send[i:i + CHUNK_SIZE])

client_socket.send("$$$")

data = client_socket.recv(1024)
print(f"Received: {data}")

client_socket.close()