from datetime import datetime
import pandas as pd


def buildDataBase(sessionsData):
    """
        return df with sessions belonging to same object merged

        Input : df = helpers_pcap.sessionsDataExtractor()
        Ouput : pd.df

    """
    data = []

    for sensorID in sessionsData['SensorID'].unique():
        sensorData = sessionsData[sessionsData['SensorID'] == sensorID]

        sessionDurationMean = (
            sensorData['EndTime'] - sensorData['StartTime']).dt.total_seconds().mean()
        sessionBytesMean = sensorData['Bytes'].mean().astype(int)

        timeBetween2Sessions = sensorData['StartTime'].diff(
        ).dt.total_seconds()

        sleepTimeMean = timeBetween2Sessions.mean(
        ) if pd.notna(timeBetween2Sessions.mean()) else 1800
        sleepTimeVariance = timeBetween2Sessions.var(
        ) if pd.notna(timeBetween2Sessions.var()) else 0

        """
            REMY insert your code here !!! <3

            print(timeBetween2sessions)
            
            sleepTimeEntropy = function_entropy(timeBetween2sessions)

            definir la function function_entropy plus haut

            ajouter sleeptimeEntropy avec data.append()
            ajouter une colonneEntropy au dataframe

            peut-être vaut il mieux renvoyer un float sur [0;1] pour un meilleur apprentissage       
        
        
        """

        # si il a aussi un mode diurne en fonctions des heures d'activation (night, dayNnight) ou bien bool sur diurne
        # regarder les dongle ports

        data.append([sensorID, sessionDurationMean, sessionBytesMean,
                    sleepTimeMean, sleepTimeVariance])

    db = pd.DataFrame(data, columns=['SensorID', 'SessionDurationMean',
                                     'SessionBytesMean', 'SleepTimeMean', 'SleepTimeVariance'])

    return(db)
