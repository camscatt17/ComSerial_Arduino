import serial
port_USB = "COM6"

def print_answer():
    answer = connection.read()
    if answer == b'1':
        print("Led Turn On.")
    elif answer == b'0':
        print("Led Turn Off.")

def user_interaction():
    return input("Type <L> to turn on the led or <D> to turn off the led: ").upper()

def valid_connection():
    action = user_interaction()
    while action == "L" or action == "D":
        if action == "L":
            connection.write(b'1')
        elif action == "D":
            connection.write(b'0')
        else:
            connection.write(b'0')
            break
        print_answer()
        action = user_interaction()
    connection.close()
    print("Connection Closed")


try:
    connection = serial.Serial(port_USB, 115200, timeout=0.5)
    print("Plugged into port: ", connection.portstr)
    valid_connection()
except serial.SerialException:
    print("No ports available.")
    pass
