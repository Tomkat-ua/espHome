import win32api
import win32gui

# APPCOMMAND_MIC_ON_OFF_TOGGLE      44 Toggle the microphone.
# APPCOMMAND_MICROPHONE_VOLUME_DOWN 25 Decrease microphone volume.
# APPCOMMAND_MICROPHONE_VOLUME_MUTE 24 Mute the microphone.
# APPCOMMAND_MICROPHONE_VOLUME_UP   26 Increase microphone volume.


def mic_man(state):
     WM_APPCOMMAND = 0x319
     APPCOMMAND_MICROPHONE_VOLUME_MUTE = 0x180000 #24
     APPCOMMAND_MIC_ON_OFF_TOGGLE      = 0x2C0000 #44
     APPCOMMAND_MICROPHONE_VOLUME_DOWN = 0x190000 #25
     APPCOMMAND_MICROPHONE_VOLUME_UP   = 0x1a0000 #26
     hwnd_active = win32gui.GetForegroundWindow()
     if state == True:
         win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_UP)
     if state == False:
         win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_MUTE)


