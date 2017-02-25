################################
from pyo import *

# Variables
MAXVOICES = 20

s = Server()
s.setMidiInputDevice(99) # Opens all devices
s.boot()
global waylotrans
global lastnote
waylotrans = 0
lastnote = 60 



def onNoteOn(which):
    pit = n["pitch"].get(True)[which]
    vel = n["velocity"].get(True)[which]
    vel = int(vel * 127)
    if int(pit) < 60:
        global waylotrans
        
        waylotrans = int(pit) - 48
        
    else:
        pity = int(pit) + waylotrans
        s.noteout(pity, vel)
        global lastnote
        lastnote = pity
        

def onNoteOff(which):
    pit = n["pitch"].get(True)[which]
    if int(pit) < 60:
         global waylotrans
         waylotrans = 0
    else:        
        pity = int(pit) + waylotrans
        global lastnote
        s.noteout(pity, 0)
        s.noteout(lastnote, 0)

n = Notein(poly=MAXVOICES, first=36, last=72)

# Setup callbacks for noteon and noteoff.
# Give a list of integer to the "arg" argument to retrieve 
# the voice number in the callbacks.
tfon = TrigFunc(n["trigon"], onNoteOn, range(MAXVOICES))
tfoff = TrigFunc(n["trigoff"], onNoteOff, range(MAXVOICES))

s.gui(locals())
#########################
