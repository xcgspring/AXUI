
import unittest

class TestAppMap(unittest.TestCase):
    def setUp(self):
        self.app_map_xml = "windows_media_player.xml"
        
    def test_app_map_create(self):
        import AXUI.XML.app_map as app_map
        app_map_instance = app_map.AppMap(self.app_map_xml)
        
    def test_get_element(self):
        import AXUI.XML.app_map as app_map
        app_map_instance = app_map.AppMap(self.app_map_xml)
        desktop_element = app_map_instance.get_element_by_name("desktop.desktop")
        wmp_window_element = app_map_instance.get_element_by_name("library_window")
        play_button_element = app_map_instance.get_element_by_name("play")

