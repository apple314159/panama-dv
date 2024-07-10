panama-dv
=========

Program to calculate the DV for the given RUC for Panama.
See [ALGORITMO PARA EL CALCULO DEL DIGITO VERIFICADOR DE LA RUC Y RECIBO](https://www.anip.gob.pa/documentos/DV_RUC.pdf)

Usage:
```python
  #!/usr/bin/env python
  import sys
  import argparse
  import ruc

  parser = argparse.ArgumentParser(description='DV calculator')
  parser.add_argument('ruc', type=str)
  args = parser.parse_args()

  dv = ruc.calculateDV(args.ruc)
  if len(dv) == 0:
    print("Unable to calculate RUC!")
    sys.exit(1)

  print(dv)
```
