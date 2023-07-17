import wx
import numpy as np
import matplotlib.pyplot as pyplot
import uldaq
import time

main_sizer = wx.FlexGridSizer(2, 3, 10, 10)
num = []
c=0
k=1000
prova=np.arange(0,k)-np.arange(0,k)
for x in range(k):
    num.append(x)
freq = 50000
res=[]
pool = uldaq.get_daq_device_inventory(7)
my_daq = uldaq.DaqDevice(pool[0])
my_daq.disconnect()
my_daq.connect()
I_channell = my_daq.get_ai_device()
out = []
class MyGrid(wx.Panel):
    
    def __init__(self, parent):
        super().__init__(parent)
        
        pyplot.scatter(out, res, color = 'green', label = 'Marks')
        pyplot.scatter(out, res, color = 'blue', label = 'Zero')
        pyplot.legend(loc='upper left', frameon=True)
        
        button = wx.Button(self, label='Start')
        button.Bind(wx.EVT_BUTTON, self.on_button1)
        
        self.staticbitmap = wx.StaticBitmap(self)
        main_sizer.Add(self.staticbitmap, 1, wx.EXPAND)
        main_sizer.Add(button, flag=wx.LEFT)
        self.SetSizer(main_sizer)
    def on_button1(self,event):
        global k
        out = uldaq.create_float_buffer(1,k)
        I_channell.a_in_scan(0,0,2,5,k,freq,8,0,out)
        time.sleep(1)
        I_channell.scan_stop()
        pyplot.plot(num, out, color = 'green')
        pyplot.plot(num, prova, color = 'blue')
        nuovo = []
        for i in range(k):
            nuovo.append(out[i])
        idx = np.argwhere(np.diff(np.sign(nuovo - prova))).flatten()
        print(idx)
        url = "/home/admin/Desktop/prova.png"
        pyplot.savefig(url)
        self.staticbitmap.SetBitmap(wx.Bitmap(url))
        print("trovati",len(idx))
        print("periodi",len(idx)/2)
        print("frequenza",(len(idx)/2)*(freq/k))
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Hello World')
        panel = MyGrid(self)
        self.Show()
if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = MyFrame()
    app.MainLoop()