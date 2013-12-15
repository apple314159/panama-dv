#!/usr/bin/env python2
#

import sys
import argparse

_arrval = {
        '00': 0,
        '10': 1,
        '11': 2,
        '12': 3,
        '13': 4,
        '14': 5,
        '15': 6,
        '16': 7,
        '17': 8,
        '18': 9,
        '19': 1,
        '20': 2,
        '21': 3,
        '22': 4,
        '23': 7,
        '24': 8,
        '25': 9,
        '26': 2,
        '27': 3,
        '28': 4,
        '29': 5,
        '30': 6,
        '31': 7,
        '32': 8,
        '33': 9,
        '34': 1,
        '35': 2,
        '36': 3,
        '37': 4,
        '38': 5,
        '39': 6,
        '40': 7,
        '41': 8,
        '42': 9,
        '43': 1,
        '44': 2,
        '45': 3,
        '46': 4,
        '47': 5,
        '48': 6,
        '49': 7
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
    r = 11 - (nsuma % 11)
    if r > 1:  return r
    return 0

def calculateDV(ruc):
    rs = ruc.split('-')
    if len(rs) != 3:
        return ''

    ructb = '0'*(10-len(rs[0])) + rs[0] + '0'*(4-len(rs[1])) + rs[1] + '0'*(6-len(rs[2])) + rs[2]
    #print ructb

    if ructb[7] != 'N':
        # RUC juridico
        pass

    # sw es true si es ruc antiguo
    sw = ructb[3] == '0' and ructb[4] == '0' and ructb[5] < '5'

    # rutina de referencia cruzada
    t = _arrval.get(ructb[5:7])
    if sw and t:
        ructb = ructb[:5] + '0' + chr(ord('0')+t)+ ructb[7:]

    #print ructb

    dv1 = _digitDV(sw, ructb)
    #print dv1
    dv2 = _digitDV(sw, ructb+chr(48+dv1))

    ret =  chr(48+dv1) + chr(48+dv2)
    #print ret
    return ret

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='DV calculator')
    parser.add_argument('ruc', type=str)
    args = parser.parse_args()

    dv = calculateDV(args.ruc)
    if len(dv) == 0:
        sys.exit(1)
    print dv
