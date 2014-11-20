'''for wmplayer operations, win8.1 os

    'wmplayer_start',
    'wmplayer_close',
               
    'wmplayer_open_media_file',
    'wmplayer_play'
    'wmplayer_pause'
    'wmplayer_set_repeat_on',
    'wmplayer_set_repeat_off'
    'wmplayer_volume_up'
    'wmplayer_volume_down'
    'wmplayer_mute'
    'wmplayer_unmute'
    'wmplayer_seek'
               
    'wmplayer_wait_playback_end',
'''

import os
import AXUI

config_file = "windows.cfg"
app_map = "windows_media_player.xml"

AXUI.Config(config_file)
appmap = AXUI.AppMap(app_map)

def wmplayer_start():
    appmap.wmplayer_Window.start()
    
def wmplayer_close():
    appmap.wmplayer_Window.stop()
    
def wmplayer_open_media_file(media_file):
    if not os.path.isfile(media_file):
        print("media file not exist: %s" % media_file)
        return
    appmap.wmplayer_Window.Open_Dialog.FileName_ComboBox.FileName_Edit.ValuePattern.SetValue(media_file)
    appmap.wmplayer_Window.Open_Dialog.Open_Button.InvokePattern.Invoke()
    
def wmplayer_play():
    appmap.wmplayer_Window.TransportSubview_Group.Play_Pause_Button.start()
    if appmap.wmplayer_Window.TransportSubview_Group.Play_Pause_Button.Name == "Play":
        appmap.wmplayer_Window.TransportSubview_Group.Play_Pause_Button.InvokePattern.Invoke()
        
def wmplayer_pause():
    appmap.wmplayer_Window.TransportSubview_Group.Play_Pause_Button.start()
    if appmap.wmplayer_Window.TransportSubview_Group.Play_Pause_Button.Name == "Pause":
        appmap.wmplayer_Window.TransportSubview_Group.Play_Pause_Button.InvokePattern.Invoke()

def wmplayer_set_repeat_on():
    appmap.wmplayer_Window.TransportSubview_Group.repeat_Button.start()
    if appmap.wmplayer_Window.TransportSubview_Group.repeat_Button.Name == "Turn repeat on":
        appmap.wmplayer_Window.TransportSubview_Group.repeat_Button.InvokePattern.Invoke()
        
def wmplayer_set_repeat_off():
    appmap.wmplayer_Window.TransportSubview_Group.repeat_Button.start()
    if appmap.wmplayer_Window.TransportSubview_Group.repeat_Button.Name == "Turn repeat off":
        appmap.wmplayer_Window.TransportSubview_Group.repeat_Button.InvokePattern.Invoke()
        
def wmplayer_volume_up():
    appmap.wmplayer_Window.keyboard.Input('{F9}')
    
def wmplayer_volume_down():
    appmap.wmplayer_Window.keyboard.Input('{F8}')
    
def wmplayer_mute():
    appmap.wmplayer_Window.MenuBar.Play_MenuItem.SetFocus()
    if int(appmap.wmplayer_Window.Volume_Menu.Mute_MenuItem.LegacyIAccessiblePattern.CurrentState) == int(0):
        appmap.wmplayer_Window.Volume_Menu.Mute_MenuItem.InvokePattern.Invoke()
        
def wmplayer_unmute():
    appmap.wmplayer_Window.MenuBar.Play_MenuItem.SetFocus()
    if int(appmap.wmplayer_Window.Volume_Menu.Mute_MenuItem.LegacyIAccessiblePattern.CurrentState) == int(16):
        appmap.wmplayer_Window.Volume_Menu.Mute_MenuItem.InvokePattern.Invoke()
        
def wmplayer_seek(seek_value):
    left, right, top, bottom = appmap.wmplayer_Window.Seek_Slider.coordinate
    
    x = (right-left)*(seek_value/100)+left
    y = (bottom+top)/2
    
    appmap.wmplayer_Window.Seek_Slider.SetFocus()
    appmap.wmplayer_Window.Seek_Slider.mouse.LeftClick((x,y))
    
def wmplayer_wait_playback_end():
    import time
    while True:
        time.sleep(1)
        if appmap.wmplayer_Window.TransportSubview_Group.Play_Pause_Button.Name == "Play":
            break
    