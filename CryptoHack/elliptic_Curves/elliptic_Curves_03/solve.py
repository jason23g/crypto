from Crypto.Util.number import *
from math import floor

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




Xx = 5323
Xy = 5438

p = 9739

n = 1337
a = 497

Rx,Ry = scalar_multiplication(a,n,Xx,Xy,p)

print("1337X=(",Rx,",",Ry,")")

Px = 2339
Py = 2213
n = 7863

Qx,Qy = scalar_multiplication(a,n,Px,Py,p)

print("7863P=(",Qx,",",Qy,")")

assert pow(Qy,2,p),(pow(Qx,3)+497*Qx+1768)%p

print("crypto{",Qx,",",Qy,"}")