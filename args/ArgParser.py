import argparse

class ArgParser():
    def __init__(self):
        self.parser = argparse.ArgumentParser(description = "Xiaomi temprature sensor")
        self.parser.add_argument("-s", "--scan", help = "Scan all btle devices", action='store_true')
        self.parser.add_argument("-g", "--getmodel", help = "Get sensor model", action='store_true')
        self.parser.add_argument("-m", "--setmac", help = "Set sensor mac address")
        self.parser.add_argument("-i", "--setmodeluuid", help = "Set model characteristic uuid")
        self.parser.add_argument("-d", "--setdatauuid", help = "Set temperature data characteristic uuid")
        self.parser.add_argument("-u", "--setunituuid", help = "Set unit characteristic uuid")
        self.args = self.parser.parse_args()