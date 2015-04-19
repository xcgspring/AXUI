
import os
from time import sleep

import unittest
from appium import webdriver

import AXUI

config_file = "appium.cfg"
app_map = "ApiDemos.xml"

AXUI.Config(config_file)
appmap = AXUI.AppMap(app_map)

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['app'] = PATH('ApiDemos-debug.apk')
        appmap.driver.start(command_executor='http://localhost:4723/wd/hub', desired_capabilities=desired_caps)

    def tearDown(self):
        # end the session
        appmap.driver.stop()

    def test_find_elements(self):
        appmap.driver.Graphic.Mouse.left_click()
        AXUI.assertIsValid(appmap.driver.Arcs)
        
        appmap.driver.BrowserPattern.back()
        AXUI.assertIsValid(appmap.driver.App)

        els = appmap.driver.clickable_items
        self.assertGreaterEqual(14, len(els))
        AXUI.assertIsValid(appmap.driver.Title)

    @unittest.skip("")
    def test_simple_actions(self):
        appmap.driver.Graphic.Mouse.left_click()
        appmap.driver.Arcs.Mouse.left_click()

        AXUI.assertIsValid(appmap.driver.Arcs_title)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)