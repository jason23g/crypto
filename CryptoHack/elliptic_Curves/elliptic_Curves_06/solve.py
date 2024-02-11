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


def montgomery_addition(Px,Py,Qx,Qy,A,B,p):

	'''
	α = (y2 - y1) / (x2 - x1 )
	x3 = Bα2 - A - x1 - x2
	y3 = α(x1 - x3) - y1
	'''
	if Px != Qx or Py != Qy :
		a = ((Qy-Py)*inverse(Qx-Px,p))

		Rx = (B*pow(a,2)-A-Px-Qx)
		Ry = (a*(Px-Rx)-Py)

	else : 
		print("Strange")
		Rx = 0
		Ry = 0


	return Rx%p,Ry%p


def montgomery_double_formula(Px,Py,A,B,p):

	'''
	α = (3x21 + 2Ax1 + 1) / (2By1)
	x3 = Bα2 - A - 2x1
	y3 = α(x1 - x3) - y1
	'''

	a = ((3*pow(Px,2) + 2*A*Px+1)*inverse(2*B*Py,p))
	Rx = (B*pow(a,2) -A -2*Px)
	Ry = (a*(Px-Rx)-Py)


	return Rx%p,Ry%p


def montgomery_algorithm(Px,Py,k,A,B,p):

	R0x = Px
	R0y = Py
	R1x,R1y = montgomery_double_formula(Px,Py,A,B,p)

	I = bin(k)
	print(I)
	k_len = len(I)


	for i in range(k_len-2, 1, -1):

		

		if I[i] == '0' :

			'''
		 	Set (R0, R1) to ([2]R0, R0 + R1)
			'''

			R0x,R0y = montgomery_double_formula(R0x,R0y,A,B,p)
			R1x,R1y = montgomery_addition(R0x,R0y,R1x,R1y,A,B,p)

		else :

			'''
			Set (R0, R1) to (R0 + R1, [2]R1)
			'''

			R0x,R0y = montgomery_addition(R0x,R0y,R1x,R1y,A,B,p)
			R1x,R1y = montgomery_double_formula(R1x,R1y,A,B,p)




	return R0x,R0y


def toneli_shanks(a,p):
 legedre_symbol = pow(a,((p-1)//2),p)

 if legedre_symbol == 1 :

        # p -1 = q * (2^s)
        q = p -1
        s = 0
        while q%2 == 0:

                q //= 2
                s = s+1

        if s == 1:
                return (pow(a,(p+1)//4,p),-pow(a,(p+1)//4,p)) 

        z = 2

        for x in range(2,p-1):
                if pow(x,((p-1)//2),p) == p-1 :
                        z = x
                        break

        c = pow(z,q,p)

        r = pow(a,(q+1)//2,p) 
        t =  pow(a,q,p)
        m = s



        while (t-1)%p != 0:

                t2 = (t*t)%p

                i = 1

                for j in range(1,m):

                        if (t2 - 1)%p == 0:
                                i = j
                                break

                        t2 = (t2*t2)%p


                b = pow(c,1 << (m-i-1),p)
                r = (r*b)%p
                t = (t * pow(b,2) )%p
                c = pow(b,2,p)
                m = i

 return (r,p-r)

B = 1
A = 486662
p = pow(2,255) - 19


Gx = 9

Gy2 = (pow(Gx,3)+A*pow(Gx,2)+Gx)%p

(Gy_pos,Gy_neg) = toneli_shanks(Gy2,p)


print(f"{Gy2=}")
print("y: ",Gy_pos,",",Gy_neg)
print(f"{Gy_pos=}")

k = "1337c0decafe"
K = bytes_to_long(bytes.fromhex(k))

print(f"{K=}")

Qx,Qy = montgomery_algorithm(Gx,Gy_pos,K,A,B,p)

print(f"{Qx=},{Qy=}")