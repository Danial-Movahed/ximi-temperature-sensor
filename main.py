import asyncio
from args.ArgParser import ArgParser
from service import Device, Scanner
from config.configParser import ConfigParser


if __name__ == '__main__':
    AP = ArgParser()
    configParser = ConfigParser()

    if AP.args.scan:
        asyncio.run(Scanner.Scan())
        
    elif AP.args.getmodel:
        dev = Device(
            MAC_ADDRESS = configParser.config["MAC_ADDRESS"],
            TEMPERATURE_HUMIDITY_UUID = configParser.config["TEMPERATURE_HUMIDITY_UUID"],
            MODEL_NBR_UUID = configParser.config["MODEL_NBR_UUID"],
        )
        asyncio.run(dev.connect())
        asyncio.run(dev.getModel())
        asyncio.run(dev.disconnect())

    elif AP.args.setmac:
        configParser.config["MAC_ADDRESS"] = AP.args.setmac
        configParser.save()

    elif AP.args.setmodeluuid:
        configParser.config["MODEL_NBR_UUID"] = AP.args.setmodeluuid
        configParser.save()

    elif AP.args.setdatauuid:
        configParser.config["TEMPERATURE_HUMIDITY_UUID"] = AP.args.setmodeluuid
        configParser.save()

    else:
        dev = Device(
            MAC_ADDRESS = configParser.config["MAC_ADDRESS"],
            TEMPERATURE_HUMIDITY_UUID = configParser.config["TEMPERATURE_HUMIDITY_UUID"],
            MODEL_NBR_UUID = configParser.config["MODEL_NBR_UUID"],
        )
        asyncio.run(dev.connect())
        asyncio.run(dev.getTemperatureHumidityData())
        asyncio.run(dev.disconnect())
