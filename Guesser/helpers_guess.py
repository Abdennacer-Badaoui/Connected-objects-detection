from Builder.helpers_pcap import *
from Builder.helpers_extractor import *
from Builder.helpers_db import *


def build_guess_db(path):

    packets = loadPcap(path)
    httpPackets = filterHTTPPackets(packets)
    tagsDictionnary = createTagsDictionnary()
    packetsData = packetsDataExtractor(httpPackets, tagsDictionnary)
    packetsData2 = mergeUpDownSessions(packetsData)
    sessionsData = sessionsDataExtractor(packetsData2)

    # la c'est juste parce que j'ai pas les bonnes captures
    sessionsData = sessionsData.loc[sessionsData['SensorID'].isin([
                                                                  '4.0', '6.0']), :]

    sessionsData['SensorID'] = '?'
    x_guess = buildDataBase(sessionsData)
    x_guess = x_guess.loc[:, x_guess.columns != 'SensorID']

    return(x_guess)
