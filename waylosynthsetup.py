import wx
from pyo import *
import sys
 
if "2.8" in wx.version():
    import wx.lib.pubsub.setupkwargs
    from wx.lib.pubsub import pub
else:
    from wx.lib.pubsub import pub


  
########################################################################
class LoginDialog(wx.Dialog):
    """
    Class to define login dialog
    """
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        
        wx.Dialog.__init__(self, None, size = (600,600), title="WAYLOSYNTH SETUP")
        self.SetBackgroundColour("light blue")
        image = wx.Image('./icon_128x128.png', wx.BITMAP_TYPE_ANY)
        imageBitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.BitmapFromImage(image), pos = (450,0))

        
 

        # attack setting
        attack_lbl = wx.StaticText(self,  label="Attack:", pos = (0, 30 ))
        self.attack = wx.TextCtrl(self, pos = (150,30))
        attackd_lbl = wx.StaticText(self,  label="default : 0.2", pos = (300, 30 ))

        # decay setting

        decay_lbl = wx.StaticText(self, label="Decay:", pos = (0,60))
        self.decay = wx.TextCtrl(self, pos = ( 150 , 60 ))
        decayd_lbl = wx.StaticText(self,  label="default : 0.001", pos = (300, 60 ))
        
        # sustain setting
        sustain_lbl = wx.StaticText(self, label="Sustain :", pos =(0, 90))
        self.sustain = wx.TextCtrl(self, pos = (150, 90))
        sustaind_lbl = wx.StaticText(self,  label="default : 0.9", pos = (300, 90 ))

        # release setting

 
        release_lbl = wx.StaticText(self,  label="Release:", pos =(0, 120))
        self.release = wx.TextCtrl(self, pos = (150,120))
        released_lbl = wx.StaticText(self,  label="default : 0.05", pos = (300, 120 ))
        
        # polyphony setting
        polyphony_lbl = wx.StaticText(self,  label="Polyphony :", pos = (0, 150))
        self.polyphony = wx.TextCtrl(self, pos = (150,150))
        polyphonyd_lbl = wx.StaticText(self,  label="default : 8", pos = (300, 150 ))

        # lowestkey setting

        lowestkey_lbl = wx.StaticText(self, label="Lowestkey :", pos = (0,180))
        self.lowestkey = wx.TextCtrl(self, pos = ( 150, 180 ))
        lowestkeyd_lbl = wx.StaticText(self,  label="default : 37", pos = (300, 180 ))
        
        # highestkey setting
        highestkey_lbl = wx.StaticText(self, label="Highestkey:", pos =(0, 210))
        self.highestkey = wx.TextCtrl(self, pos = (150, 210))
        highestkeyd_lbl = wx.StaticText(self,  label="default : 83", pos = (300, 210 ))

        # bendrange setting

 
        bendrange_lbl = wx.StaticText(self,  label="Bendrange:", pos =(0, 240))
        self.bendrange = wx.TextCtrl(self, pos = (150,240))
        bendranged_lbl = wx.StaticText(self,  label="default : 2", pos = (300, 240))

        # inputchannel setting
        inputchannel_lbl = wx.StaticText(self,  label="Inputchannel:", pos = (0, 270 ))
        self.inputchannel = wx.TextCtrl(self, pos = (150,270))
        inputchanneld_lbl = wx.StaticText(self,  label="default : 0", pos = (300, 270 ))

        # outputchannel setting

        outputchannel_lbl = wx.StaticText(self, label="Outputchannel:", pos = (0,300))
        self.outputchannel = wx.TextCtrl(self, pos = ( 150 , 300 ))
        outputchanneld_lbl = wx.StaticText(self,  label="default : 0", pos = (300, 300 ))
        
        # samplerate setting
        samplerate_lbl = wx.StaticText(self, label="Samplerate:", pos =(0, 330))
        self.samplerate = wx.TextCtrl(self, pos = (150, 330))
        samplerated_lbl = wx.StaticText(self,  label="default : 96000 ", pos = (300, 330))

        # buffersize setting

 
        buffersize_lbl = wx.StaticText(self,  label="Buffersize:", pos =(0, 360))
        self.buffersize = wx.TextCtrl(self, pos = (150,360))
        buffersized_lbl = wx.StaticText(self,  label="default : 256 ", pos = (300, 360 ))




        # buttons to start or quit or save settings 

        btn = wx.Button(self, label="ENTER NEW SETTINGS (FILL IN ALL BOXES) AND CLICK HERE TO SAVE" , pos = (0,420))
        btn.Bind(wx.EVT_BUTTON, self.onLogin)

    
        btn2 = wx.Button(self, label="RESTORE DEFAULT SETTINGS" , pos = (0,450))
        btn2.Bind(wx.EVT_BUTTON, self.onLogin2)      


        btn4 = wx.Button(self, label="QUIT", pos = (0,480))
        btn4.Bind(wx.EVT_BUTTON, self.onQuit)
 
    #----------------------------------------------------------------------
    def onLogin(self, event):
        """
        

        
        """
        # if store settings button is pressed take values from 

        decay = self.decay.GetValue()

        attack = self.attack.GetValue()

        sustain = self.sustain.GetValue()

        release = self.release.GetValue()

        polyphony = self.polyphony.GetValue()

        lowestkey = self.lowestkey.GetValue()

        highestkey = self.highestkey.GetValue()

        bendrange = self.bendrange.GetValue()

        inputchannel = self.inputchannel.GetValue()

        outputchannel = self.outputchannel.GetValue()

        samplerate = self.samplerate.GetValue()

        buffersize = self.buffersize.GetValue()


        #create array with entered values

        fieldValues = ["","","","","","","","","","","","",""]
        fieldValues[0] = decay
        fieldValues[1] = attack
        fieldValues[2] = sustain
        fieldValues[3] = release
        fieldValues[4]= polyphony
        fieldValues[5]= lowestkey
        fieldValues[6]= highestkey
        
        fieldValues[7]= bendrange
        fieldValues[8]= inputchannel
        fieldValues[9] = outputchannel
        fieldValues[10] = samplerate
        fieldValues[11] = buffersize

        #write entered values to settings file 

        outF = open('../../../waylosynth101.app/contents/resources/settings.txt', 'w')
        for line in fieldValues:
             outF.write(line + '\n')
        outF.close()
        


    def onLogin2(self, event):




        fieldValues1 = ["","","","","","","","","","","","",""]
        fieldValues1[0] = "0.001"
        fieldValues1[1] = "0.2"
        fieldValues1[2] = "0.9"
        fieldValues1[3] = "0.05"
        fieldValues1[4]= "8"
        fieldValues1[5]= "37"
        fieldValues1[6]= "83"
        
        fieldValues1[7]= "2"
        fieldValues1[8]= "0"
        fieldValues1[9] = "0"
        fieldValues1[10] = "96000"
        fieldValues1[11] = "256"

        #write entered values to settings file 

        outF = open('../../../waylosynth101.app/contents/resources/settings.txt', 'w')
        for line in fieldValues1:
             outF.write(line + '\n')
        outF.close()
        






        
        
        



 

       

    def onQuit(self, event):

        sys.exit()

        
        




         
        

        
        

 
########################################################################
class MyPanel(wx.Panel):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent, size = (600,600))
        
 
 
########################################################################
class MainFrame(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, size = (600,600) , title="Main App", )
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
        




# get devices found by pyo 
        
ains = pa_get_input_devices()
aouts = pa_get_output_devices()
mins = pm_get_input_devices()
mouts = pm_get_output_devices()


names, indexes = pa_get_input_devices()
name1 = names[indexes.index(pa_get_default_input())]
names, indexes = pa_get_output_devices()
name2 = names[indexes.index(pa_get_default_output())]
names, indexes = pm_get_output_devices()
name3 = names[indexes.index(pm_get_default_output())]
names, indexes = pm_get_input_devices()
name4 = names[indexes.index(pm_get_default_input())]
settings = ('Default audio input is' + str(name1) + '\n' + 'Default audio output is ' +  str(name2)  + '\n' + 'Default midi output is ' +  str(name3) + '\n' +'Default midi input is ' +  str(name4)
            + '\n' + 'Input devices found is ' +  str(ains) + '\n'  + 'Output devices found is ' + str(aouts) + '\n' +  'Midi input devices found is ' + str(mins) 
+ '\n' + 'Midi output devices found is ' + str(mouts))


#print out default devices found in a wx.python message box 

app1 = wx.App()
wx.MessageBox( settings ,'Waylosynth input and outputs available' , wx.OK | wx.ICON_INFORMATION)


app = wx.App(False)
frame = MainFrame()
app.MainLoop()


















