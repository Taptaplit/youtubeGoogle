from pydub import AudioSegment
import math
import speech_recognition as sr
import os, shutil

r = sr.Recognizer()

class SplitWavAudioMubin():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = filename
        self.wholetext = ""
        
        self.audio = AudioSegment.from_wav(self.filepath)
        
        if not os.path.isdir('audioio'):
            os.mkdir('audioio')
    
    def get_duration(self):
        return self.audio.duration_seconds
    
    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '\\' + split_filename, format="wav")
        
    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 60)
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i+min_per_split, split_fn)
            print(str(i) + ' files out of ' + str(total_mins / min_per_split) + ' Finished!')
            
            split_fn = os.path.join(self.folder, f"{split_fn}")
            with sr.AudioFile(split_fn) as source:
                audio_listened = r.record(source)
                # try converting it to text
                try:
                    text = r.recognize_google(audio_listened)
                except sr.UnknownValueError as e:
                    print("Speech To Text Error! >>", str(e ))
                else:
                    text = f"{text.capitalize()}. "
                    self.wholetext += text
            
            if i == total_mins - min_per_split:
                print('All splited successfully')
        # return the text for all chunks detected
        shutil.rmtree('audioio') 
        return self.wholetext
                

