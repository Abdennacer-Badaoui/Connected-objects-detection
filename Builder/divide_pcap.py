from helpers_pcap import *
import sys
from scapy.all import *
from datetime import *

if __name__ == '__main__':
    if len(sys.argv) != 2:
        pcapInName = str(
            input("Saisir un unique nom de fichier pcap à diviser : "))
    else:
        pcapInName = (sys.argv[1])

    packets = loadPcap(pcapInName)

    start = datetime.fromtimestamp(int(packets[0].time))
    file_nb = 0
    print(f"creating subfile n°0 ...")
    pcapOutName = f"Captures/{pcapInName}-{file_nb}.pcap"

    for pkt in packets:
        if (datetime.fromtimestamp(int(pkt.time)) > start + timedelta(minutes=30)):
            file_nb += 1
            print(f"creating subfile n°{file_nb} ...")
            pcapOutName = f"Captures/{pcapInName}-{file_nb}.pcap"
            start = datetime.fromtimestamp(int(pkt.time))

        wrpcap(pcapOutName, pkt, append=True)

    print("done!")
