from pyo import *

### print out inputs 
print("Audio host APIS:")
pa_list_host_apis()
pa_list_devices()
pm_list_devices()
print("Default input device: %i" % pa_get_default_input())
print("Default output device: %i" % pa_get_default_output())


import sys

### settings 
attacksetting = 0.001

decaysetting= 0.2

sustainsetting= 0.9

releasesetting= 0.05

polyphony= 8

bendrange= 2

inputchan = 0

outputchan = 0

samplerate = 44100

buffsize = 512

### set up inputs 
s = Server(sr=samplerate, buffersize=buffsize)
s.setInputDevice(0)
s.setOutputDevice(0)
s.setMidiInputDevice(1)

s.boot()

### get some input from audio and midi 
a = Input(chnl=inputchan)



n = Notein(poly=polyphony,scale=2) # transpo
n.setCentralKey(60)
bend = Bendin(brange=bendrange, scale=1)


env = MidiAdsr(n['velocity'], attack=attacksetting, decay=decaysetting, sustain=sustainsetting, release=releasesetting)
pit = n["pitch"]

### perform psola transposition on incoming audio. middle C should not transpose . C# should transpose up a half step
pva = PVAnal(a, size=1024)
pvt = PVTranspose(pva, transpo= pit*bend)
pvs = PVSynth(pvt)

### send the result to outputs 
fx2 = STRev(pvs, inpos=0.25, revtime=2, cutoff=5000, mul=env, bal=0.01, roomSize=1).out(0)
fx3 = STRev(pvs, inpos=0.25, revtime=2, cutoff=5000, mul=env, bal=0.01, roomSize=1).out(1)




### processing loop with gui 
s.gui(locals())






