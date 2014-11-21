
import unittest

class TestAppMap(unittest.TestCase):
    def setUp(self):
        self.app_map_xml = "windows_media_player.xml"
        
    def test_app_map_create(self):
        import AXUI.XML.app_map as app_map
        app_map_instance = app_map.AppMap(self.app_map_xml)
        self.assertTrue(app_map_instance, "app map create instance fail")
        
    def test_app_map_singleton(self):
        import AXUI.XML.app_map as app_map
        app_map_instance = app_map.AppMap(self.app_map_xml)
        app_map_instance2 = app_map.AppMap(self.app_map_xml)
        self.assertIs(app_map_instance, app_map_instance2, "app map should have one instance for same xml")
        
    def test_get_element(self):
        import AXUI.XML.app_map as app_map
        app_map_instance = app_map.AppMap(self.app_map_xml)
        desktop_element = app_map_instance.get_UI_element_by_name("desktop.desktop")
        self.assertTrue(desktop_element)
        wmplayer_element = app_map_instance.get_UI_element_by_name("wmplayer_Window")
        self.assertTrue(wmplayer_element)
        play_button_element = app_map_instance.get_UI_element_by_name("wmplayer_Window.TransportSubview_Group.Play_Pause_Button")
        self.assertIs(play_button_element, app_map_instance.wmplayer_Window.TransportSubview_Group.Play_Pause_Button)


