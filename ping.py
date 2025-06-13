# Esto es para el coso de ping
# Timeout para que se pierdan algunos: 0.00000000000000000000001
from scapy.all import IP, TCP, Ether, sr1, UDP, DNS, ICMP, sr
import time
import statistics

def enviar_paquete(direccion):
    p = (IP(dst=direccion)/ICMP())
    envio = time.time()
    ans, unans = sr(p, timeout=0.00000000000000000000001, verbose=False)
    respuesta = time.time()

    if ans:
        rcvd = "Recibido"
        rtt = (respuesta - envio) * 1000
        ttl = ans[0][1].ttl
        len = ans[0][1].len
        return [rcvd, rtt, ttl, len]

    else:
        return [0, 0, 0, 0]

def enviar_varios_paquetes(cantidad, direccion):
    recibidos = 0
    total_rtts = []

    for i in range(cantidad):
        respuesta = enviar_paquete(direccion)
        print("Paquete numero " + str(i))
        if respuesta[0] == "Recibido":
            recibidos += 1
            total_rtts.append(respuesta[1])
            print("\tRTT: " + str(respuesta[1]))
            print("\tTTL: " + str(respuesta[2]))
            print("\tLongitud: " + str(respuesta[3]))
        else:
            print("\tSe perdio el paquete [x]")

    print("Estadisticas:")
    print("\tEnviados: " + str(cantidad))
    print("\tRecibidos: " + str(recibidos))
    print("\tPerdidos: " + str(cantidad-recibidos))
    print("\tPorcentaje perdidos: " + str(((cantidad-recibidos)/cantidad)*100) + "%")
    print("\tPromedio RTT: " + str(statistics.mean(total_rtts)))
    print("\tRTT Maximo: " +str(max(total_rtts)))
    print("\tRTT Minimo: " +str(min(total_rtts)))
    print("\tDesvio estandar del RTT promedio: " +str(statistics.stdev(total_rtts)))


enviar_varios_paquetes(20, "8.8.8.8")