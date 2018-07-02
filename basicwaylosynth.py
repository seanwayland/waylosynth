

from pyo import *
import sys

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

s = Server(sr=samplerate, buffersize=buffsize).boot()
s.start()
a = Input(chnl=inputchan)
n = Notein(poly=polyphony,scale=2) # transpo
bend = Bendin(brange=bendrange, scale=1)
env = MidiAdsr(n['velocity'], attack=attacksetting, decay=decaysetting, sustain=sustainsetting, release=releasesetting)

pit = n["pitch"]
pva = PVAnal(a, size=2048)
pvt = PVTranspose(pva, transpo= pit*bend)
pvs = PVSynth(pvt)
fx2 = STRev(pvs, inpos=0.25, revtime=2, cutoff=5000, mul=env, bal=0.01, roomSize=1).out()

s.gui(locals())


