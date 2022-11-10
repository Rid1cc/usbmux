import argparse

ARGPARSER = argparse.ArgumentParser(description="Interface for connected muxes.")
ARGPARSER.add_argument("--inf", help="Prints device info.")
ARGPARSER.add_argument("--reboot", help="Reboots device.")
ARGPARSER.add_argument("--relayname", help="Changes relay name", nargs=2)