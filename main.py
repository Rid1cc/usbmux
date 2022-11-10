import serial.tools.list_ports
from time import sleep



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
            for line in lines:
                print(line)

        except Exception as err:
            print(err, f"happened at port {port_name}")
            print()
def checkMuxReboot(port_name: str):
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
            data = ser.read(ser.in_waiting)  # read all input buffer
            lines = data.decode('UTF-8').split('\r\n')  # decode bytes data into string and split lines
            for line in lines:
                print(line)
            print("REBOOTED")

        except Exception as err:
            print(err, f"happened at port {port_name}")
            print()

# def change_nameMuxRelay(data_row: list):
#     try:
#         with open('data/relay_names.csv', 'rw') as csvfile:
#             write = csv.writer(csvfile)
#             read = csv.reader(csvfile)
#             for lines in read:
#                 if lines[0] == data_row[0] and lines[1] == data_row[1]:
#                     pass
#     except:
#         with open('data/relay_names.csv', 'x') as csvfile:
#             write = csv.writer(csvfile, fieldnames = ['Port Name', 'Relay ID', 'Relay Name'])
#             write.writeheader()
#             write.writerow(data_row)

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
            data = ser.read(ser.in_waiting)  # read all input buffer
            lines = data.decode('UTF-8').split('\r\n')  # decode bytes data into string and split lines
            for line in lines:
                print(line)
            print("RENAMED")

        except Exception as err:
            print(err, f"happened at port {port_name}")
            print()



if __name__ == '__main__':
    #checkMuxInf('COM4')
    #checkMuxReboot('COM4')
    change_muxName('COM4', 'essa')


