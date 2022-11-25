import pandas as pd
from scapy.all import *


def loadPcap(path):
    return(rdpcap(path))


def createTagsDictionnary():
    """
        create a dictionnary with data from sensors_tags.txt
    """
    file = open('Builder/sensors_tags.txt', 'r')
    res = {}
    for line in file.readlines():
        name, sensor_id, tags, _ = line.split(" : ")
        res[(name, int(sensor_id))] = tags.split(" , ")
    return(res)


def findTags(string, balises_dic):
    """
        search for tag in string expression
        return the id of the sensor linked to the tag found

        Output: set of id, 'None' if set is empty
    """
    res = []
    for key, values in balises_dic.items():
        res += [key[1] for value in values if value in string]

    if len(set(res)) > 1:
        raise ValueError(
            "une frame a plusieurs labels! \n le contenu de la frame: " + string)

    return(int(res[0]) if res else None)


def filterHTTPPackets(packets):
    """
        return packets with source_port == 80 or destination_port == 80
    """
    return(packets.filter(lambda x: x.haslayer(IP) and (x[IP].dport == 80 or x[IP].sport == 80)))


def mergeUpDownSessions(df):
    """
        change sessionID (A > B) and (B > A) into (A <> B)
        to be used this way :
        >>> packetsData = packetsDataExtractor(packets)
        >>> updatedpacketsData = mergeUpDownSessions(packetsDAta)

        Input: pandas.dataframe
        Ouput: pandas.dataframe
    """
    sessions = df['Session'].unique()
    dict = {}
    for session in sessions:
        protocol, src, sign, dest = session.split(' ')
        new_key = protocol + ' ' + dest + ' <> ' + src
        if new_key in dict.values():
            dict[session] = new_key
        else:
            dict[session] = protocol + ' ' + src + ' <> ' + dest
    df.Session = df.apply((lambda y: dict[y.Session]), axis=1)

    return(df)
