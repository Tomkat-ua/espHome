import aioesphomeapi
import asyncio
#import win32api
#import win32gui
import register
import datetime

# APPCOMMAND_MIC_ON_OFF_TOGGLE      44 Toggle the microphone.
# APPCOMMAND_MICROPHONE_VOLUME_DOWN 25 Decrease microphone volume.
# APPCOMMAND_MICROPHONE_VOLUME_MUTE 24 Mute the microphone.
# APPCOMMAND_MICROPHONE_VOLUME_UP   26 Increase microphone volume.

host =  "192.168.2.31"
password =  "EspAdminn"
#loop = asyncio.get_running_loop()
#cli = aioesphomeapi.APIClient(loop, host, 6053, password)

# def mic_man(state):
#     WM_APPCOMMAND = 0x319
#     APPCOMMAND_MICROPHONE_VOLUME_MUTE = 0x180000 #24
#     APPCOMMAND_MIC_ON_OFF_TOGGLE      = 0x2C0000 #44
#     APPCOMMAND_MICROPHONE_VOLUME_DOWN = 0x190000 #25
#     APPCOMMAND_MICROPHONE_VOLUME_UP   = 0x1a0000 #26
#     hwnd_active = win32gui.GetForegroundWindow()
#     if state == True:
#         win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_UP)
#     if state == False:
#         win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_MUTE)

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
        #print( lInfo.key)
    #     print(lInfo.key )
        # for j in range(len(lInfo)):
        #     print(str(lInfo))
        #print(str(i) +':'+ str(sInfo[i].key)+',' +str(sInfo[i].name) )
        #if sInfo[i].key == 575851988:
        #    print(str(sInfo[i].name))

    #print(sInfo[3].name)
    # print(entities[0][3].name)
    # print(entities[0][3].index('575851988'))
# loop = asyncio.get_event_loop()
# loop.run_until_complete(info())

def _log(key,state,missing_state):
    today = datetime.datetime.today()
    action_date  = str(today.strftime("%d.%m.%Y %H:%M:%S"))
    return ('<ROWSET>\n	<ROW>\n' \
		    '		<ACTION_DATE>'+action_date+'</ACTION_DATE>\n' \
#		    '		<ACTION_DESCRIPTION>'+'test'+'</ACTION_DESCRIPTION>\n' \
#            '		<OBJECT_NAME>'+'sensor1' +'</OBJECT_NAME>\n' \
            '		<KEY>'+str(key)+'</KEY>\n' \
            '		<STATE>'+ str(state) + '</STATE>\n' \
            '    <MISSION_STATE>'+ str(missing_state) + '</MISSION_STATE>\n' \
		    '  </ROW>\n</ROWSET>')


async def main():

    """Connect to an ESPHome device and wait for state changes."""
    loop = asyncio.get_running_loop()
    cli = aioesphomeapi.APIClient(loop,host, 6053, password)

    await cli.connect(login=True)

    def change_callback(state):
        #if state.key == 575851988:
        today = datetime.datetime.today()
        if state.state != 0.0:
#            print(str(today.strftime("%d.%m.%Y %H:%M:%S")) +' '+ str(state))
            print(_log(state.key,state.state,state.missing_state))
            #register.send(_log(state.key,state.state,state.missing_state),2)

    # Subscribe to the state changes
    await cli.subscribe_states(change_callback)

loop = asyncio.get_event_loop()
#asyncio.ensure_future(main())
try:

     #asyncio.ensure_future(info())
     asyncio.ensure_future(main())
     loop.run_forever()
#except cli.call_connection_lost:
 #   pass
except KeyboardInterrupt:
    pass
finally:
    loop.close()
