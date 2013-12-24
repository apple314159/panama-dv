#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Reference:
# https://www.anip.gob.pa/documentos/DV_RUC.pdf

_arrval = {
        '00': '00',
        '10': '01',
        '11': '02',
        '12': '03',
        '13': '04',
        '14': '05',
        '15': '06',
        '16': '07',
        '17': '08',
        '18': '09',
        '19': '01',
        '20': '02',
        '21': '03',
        '22': '04',
        '23': '07',
        '24': '08',
        '25': '09',
        '26': '02',
        '27': '03',
        '28': '04',
        '29': '05',
        '30': '06',
        '31': '07',
        '32': '08',
        '33': '09',
        '34': '01',
        '35': '02',
        '36': '03',
        '37': '04',
        '38': '05',
        '39': '06',
        '40': '07',
        '41': '08',
        '42': '09',
        '43': '01',
        '44': '02',
        '45': '03',
        '46': '04',
        '47': '05',
        '48': '06',
        '49': '07'
        }

def _digitDV(sw, ructb):
    # rutina calcula dv
    j = 2
    nsuma = 0

    for c in reversed(ructb):
        if sw and j == 12:
            sw = False
            j -= 1

        nsuma += j*(ord(c)-ord('0'))
        j += 1
    r = nsuma % 11
    if r > 1:  return 11 - r
    return 0

def calculateDV(ruc):
    rs = ruc.split('-')
    if (len(rs) == 4 and RS[1] != 'NT') or len(rs) < 3 or len(rs) > 5:
        return ''

    sw = False

    # TODO: NT
    if ruc[0] == 'E':
        ructb = '0'*(4-len(rs[1])) + '0000005' + '00' + '50' + '0'*(3-len(rs[1])) + rs[1] + '0'*(5-len(rs[2])) + rs[2]

    elif rs[1] == 'NT':
        ructb = '0'*(4-len(rs[1])) + '0000005' + '00'*(2-len(rs[0][:-2])) + rs[0][:-2] + '43' + '0'*(3-len(rs[2])) + rs[2] + '0'*(5-len(rs[3])) + rs[3]

    elif rs[0][-2:] == 'AV':
        ructb = '0'*(4-len(rs[1])) + '0000005' + '00'*(2-len(rs[0][:-2])) + rs[0][:-2] + '15' + '0'*(3-len(rs[1])) + rs[1] + '0'*(5-len(rs[2])) + rs[2]

    elif rs[0][-2:] == 'PI':
        ructb = '0'*(4-len(rs[1])) + '0000005' + '00'*(2-len(rs[0][:-2])) + rs[0][:-2] + '79' + '0'*(3-len(rs[1])) + rs[1] + '0'*(5-len(rs[2])) + rs[2]

    elif rs[0] == 'PE':
        ructb = '0'*(4-len(rs[1])) + '0000005' + '00' + '75' + '0'*(3-len(rs[1])) + rs[1] + '0'*(5-len(rs[2])) + rs[2]

    elif ruc[0] == 'N':
        ructb = '0'*(4-len(rs[1])) + '0000005' + '00' + '40' + '0'*(3-len(rs[1])) + rs[1] + '0'*(5-len(rs[2])) + rs[2]

    elif 0 < len(rs[0]) <= 2:
        ructb = '0'*(4-len(rs[1])) + '0000005' + '0'*(2-len(rs[0])) + rs[0] + '00' + '0'*(3-len(rs[1])) + rs[1] + '0'*(5-len(rs[2])) + rs[2]

    else: # RUC juridico
        ructb = '0'*(10-len(rs[0])) + rs[0] + '0'*(4-len(rs[1])) + rs[1] + '0'*(6-len(rs[2])) + rs[2]
        #print ructb

        # sw es true si es ruc antiguo
        sw = ructb[3] == '0' and ructb[4] == '0' and ructb[5] < '5'

    # rutina de referencia cruzada
    if sw:
        ructb = ructb[:5] + _arrval.get(ructb[5:7],ructb[5:7]) + ructb[7:]

    #print ructb

    dv1 = _digitDV(sw, ructb)
    #print dv1
    dv2 = _digitDV(sw, ructb+chr(48+dv1))

    ret =  chr(48+dv1) + chr(48+dv2)
    #print ret
    return ret

if __name__ == "__main__":
    import sys
    import argparse

    parser = argparse.ArgumentParser(description='DV calculator')
    parser.add_argument('ruc', type=str)
    args = parser.parse_args()

    dv = calculateDV(args.ruc)
    if len(dv) == 0:
        sys.exit(1)
    print dv
