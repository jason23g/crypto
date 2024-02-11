from Crypto.Util.number import *



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



p = 9739 

Xx = 5274
Xy = 2841

Yx = 8669
Yy = 740

a = 497

Rx,Ry = point_addition(a,Xx,Xy,Yx,Yy,p)

print("X+X=(",Rx,",",Ry,")")

Rx,Ry = point_addition(a,Xx,Xy,Xx,Xy,p)

print("X+X=(",Rx,",",Ry,")")



Px = 493
Py = 5564

Qx = 1539
Qy = 4742

Rx = 4403
Ry = 5202

PPx,PPy = point_addition(a,Px,Py,Px,Py,p)

QRx,QRy = point_addition(a,Qx,Qy,Rx,Ry,p)

Sx,Sy	= point_addition(a,PPx,PPy,QRx,QRy,p)


print("S=P+P+Q+R=(",Sx,",",Sy,")")


assert pow(Sy,2,p),(pow(Sx,3)+497*Sx+1768)%p

print("crypto{",Sx,",",Sy,"}")







