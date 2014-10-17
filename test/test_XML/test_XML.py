
import unittest

class TestAppMap(unittest.TestCase):
    def setUp(self):
        self.app_map_xml = "windows_media_player.xml"
        
    def test_app_map_create(self):
        import AXUI.XML.app_map as app_map
        app_map_instance = app_map.AppMap(self.app_map_xml)
        assertTrue(app_map_instance, "app map create instance fail")
        
    def test_app_map_singleton(self):
        import AXUI.XML.app_map as app_map
        app_map_instance = app_map.AppMap(self.app_map_xml)
        app_map_instance2 = app_map.AppMap(self.app_map_xml)
        self.assertIs(app_map_instance, app_map_instance2, "app map should have one instance for same xml")
        
    def test_get_element(self):
        import AXUI.XML.app_map as app_map
        app_map_instance = app_map.AppMap(self.app_map_xml)
        desktop_element = app_map_instance.get_element_by_name("desktop.desktop")
        assertTrue(desktop_element)
        wmplayer_element = app_map_instance.get_element_by_name("wmplayer")
        assertTrue(wmplayer_element)
        play_button_element = app_map_instance.get_element_by_name("library_window.transport_button_group.play")
        assertTrue(play_button_element)
        assertTrue(app_map_instance.library_window.transport_button_group.play)

