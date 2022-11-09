import argparse

ARGPARSER = argparse.ArgumentParser(description="Interface for connected muxes.")
ARGPARSER.add_argument("--inf", help="Prints device info. [INF-port_name]")
ARGPARSER.add_argument("--reboot", help="Reboots device. [Reboot-port_name]")