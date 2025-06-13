# Esto es para el coso de ping
from scapy.all import IP, TCP, Ether, sr1, UDP, DNS, ICMP, sr
import time
import statistics

# def paquete():
#     p = sr(IP(dst="www.slashdot.org")/ICMP(), timeout=3)
#     return p

# print(paquete())

# p = sr1(IP(dst="www.slashdot.org")/ICMP()/"XXXXXXXXXXX")
# print(p)
# print(p.show())

# ans, unans = sr(IP(dst="192.168.1.0/24")/ICMP(), timeout=3)
# print(ans, unans)

# p = sr(IP(dst="www.slashdot.org")/ICMP(), timeout=3)

p = IP(dst="www.slashdot.org")/ICMP()
envio = time.time()
ans, unans = sr(p)
respuesta = time.time()

# if ans:
#     rtt = (respuesta - envio) * 1000
#     print("Respuestas recibidas: " + str(len(ans)) + "\nTiempo: " + str(rtt))

print(ans.sprintf())
# print(ans.summary(lambda s,r: r.sprintf("%IP.src% is alive") ))