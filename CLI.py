import argparse

ARGPARSER = argparse.ArgumentParser(description="Finds connected USB-MUXes with ports they are connected to.")
ARGPARSER.add_argument("--inf",
                       help="Search for mux with provided name. Return it's port name.")