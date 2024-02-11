import librosa
import numpy as np
import mysql.connector
keysAre = []

mydata = mysql.connector.connect(
    host="localhost",
    username="root",
    password="aakash",
)
cmd = mydata.cursor()
def closest(lst, K):
     
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

def compare(fre):
    cmd.execute("use keyfrequency")
    cmman = "select frq from pinao"

    cmd.execute(cmman)
    result = cmd.fetchall()
    data = result
    cvalue = closest(data, fre)

    cmd.execute("select KeyName from pinao where frq like %s",cvalue)
    KEYK = cmd.fetchall()
            
            
    keysAre.append(KEYK)

    return KEYK


    

        





def analyze_frequency(frame, sample_rate):
    frequencies = np.fft.fft(frame)
    freq_magnitude = np.abs(frequencies)
    frequency = np.argmax(freq_magnitude) * sample_rate / len(frame)

    return frequency


audio_file_path = "M1.MP3"


audio_data, sample_rate = librosa.load(audio_file_path, sr=None, mono=True)

analysis_duration = 1.0


frames_per_analysis = int(analysis_duration * sample_rate)


for i in range(0, len(audio_data), frames_per_analysis):
    audio_chunk = audio_data[i:i+frames_per_analysis]

    
    if len(audio_chunk) < frames_per_analysis:
        break

    
    frequency = analyze_frequency(audio_chunk, sample_rate)
    noets = compare(frequency)
    


    print(f"KeyNots for piano time: {i//frames_per_analysis + 1} Key : {noets} Hz")


# print("end reaults are : ",keysAre)
