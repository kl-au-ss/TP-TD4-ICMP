# Esto es para el coso de ping
# Timeout para que se pierdan algunos: 0.00000000000000000000001
from scapy.all import IP, TCP, Ether, sr1, UDP, DNS, ICMP, sr
import time
import statistics

errores_tipo3 = {
    0: "Destination network unreachable",
    1: "Destination host unreachable",
    2: "Destination protocol unreachable",
    3: "Destination port unreachable",
    6: "Destination network unknown",
    7: "Destination host unknown"
}

def ping(direccion):
    p = (IP(dst=direccion)/ICMP())
    envio = time.time()
    ans, unans = sr(p, timeout=0.00000000000000000000001, verbose=False)
    respuesta = time.time()

    if ans:
        mensaje = ans[0][1].type, ans[0][1].code
        if mensaje[0] == 0:
            rcvd = True
            rtt = (respuesta - envio) * 1000
            ttl = ans[0][1].ttl
            len = ans[0][1].len
            return [rcvd, rtt, ttl, len, 0, 0]
        
        if mensaje[0] == 3:
            return [0,0,0,0,3,mensaje[1]]

    else:
        return [0, 0, 0, 0, 0, 0]

def enviar_varios_ping(cantidad, direccion):
    recibidos = 0
    total_rtts = []

    for i in range(cantidad):
        respuesta = ping(direccion)
        print("Paquete numero " + str(i))
        if respuesta[0] == True:
            if respuesta[4] == 0:
                recibidos += 1
                total_rtts.append(respuesta[1])
                print("\tRespuesta ICMP tipo " + str(respuesta[4]) + ", codigo " + str(respuesta[5]))
                print("\tRTT: " + str(respuesta[1]))
                print("\tTTL: " + str(respuesta[2]))
                print("\tLongitud: " + str(respuesta[3]))
            elif respuesta[4] == 3:
                print("Error: " + errores_tipo3[respuesta[5]])
        else:
            print("\tSe perdio el paquete [x]")

    print("Estadisticas:")
    print("\tEnviados: " + str(cantidad))
    print("\tRecibidos: " + str(recibidos))
    print("\tPerdidos: " + str(cantidad-recibidos))
    print("\tPorcentaje perdidos: " + str(((cantidad-recibidos)/cantidad)*100) + "%")
    if (len(total_rtts)>=1):
        print("\tPromedio RTT: " + str(statistics.mean(total_rtts)))
        print("\tRTT Maximo: " +str(max(total_rtts)))
        print("\tRTT Minimo: " +str(min(total_rtts)))
        if (len(total_rtts)>1):
            print("\tDesvio estandar del RTT promedio: " +str(statistics.stdev(total_rtts)))
    else:
        print("\tRTT no calculable")


enviar_varios_ping(80, "8.8.8.8")