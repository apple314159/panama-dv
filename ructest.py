#!/usr/bin/env python2

import unittest
import ruc

class DVerrorTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(ruc.calculateDV(''),'')
        self.assertEqual(ruc.calculateDV('E'),'')

    def test2(self):
        self.assertEqual(ruc.calculateDV('61302-14-123411'),'22')
        self.assertEqual(ruc.calculateDV('1102-85-117211'),'95')
        self.assertEqual(ruc.calculateDV('2486589-1-816994'),'62')
        self.assertEqual(ruc.calculateDV('1830234-1-710357'),'82')

        self.assertEqual(ruc.calculateDV('41369-85-283456'),'73')

    def test3(self):
        self.assertEqual(ruc.calculateDV('64296-75-357434'),'00')
        self.assertEqual(ruc.calculateDV('203141-1-17214'),'60')
        self.assertEqual(ruc.calculateDV('1075137-1-553125'),'18')
        self.assertEqual(ruc.calculateDV('212871-1-263'),'37')
        self.assertEqual(ruc.calculateDV('557-554-101637'),'61')
        self.assertEqual(ruc.calculateDV('224080-45-201122'),'65')

if __name__ == "__main__":
    unittest.main()
