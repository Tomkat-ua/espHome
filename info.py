import aioesphomeapi
import asyncio




host =  "192.168.2.31"
password =  "EspAdminn"


async def info ():
    """Connect to an ESPHome device and get details."""
    loop = asyncio.get_running_loop()

    # Establish connection
    api = aioesphomeapi.APIClient(loop,host, 6053, password)
    await api.connect(login=True)

    # Get API version of the device's firmware
    #print("api.api_version:"+str(api.api_version))

    # Show device details
    device_info = await api.device_info()
    #print("device_info:"+str(device_info))

    # List all entities of the device
    entities = await api.list_entities_services()
    #print("entities:"+str(entities))

    ###
    sInfo = entities[0]
    #rint (len(sInfo))
    d = {}
    for i in range(len(sInfo)):
        lInfo = sInfo[i]
        print( str(lInfo.key) +';'+ str(lInfo.name))

loop = asyncio.get_event_loop()

try:

    asyncio.ensure_future(info())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    loop.close()
