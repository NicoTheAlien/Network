from dhcp import dhcp
from Computer import Computer
from Switch import Switch
from SO import SO

sw1 = Switch("Switch1", "192.168.10.1")
d1 = dhcp("DHCP1", "192.168.10.100", "/24", "192.168.10.2", "/24", sw1.getgateway(), 10)
o1 = Computer("PC1", d1.getipPC(), d1.getmPC(), d1.getgateway(), "", 1000)
so1 = SO("Windows10", "6.6.6", "x64", "patatas fritas", "puede", 700)

sw1.anadirDipositivo(d1)
sw1.listadispositivos(o1)

