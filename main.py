import serial.tools.list_ports


from time import sleep
from enum import Enum


class off_on(Enum):

    """Enum for off and on

    Args:
        Enum (str): enum for off and on
    """
    ON = '1'
    OFF = '0'


def check_mux_inf(port_name: str):

    """Returns info message

    Args:
        port_name (str): port name of port where MUX is connected

    Returns:
        list: returns info message
    """
    with serial.Serial(
            port_name,
            baudrate=115200,
            timeout=1,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE
    ) as ser:
        try:
            ser.reset_input_buffer()
            ser.reset_output_buffer()
            ser.write(b'inf\n')
            sleep(1)
            # read all input buffer
            data = ser.read(ser.in_waiting)
            # decode bytes data into string and split lines
            lines = data.decode('UTF-8').split('\r\n')
            return lines

        except Exception as err:
            print(err, f"happened at port {port_name}")
            print()
            return []


def mux_reboot(port_name: str):

    """Reboots MUX

    Args:
        port_name (str): port name of port where MUX is connected
    """
    with serial.Serial(
            port_name,
            baudrate=115200,
            timeout=1,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE
    ) as ser:
        try:
            ser.reset_input_buffer()
            ser.reset_output_buffer()
            ser.write(b'r\n')
            sleep(1)
            print("REBOOTED")

        except Exception as err:
            print(err, f"happened at port {port_name}")
            print()


def change_mux_name(port_name: str, mux_name: str):

    """Changes MUX name
    Args:
        port_name (str): port name of port where MUX is connected
        mux_name (str): new name of MUX
    """
    with serial.Serial(
            port_name,
            baudrate=115200,
            timeout=1,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE
    ) as ser:
        try:
            ser.reset_input_buffer()
            ser.reset_output_buffer()
            test = f'n,{mux_name}\n'
            ser.write(bytes(test, encoding='utf-8'))
            sleep(1)
            print("RENAMED")

        except Exception as err:
            print(err, f"happened at port {port_name}")
            print()


def switch_relay(port_name: str, relay_id: str, relay_state: off_on):

    """Switches relay state(on/off)

    Args:
        port_name (str): port name of port where MUX is connected
        relay_id (str): id of relay
        relay_state (off_on): relay state in enum off_on
    """
    with serial.Serial(
            port_name,
            baudrate=115200,
            timeout=1,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE
    ) as ser:
        try:
            ser.reset_input_buffer()
            ser.reset_output_buffer()
            power = f'pwr,{relay_id},{relay_state.value}\n'
            ser.write(bytes(power, encoding='utf-8'))
            sleep(1)
            if relay_state == off_on.ON:
                print("Relay ON")
            if relay_state == off_on.OFF:
                print("Relay OFF")
        except Exception as err:
            print(err, f"happened at port {port_name}")
            print()


def get_name(port_name: str):

    """Returns name of MUX

    Args:
        port_name (str): port name of port where MUX is connected

    Returns:
        str: returns name of MUX
    """
    with serial.Serial(
            port_name,
            baudrate=115200,
            timeout=1,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE
    ) as ser:
        try:
            ser.reset_input_buffer()
            ser.reset_output_buffer()
            ser.write(b'inf\n')
            sleep(1)
            data = ser.read(ser.in_waiting)  # read all input buffer
            lines = data.decode('UTF-8').split('\r\n')
            line = lines[3]
            if line[0:5] == "Name:":
                return line[6:]
            else:
                return 'no_name'
        except Exception as err:
            print(err, f"happened at port {port_name}")
            print()
            return 'error'


if __name__ == '__main__':
    change_mux_name('COM4', 'default')
    switch_relay('COM4', '1', off_on.ON)
    print(get_name('COM4'))
    print(check_mux_inf('COM4'))
    mux_reboot('COM4')
