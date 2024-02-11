from Crypto.Util.number import *

p = 9739

Px = 8045
Py = 6936

Qx = (Px)%p
Qy = (-Py)%p

print(f"crypto{Qx,Qy}")