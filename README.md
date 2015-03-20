panama-dv
=========

Program to calculate the DV for the given RUC for Panama.
See [ALGORITMO PARA EL CALCULO DEL DIGITO VERIFICADOR DE LA RUC Y RECIBO](https://www.anip.gob.pa/documentos/DV_RUC.pdf)

Usage:
```python
  #!/usr/bin/env python2
  import sys
  import argparse
  import ruc

  parser = argparse.ArgumentParser(description='DV calculator')
  parser.add_argument('ruc', type=str)
  args = parser.parse_args()

  dv = calculateDV(args.ruc)
  if len(dv) == 0:
    sys.exit(1)

  print dv
```
