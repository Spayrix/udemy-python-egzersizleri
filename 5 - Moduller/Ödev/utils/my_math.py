"""
Math modülünde kullandığınız fonksiyonları kendiniz de ayrı bir modüle (Python dosyasına) yazmaya çalışın
ve bu yazdığınız modülü kullanarak gelişmiş bir hesap makinesi yazın.
"""
import math

def karekok(x):
    return math.sqrt(x)

def us_alma(x,y):
    return math.pow(x,y)

def log_alma(x,y):
    return math.log(x,y)

def faktoriyel(x):
    return math.factorial(x)

def EBOB(x,y):
    return math.gcd(x,y)

def yuvarla_asagi(x):
    return math.floor(x)

def yuvarla_yukari(x):
    return math.ceil(x)

def derece_to_radyan(x):
    return math.radians(x)

def radyan_to_derece(x):
    return math.degrees(x)