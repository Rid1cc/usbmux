import sys
sys.path.insert(0, '/API/')

from API import mux_connector_api

example = mux_connector_api.MuxConnectorApi()
print(example.reboot())