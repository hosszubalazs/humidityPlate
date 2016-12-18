import unittest
import src.LCDHelper as LCDH
import src.constants as c

class TestHeatMap(unittest.TestCase):

    def testCOld(self):
        self.assertEqual(c.LCD_COLD_BLUE, LCDH.map_heat_to_bgcolor(17.9))

    def testNormalLower(self):
        self.assertEqual(c.LCD_NICE_GREEN, LCDH.map_heat_to_bgcolor(18))

    def testNormalUpprt(self):
        self.assertEqual(c.LCD_NICE_GREEN, LCDH.map_heat_to_bgcolor(22.9))

    def testHotLower(self):
        self.assertEqual(c.LCD_HOT_RED, LCDH.map_heat_to_bgcolor(23))

def main():
    unittest.main()

if __name__ == '__main__':
    unittest.main()