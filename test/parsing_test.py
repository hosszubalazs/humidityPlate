import unittest
import src.HumiPlate as humi

class TestParsing(unittest.TestCase):

    def testInt(self):
        parsed = humi.parseTemp(5)
        expected =  '5.0*C'
        self.assertEqual(expected, parsed)

    def testReal(self):
        parsed = humi.parseTemp(5.1)
        expected =  '5.1*C'
        self.assertEqual(expected, parsed)

    def testRealVerbose(self):
        parsed = humi.parseTemp(5.234)
        expected =  '5.2*C'
        self.assertEqual(expected, parsed)

    def testRealMultiDigits(self):
        parsed = humi.parseTemp(125.2)
        expected =  '125.2*C'
        self.assertEqual(expected, parsed)

    def testIntNegative(self):
        parsed = humi.parseTemp(-10)
        expected =  '-10.0*C'
        self.assertEqual(expected, parsed)

    def testIntHumidity(self):
        parsed = humi.parseHumidity(5)
        expected =  '5.0*%'
        self.assertEqual(expected, parsed)

def main():
    unittest.main()

if __name__ == '__main__':
    unittest.main()