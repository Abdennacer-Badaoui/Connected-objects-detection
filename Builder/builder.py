from Builder.helpers_db import *
from Builder.helpers_pcap import *
from Builder.helpers_extractor import *
import glob


def build(path, dest):

    name = path.split(".")[0].split("/")[-1].split("\\")[-1]

    packets = loadPcap(path)
    httpPackets = filterHTTPPackets(packets)
    tagsDictionnary = createTagsDictionnary()
    packetsData = packetsDataExtractor(httpPackets, tagsDictionnary)

    packetsData2 = mergeUpDownSessions(packetsData)
    sessionsData = sessionsDataExtractor(packetsData2)

    db = buildDataBase(sessionsData)
    db.to_csv(f"{dest}{name}-iot-db.csv", index=False)

    return True


def merge():
    frames = []
    for db in glob.glob("DB/*.csv"):
        df = pd.read_csv(db)
        frames += [df]
    main_df = pd.concat(frames, ignore_index=True)

    main_df.to_csv(f"Learner/TrainingDB/trainingDB.csv", index=False)

    return True
