#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
import ruc

class DVTest(unittest.TestCase):
    def test_errors(self):
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

        #self.assertEqual(ruc.calculateDV('212871-1-263'),'37')
        #self.assertEqual(ruc.calculateDV('557-554-101637'),'61')
        #self.assertEqual(ruc.calculateDV('224080-4520-1122'),'65')

class FormatoRUC_2005Test(unittest.TestCase):
    def test_I(self):
        "Formato para Cédulas (Personas Naturales)"
        # Panam
        self.assertEqual(ruc.calculateDV('8-442-445'), '08')
        self.assertEqual(ruc.calculateDV('PE-10-442'),'50')
        self.assertEqual(ruc.calculateDV('N-45-832'),'58')
        self.assertEqual(ruc.calculateDV('E-12-342'),'10')
        self.assertEqual(ruc.calculateDV('1AV-432-658'),'96')
        self.assertEqual(ruc.calculateDV('4PI-234-123'),'96')

    def test_II(self):
        "Formato para Pasaportes (Persona Natural Extranjera)"
        self.assertEqual(ruc.calculateDV('PAS1311723564'),'')

    def test_III(self):
        "Formato para RUC (Persona Jurídica)"
        self.assertEqual(ruc.calculateDV('11947-1027-0229562'),'71')
        self.assertEqual(ruc.calculateDV('11947-1-0229562'),'42')

    def test_IV(self):
        "Formato para Jurídico NT"
        self.assertEqual(ruc.calculateDV(''),'')
        self.assertEqual(ruc.calculateDV(''),'')

if __name__ == "__main__":
    unittest.main()
