import serial.tools.list_ports
from time import sleep
from enum import Enum

class off_on(Enum):
    ON = '1'
    OFF = '0'



def checkMuxInf(port_name: str):
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
            lines = data.decode('UTF-8').split('\r\n')  # decode bytes data into string and split lines
            return lines

        except Exception as err:
            print(err, f"happened at port {port_name}")
            print()
            return []


def muxReboot(port_name: str):
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


def change_muxName(port_name:str, mux_name:str):
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
            test =f'n,{mux_name}\n'
            ser.write(bytes(test, encoding='utf-8'))
            sleep(1)
            print("RENAMED")

        except Exception as err:
            print(err, f"happened at port {port_name}")
            print()

def switchRelay(port_name:str, relay_id:str, relay_state:off_on):
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
            power =f'pwr,{relay_id},{relay_state.value}\n'
            ser.write(bytes(power, encoding='utf-8'))
            sleep(1)
            if relay_state == off_on.ON:
                print("Relay ON")
            if relay_state == off_on.OFF:
                print("Relay OFF")
        except Exception as err:
            print(err, f"happened at port {port_name}")
            print()

def get_name(port_name:str):
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
            if line[0:5]=="Name:":
                return line[6:]
            else:
                return 'no_name'
        except Exception as err:
            print(err, f"happened at port {port_name}")
            print()
            return 'error'




if __name__ == '__main__':
    change_muxName('COM4', 'default')
    switchRelay('COM4','1', off_on.ON)
    print(get_name('COM4'))
    muxReboot('COM4')


