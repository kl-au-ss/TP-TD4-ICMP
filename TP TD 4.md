# Ejercicios

## 1. Investigar sobre el protocolo ICMP y responder las siguientes preguntas

### a. ¿Cuál es la función del protocolo ICMP?

El protocolo ICMP es utilizado para la comunicacion de informacion sobre la capa de red entre routers y hosts. Tiene varios usos, pero el mas comun es el reportaje de errores. Los mensajes ICMP son transportados dentro de datagramas IP, por lo que se podria decir que se encuentra en un nivel mas arriba que IP. Sus mensajes contienen el header y los primeros 8 bytes del datagrama IP que causo que el mensaje sea generado. Tienen un campo de tipo y de codigo.

### b. Investigar sobre los tipos de mensaje ICMP que existen y sus códigos. ¿Qué tipos de mensaje ICMP se utilizan en el comando ping y cómo funciona el proceso?

El tipo de mensaje ICMP utilizado en el comando ping es un mensaje tipo 8 con codigo 0. Funciona de forma que una vez que el host de destino recibe el mensaje, este mismo responde enviando un mensaje ICMP tipo 0 con codigo 0.

### c. ¿Qué es el programa Traceroute? Describa cómo se puede implementar Traceroute usando mensajes ICMP. (Traceroute utiliza mensajes ICMP del tipo Time Exceeded)

El programa Traceroute tiene como funcion trazar la ruta entre un host y otro host. Esto lo hace implementando mensajes ICMP. Envia varios datagramas IP que incluyen segmentos UDP con un numero de puerto poco probable. Cada vez que el host origen envia un datagrama, comienza un timer. El TTL de cada uno de estos datagramas va incrementando, es decir, el primero tiene un TTL de 1, el segundo de 2 y asi. Cuando uno de estos datagramas llega a un router, este lo descarta ya que nota la terminacion del TTL, al mismo tiempo que envia un mensaje ICMP de tipo 11 con codigo 0 de advertencia, el cual incluye la direccion IP del router y su nombre. Una vez que este mensaje llega al host de origen, este calcula el RTT con el timer junto a la informacion recibida con este ultimo mensaje. Como el TTL aumenta con cada datagrama enviado, uno de estos va a llegar al host destino, quien, debido al numero de puerto indicado, enviara un mensaje ICMP de tipo 3 codigo 3 hacia el origen indicando que el puerto no es alcanzable. Al recibir el mensaje, el host de origen para de enviar paquetes.