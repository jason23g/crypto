from Crypto.Util.number import *
from math import floor
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad



def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

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



iv = "cd9da9f1c60925922377ea952afc212c"
ciphertext = "febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8"

Qx = 4726
p = 9739

nB = 6534

y2 = (pow(Qx,3)+497*Qx+1768)%p

a = 497


print("y^2  :",y2," x^2 : ",pow(Qx,2,p))


(Qy_pos,Qy_neg) = toneli_shanks(y2,p)

print("y: ",Qy_pos,",",Qy_neg)


Sx,Sy = scalar_multiplication(a,nB,Qx,Qy_pos,p)


print(f"{Sx,Sy}")


print(decrypt_flag(Sx,iv,ciphertext))
