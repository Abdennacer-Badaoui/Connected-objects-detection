import pandas as pd
from scapy.all import *
from Builder.helpers_pcap import findTags
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def packetsDataExtractor(packets, tagsDictionnary):
    """
        Extract main information from frames :
        session_id, time_stamp, port_src, port_dst, length, sensor

        Input: scapy.rdpcap (dictionnary)
        Output: pandas.dataframe (one line per frame)
    """

    pktSession = []
    pktBytes = []
    pktTimes = []
    pktPortsrc = []
    pktPortdest = []
    pktSensorID = []

    sessions = packets.sessions()

    for session_id, packetList in sessions.items():

        for pkt in packetList:

            # global info
            pktSession.append(session_id)
            pktBytes.append(pkt.len)
            pktTime = pd.Timestamp(
                float(pkt.time), unit='s', tz='Europe/Paris')
            pktTimes.append(pktTime)

            # TCP layer
            pktPortsrc.append(pkt[IP].sport)
            pktPortdest.append(pkt[IP].dport)

            # content
            pktSensorID.append(findTags(str(pkt), tagsDictionnary))

    session = pd.Series(pktSession).astype(str)
    bytes = pd.Series(pktBytes).astype(int)
    times = pd.to_datetime(pd.Series(pktTimes).astype(str),  errors='coerce')
    portSrc = pd.Series(pktPortsrc).astype(int)
    portDest = pd.Series(pktPortdest).astype(int)
    sensorID = pd.Series(pktSensorID).astype('str')

    df = pd.DataFrame({"Session": session, "Bytes": bytes, "Time": times,
                       "PortSrc": portSrc, "PortDest": portDest, "SensorID": sensorID})

    return(df)


def sessionsDataExtractor(packetsData):
    """
        Compute sessions data based on packets data :
        session_id, start_time, duration, port_src, port_dst, length, sensor

        Input: packets in pandas.DataFrame
        Output: pandas.dataframe (one line per session)
    """
    data = []

    for sessionId in packetsData['Session'].unique():
        pkts = packetsData[packetsData['Session'] == sessionId]
        bytes = pkts['Bytes'].sum()
        numberOfPackets = pkts.shape[0]
        startTime = pkts['Time'].min()
        endTime = pkts['Time'].max()
        donglePort = pkts['PortSrc'].max()
        sensorID = pkts['SensorID'].min()
        data.append([sessionId, bytes, numberOfPackets, startTime,
                    endTime, donglePort, sensorID])

    df = pd.DataFrame(data, columns=[
        'Session', 'Bytes', 'NumberOfPackets', 'StartTime', 'EndTime', 'DonglePort', 'SensorID'])

    return(df)
