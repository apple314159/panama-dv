===============================
panamadv
===============================

.. image:: https://img.shields.io/travis/Vauxoo/panamadv.svg
        :target: https://travis-ci.org/Vauxoo/panamadv

.. image:: https://img.shields.io/pypi/v/panamadv.svg
        :target: https://pypi.python.org/pypi/panamadv


Program to calculate the DV for the given RUC for Panama.

* Free software: BSD license
* Documentation: https://panamadv.readthedocs.org.

Features
--------

See [ALGORITMO PARA EL CALCULO DEL DIGITO VERIFICADOR DE LA RUC Y RECIBO](https://www.anip.gob.pa/documentos/DV_RUC.pdf)

Usage:

.. code:: python

    #!/usr/bin/env python2
    import sys
    import argparse
    from panamadv import ruc

    parser = argparse.ArgumentParser(description='DV calculator')
    parser.add_argument('ruc', type=str)
    args = parser.parse_args()

    dv = ruc.calculateDV(args.ruc)
    if len(dv) == 0:
        print "Unable to calculate RUC!"
        sys.exit(1)

    print dv

