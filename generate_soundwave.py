import math
import wave
import struct


audio = []
sample_rate = 44100.0


## Function: generate silence
def append_silence(duration_milliseconds=500):
    num_samples = duration_milliseconds * (sample_rate / 1000.0)

    for x in range(int(num_samples)): 
        audio.append(0.0)

    return


## Function: generate sinewave sequence
def append_sinewave(
        freq=440.0, 
        duration_milliseconds=1000, 
        volume=1.0):

    global audio

    num_samples = duration_milliseconds * (sample_rate / 1000.0)

    for x in range(int(num_samples)):
        audio.append(volume * math.sin(2 * math.pi * freq * ( x / sample_rate )))

    return


## Function: Save sound sequence as .wav file
def save_wav(file_name):
    # Open .wav file
    wav_file=wave.open(file_name,"w")

    # .wav file paramenters
    nchannels = 1
    sampwidth = 2

    nframes = len(audio)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))

    for sample in audio:
        wav_file.writeframes(struct.pack('h', int( sample * 32767.0 )))

    wav_file.close()

    return


## Generate tone sequence
if False:
    for n in range(0,7):
        append_sinewave(volume=0.5, freq = 440)
        append_silence()
        append_sinewave(volume=0.25, freq = 400)
        append_silence()
        
    save_wav("sequence_beep.wav")

## Generate metronome sequence
if False: 
    audio = []
    for n in range(0,14):
        append_sinewave(duration_milliseconds = 50, volume = 0.5, freq = 440)
        append_silence(duration_milliseconds = 450)
        append_sinewave(duration_milliseconds = 50, volume = 0.5, freq = 400)
        append_silence(duration_milliseconds = 450)
        append_sinewave(duration_milliseconds = 50, volume = 0.5, freq = 400)
        append_silence(duration_milliseconds = 450)        
        
    save_wav("sequence_tick.wav")
    
## Generate fast metronome sequence
if False: 
    audio = []
    for n in range(0,84):
        append_sinewave(duration_milliseconds = 25, volume = 0.2, freq = 400)
        append_silence(duration_milliseconds = 225)      
        
    save_wav("sequence_tick_fast.wav")