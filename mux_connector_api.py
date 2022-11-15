from enum import Enum
from time import sleep

import serial.tools.list_ports


class off_on(Enum):
    """Enum for off and on

    Args:
        Enum (str): enum for off and on
    """
    ON = '1'
    OFF = '0'


class Handler:
    def __init__(self, port_name: str):
        """Constructor of class

        Args:
            port_name (str): port name of port connected with mux
        """
        self.port_name = port_name
        self.ser = serial.Serial(
            port_name,
            baudrate=115200,
            timeout=1,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE
        )

    def check_relay_state(self, relay_id):
        try:
            self.ser.reset_input_buffer()
            self.ser.reset_output_buffer()
            state = f'st,{relay_id}\n'
            self.ser.write(bytes(state, encoding='utf-8'))
            sleep(1)
            data = self.ser.read(self.ser.in_waiting)

            lines = data.decode('UTF-8').split('\r\n')
            line = lines[2]
            if line == "PowerRelay{relay_id} state SET to: RELAY_ON":
                print(line)
                return off_on.ON
            else:
                print(line)
                return off_on.OFF

            return lines
        except Exception as err:
            print(err, f"happened at port {self.port_name}")
            print()
            return None

    def check_mux_inf(self):
        """Returns info message

        Returns:
            lines (List[str]): returns info message
        """
        try:
            self.ser.reset_input_buffer()
            self.ser.reset_output_buffer()
            self.ser.write(b'inf\n')
            sleep(1)
            # read all input buffer
            data = self.ser.read(self.ser.in_waiting)
            # decode bytes data into string and split lines
            lines = data.decode('UTF-8').split('\r\n')
            return lines

        except Exception as err:
            print(err, f"happened at port {self.port_name}")
            print()
            return None

    def mux_reboot(self):
        """Reboots MUX
        """
        try:
            self.ser.reset_input_buffer()
            self.ser.reset_output_buffer()
            self.ser.write(b'r\n')
            sleep(1)
            print("REBOOTED")
        except Exception as err:
            print(err, f"happened at port {self.port_name}")
            print()

    def change_mux_name(self, mux_name: str):
        """Changes MUX name

        Args:
            mux_name (str): new name of MUX
        """
        try:
            self.ser.reset_input_buffer()
            self.ser.reset_output_buffer()
            test = f'n,{mux_name}\n'
            self.ser.write(bytes(test, encoding='utf-8'))
            sleep(1)
            print("RENAMED")

        except Exception as err:
            print(err, f"happened at port {self.port_name}")
            print()

    def switch_relay(self, relay_id: int, relay_state: off_on):
        """Switches relay state(on/off)

        Args:
            relay_id (int): id of relay
            relay_state (off_on): relay state in enum off_on
        """
        try:
            self.ser.reset_input_buffer()
            self.ser.reset_output_buffer()
            power = f'pwr,{relay_id},{relay_state.value}\n'
            self.ser.write(bytes(power, encoding='utf-8'))
            sleep(1)
            if relay_state == off_on.ON:
                print("Relay ON")
            if relay_state == off_on.OFF:
                print("Relay OFF")
        except Exception as err:
            print(err, f"happened at port {self.port_name}")
            print()

    def get_name(self):
        """Returns name of MUX

        Returns:
            name (str): returns name of MUX
        """
        try:
            self.ser.reset_input_buffer()
            self.ser.reset_output_buffer()
            self.ser.write(b'inf\n')
            sleep(1)
            data = self.ser.read(self.ser.in_waiting)  # read all input buffer
            lines = data.decode('UTF-8').split('\r\n')
            line = lines[3]
            if line[0:5] == "Name:":
                return line[6:]
            else:
                return None
        except Exception as err:
            print(err, f"happened at port {self.port_name}")
            print()
            return None
