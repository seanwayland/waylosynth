
import wx
from pyo import *
import sys
 
if "2.8" in wx.version():
    import wx.lib.pubsub.setupkwargs
    from wx.lib.pubsub import pub
else:
    from wx.lib.pubsub import pub
    
liner = [line.rstrip('\n') for line in open('settings.txt')]
attacksetting = float(liner[0])

decaysetting= float(liner[1])
    
sustainsetting= float(liner[2])

releasesetting= float(liner[3])

polyphony= int(liner[4])

lowestkey= int(liner[5])

highestkey= int(liner[6])

bendrange= int(liner[7])

inputchan = int(liner[8])

outputchan = int(liner[9])

samplerate = int(liner[10])

buffsize = int(liner[11])

s = Server(sr=samplerate, buffersize=buffsize).boot()
s.start()
a = Input(chnl=inputchan)
n = Notein(poly=polyphony,scale=2, first=lowestkey, last=highestkey) # transpo
bend = Bendin(brange=bendrange, scale=1)
env = MidiAdsr(n['velocity'], attack=attacksetting, decay=decaysetting, sustain=sustainsetting, release=releasesetting)

pit = n["pitch"]
pva = PVAnal(a, size=2048)
pvt = PVTranspose(pva, transpo= pit*bend)
pvs = PVSynth(pvt)
fx2 = STRev(pvs, inpos=0.25, revtime=2, cutoff=5000, mul=env, bal=0.01, roomSize=1).out()

class LoginDialog(wx.Dialog):
    """
    Class to define login dialog
    """

    def __init__(self):
        """Constructor"""
        
        wx.Dialog.__init__(self, None, size = (600,400), title="WAYLOSYNTH")
        self.SetBackgroundColour("light blue")
        image = wx.Image('./icon_128x128.png', wx.BITMAP_TYPE_ANY)
        imageBitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.BitmapFromImage(image), pos = (450,0))
        attack_lbl = wx.StaticText(self,  label="Attack:", pos = (0, 30 ))
        self.attak = PyoGuiControlSlider(parent=self, 
                                        minvalue=0.001, 
                                        maxvalue=2, 
                                        init=0.02, 
                                        pos=(60, 30), 
                                        size=(300, 16),
                                        log=False, 
                                        integer=False,
                                        powoftwo=False,
                                        orient=wx.HORIZONTAL)
                                        
        self.attak.Bind(EVT_PYO_GUI_CONTROL_SLIDER, self.changeAttack)
        decay_lbl = wx.StaticText(self,  label="Decay:", pos = (0, 90 ))
        self.decy = PyoGuiControlSlider(parent=self, 
                                        minvalue=0.1, 
                                        maxvalue=2, 
                                        init=0.2, 
                                        pos=(60, 90), 
                                        size=(300, 16),
                                        log=False, 
                                        integer=False,
                                        powoftwo=False,
                                        orient=wx.HORIZONTAL)    
        self.decy.Bind(EVT_PYO_GUI_CONTROL_SLIDER, self.changedecy)
        
        sustn_lbl = wx.StaticText(self,  label="Sustain:", pos = (0, 150 ))
        self.sustn = PyoGuiControlSlider(parent=self, 
                                        minvalue=0.1, 
                                        maxvalue=2, 
                                        init=0.9, 
                                        pos=(60, 150), 
                                        size=(300, 16),
                                        log=False, 
                                        integer=False,
                                        powoftwo=False,
                                        orient=wx.HORIZONTAL)
                                        
        self.sustn.Bind(EVT_PYO_GUI_CONTROL_SLIDER, self.changeSustn)
        rlease_lbl = wx.StaticText(self,  label="Release:", pos = (0, 210 ))
        self.rlease = PyoGuiControlSlider(parent=self, 
                                        minvalue=0.01, 
                                        maxvalue=2, 
                                        init=0.05, 
                                        pos=(60, 210), 
                                        size=(300, 16),
                                        log=False, 
                                        integer=False,
                                        powoftwo=False,
                                        orient=wx.HORIZONTAL)    
        self.rlease.Bind(EVT_PYO_GUI_CONTROL_SLIDER, self.changeRlease)
        btn4 = wx.Button(self, label="QUIT", pos = (0,290))
        btn4.Bind(wx.EVT_BUTTON, self.onQuit)
        
    def changeAttack(self, evt):
        env.attack = evt.value
        
    def changedecy(self, evt):
        env.decay = evt.value
        
    def changeSustn(self, evt):
        env.sustain = evt.value
        
    def changeRlease(self, evt):
    
        env.release = evt.value
    def onQuit(self, event):
        s.stop()
        time.sleep(0.25)
        s.shutdown()
        time.sleep(0.25)

        sys.exit()
        
########################################################################
class MyPanel(wx.Panel):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent, size = (600,400))
        
 
 
########################################################################
class MainFrame(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, size = (600,400) , title="Main App", )
        panel = MyPanel(self)
        
        
        pub.subscribe(self.myListener, "frameListener")
 
        # Ask user to login
        dlg = LoginDialog()
        dlg.ShowModal()
 
    #----------------------------------------------------------------------
    def myListener(self, message, arg2=None):
        """
        Show the frame
        """
        self.Show()
        


app = wx.App(False)
frame = MainFrame()
app.MainLoop()

# Clean up...
s.stop()
time.sleep(0.25)
s.shutdown()
time.sleep(0.25)
sys.exit()
