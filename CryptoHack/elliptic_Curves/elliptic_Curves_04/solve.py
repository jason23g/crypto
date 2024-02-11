from Crypto.Util.number import *
from math import floor

from hashlib import sha1

def point_addition(a,Px,Py,Qx,Qy,p):

	if Px == 0 and Py == 0 :
		Rx = Qx
		Ry = Qy
	elif Qx == 0 and Qy == 0 :
		Rx = Px
		Ry = Py
	elif Px == Qx and Py == -Qy :
		Rx = 0
		Ry = 0
	else :
		if Px != Qx or Py != Qy :
			lamda = (Qy - Py )*(inverse(Qx-Px,p))
		else :
			lamda = (3*pow(Px,2) + a)*(inverse(2*Py,p))

		Rx = pow(lamda,2) - Px - Qx
		Ry = lamda*(Px-Rx) - Py

	return Rx%p,Ry%p


def scalar_multiplication(a,n,Px,Py,p):

	Qx = Px
	Qy = Py

	Rx = 0
	Ry = 0

	while n > 0 :

		if n%2 == 1 :

			Rx,Ry = point_addition(a,Rx,Ry,Qx,Qy,p)

		Qx,Qy = point_addition(a,Qx,Qy,Qx,Qy,p)

		n = floor(n/2)




	return Rx%p,Ry%p




QA = (815, 3190)

QAx = 815
QAy = 3190

a = 497

p = 9739

nB = 1829


Sx,Sy = scalar_multiplication(a,nB,QAx,QAy,p)


secret = str(Sx).encode()

print(secret)

print("crypto{",sha1(secret).hexdigest(),"}")


