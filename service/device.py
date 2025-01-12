from math import e
from bleak import BleakClient, BleakScanner
import asyncio


class Scanner():
    async def Scan():
        devices = await BleakScanner.discover()
        for d in devices:
            print(d)


class Device():
    def __init__(self, MAC_ADDRESS, TEMPERATURE_HUMIDITY_UUID, MODEL_NBR_UUID):
        self.MAC_ADDRESS = MAC_ADDRESS
        self.MODEL_NBR_UUID = MODEL_NBR_UUID
        self.TEMPERATURE_HUMIDITY_UUID = TEMPERATURE_HUMIDITY_UUID
        self.client = None
        
    async def connect(self):
        self.client = BleakClient(self.MAC_ADDRESS)
        try:
            await self.client.connect()
        except Exception as e:
            print(e)

    async def getModel(self):
        try:
            model_number = await self.client.read_gatt_char(self.MODEL_NBR_UUID)
            print("Model Number: {0}".format(
                "".join(map(chr, model_number))))
        except Exception as e:
            print(e)

    async def getTemperatureHumidityData(self):
        try:
            data = await self.client.read_gatt_char(self.TEMPERATURE_HUMIDITY_UUID)
            print(data)
        except Exception as e:
            print(e)

    async def disconnect(self):
        try:
            await self.client.disconnect()
        except Exception as e:
            print(e)
