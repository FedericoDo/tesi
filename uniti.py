#!/usr/bin/python
import matplotlib.pyplot as plt
import uldaq
import tkinter
import time
import numpy
import sys

#enabling interactive mode
plt.ion()
#variable initialization
time_for_avg=0
nominal_eff=0
e2 = ""
master2 = ""
keep = 1
    
#callback for second entry box
def callback2():
    global master2
    global nominal_eff
    global e2
    value = e2.get()
    try:
        nominal_eff = float(value)
        tkinter.messagebox.showinfo(title="VAL. VALIDO", message="il valore inserito è valido")
    except :
        tkinter.messagebox.showwarning(title="VAL. INVALIDO", message="il valore inserito non è un numero, impostato in automatico a 3.5")
        nominal_eff = 3.5
    master2.destroy()

#callback for first entry box
def callback():
    global master
    global master2
    global time_for_avg
    global e
    global e2
    value = e.get()
    if value.isdigit()
        time_for_avg = int(value)
        tkinter.messagebox.showinfo(title="VAL. VALIDO", message="il valore inserito è valido")
    else :
        tkinter.messagebox.showwarning(title="VAL. INVALIDO", message="il valore inserito non è intero, impostato in automatico a 10")
        time_for_avg = 10
    master.destroy()
    #box2 creation
    master2 = Tk()
    master2.geometry("400x50")
    master2.title("inserisci valore efficace nominale")
    e2 = Entry(master2)
    e2.pack()
    b2 = Button(master2, text = "inserisci", width = 10, command = callback2)
    b2.pack()
    e2.focus_set()
    master2.mainloop()
    
#box1 creation
master = Tk()
master.geometry("400x50")
master.title("inserisci intervallo secondi campionamento")
e = Entry(master)
e.pack()
e.focus_set()
b = Button(master, text = "inserisci", width = 10, command = callback)
b.pack()
master.mainloop()

class DynamicUpdate():
    #Suppose we know the x range
    min_x = 0
    max_x = 10
    global time_for_avg
   

    def on_launch(self):
        #Set up plot
        self.figure, self.ax = plt.subplots(2,2)
        self.lines, = self.ax[0][0].plot([],[], 'o')
        self.lines2, = self.ax[0][1].plot([],[], 'o')
        self.lines7, = self.ax[1][0].plot([],[], 'o')
        self.lines8, = self.ax[1][1].plot([],[], 'o')
        #effective value limits
        self.lines3, = self.ax[0][0].plot([],[], 'r')
        self.lines4, = self.ax[0][0].plot([],[], 'r')
        #frequency limits
        self.lines5, = self.ax[0][1].plot([],[], 'r')
        self.lines6, = self.ax[0][1].plot([],[], 'r')
        #average effective value limits
        self.lines9, = self.ax[1][0].plot([],[], 'r')
        self.lines10, = self.ax[1][0].plot([],[], 'r')
        #average frequency limits
        self.lines11, = self.ax[1][1].plot([],[], 'r')
        self.lines12, = self.ax[1][1].plot([],[], 'r')
        #Autoscale on unknown axis and known lims on the other
        self.ax[0][0].set_autoscaley_on(True)
        self.ax[0][0].set_xlim(self.min_x, self.max_x)
        self.ax[0][1].set_autoscaley_on(True)
        self.ax[0][1].set_xlim(self.min_x, self.max_x)
        self.ax[1][0].set_autoscaley_on(True)
        self.ax[1][0].set_xlim(self.min_x, self.max_x)
        self.ax[1][1].set_autoscaley_on(True)
        self.ax[1][1].set_xlim(self.min_x, self.max_x)
        #Other stuff
        self.ax[0][0].title.set_text("valore efficace")
        self.ax[0][1].title.set_text("frequenza")
        self.ax[1][0].title.set_text("valore efficace medio")
        self.ax[1][1].title.set_text("frequenza media")
        self.ax[0][0].grid()
        self.ax[0][1].grid()
        self.ax[1][0].grid()
        self.ax[1][1].grid()

    def on_running(self, xdata, ydata1, ydata2, eff_sup, eff_inf, freq_sup, freq_inf, eff_avg, freq_avg, xdata2):
        #Update data (with the new and the old points)
        global keep
        try:
            self.lines.set_xdata(xdata)
            self.lines.set_ydata(ydata1)
            self.lines2.set_xdata(xdata)
            self.lines2.set_ydata(ydata2)
            t = numpy.linspace(-5, xdata[len(xdata)-1]+10, 400)
            self.lines7.set_xdata(xdata2)
            self.lines7.set_ydata(eff_avg)
            self.lines8.set_xdata(xdata2)
            self.lines8.set_ydata(freq_avg)
            if len(xdata2) > 0 :
                t2 = numpy.linspace(-5, xdata2[len(xdata2)-1]+10, 400)
            #effective value limits
            self.lines3.set_xdata(t)
            self.lines3.set_ydata(eff_sup)
            self.lines4.set_xdata(t)
            self.lines4.set_ydata(eff_inf)
            self.ax[0][0].set_xlim(xdata[len(xdata)-1]-5, xdata[len(xdata)-1]+5)
            #frequency limits
            self.lines5.set_xdata(t)
            self.lines5.set_ydata(freq_sup)
            self.lines6.set_xdata(t)
            self.lines6.set_ydata(freq_inf)
            self.ax[0][1].set_xlim(xdata[len(xdata)-1]-5, xdata[len(xdata)-1]+5)
            #average middle value limits
            if len(xdata2)>0 :
                self.lines9.set_xdata(t2)
                self.lines9.set_ydata(eff_sup)
                self.lines10.set_xdata(t2)
                self.lines10.set_ydata(eff_inf)
                self.ax[1][0].set_xlim(xdata2[len(xdata2)-1]-5, xdata2[len(xdata2)-1]+5)
            #average frequency limits
                self.lines11.set_xdata(t2)
                self.lines11.set_ydata(freq_sup)
                self.lines12.set_xdata(t2)
                self.lines12.set_ydata(freq_inf)
                self.ax[1][1].set_xlim(xdata2[len(xdata2)-1]-5, xdata2[len(xdata2)-1]+5)
            #Need both of these in order to rescale
            self.ax[0][0].relim()
            self.ax[0][0].autoscale_view()
            self.ax[0][1].relim()
            self.ax[0][1].autoscale_view()
            self.ax[1][0].relim()
            self.ax[1][0].autoscale_view()
            self.ax[1][1].relim()
            self.ax[1][1].autoscale_view()
            #We need to draw *and* flush
            self.figure.canvas.draw()
            self.figure.canvas.flush_events()
        except KeyboardInterrupt:
            print ("ending")
            keep = 0
        
    #Example
    def __call__(self):
        import numpy as np
        import time
        global keep
        self.on_launch()
        freq = 50000
        k=50000
        cont = 0
        contatore = 0
        contatore2 = 0
        freq_for_avg = [0]*time_for_avg
        eff_for_avg = [0]*time_for_avg
        avg_freq = []
        avg_eff = []
        limite_sup_eff=nominal_eff+(nominal_eff/10)
        limite_inf_eff=nominal_eff-(nominal_eff/10)
        limite_sup_freq=50.5
        limite_inf_freq=49.5
        frequenze =[]
        asse_x = []
        asse_x_2 = []
        out=[]
        res=[]
        pool = uldaq.get_daq_device_inventory(7)
        my_daq = uldaq.DaqDevice(pool[0])
        my_daq.disconnect()
        my_daq.connect()
        zero=np.arange(0,k)-np.arange(0,k)
        I_channell = my_daq.get_ai_device()
        while(keep):
            try:
                out = uldaq.create_float_buffer(1,k)
                I_channell.a_in_scan(0,0,2,5,k,freq,8,0,out)
                time.sleep(1)
                I_channell.scan_stop()
                #effective value:
                somma = 0
                for r in range(k):
                    somma += out[r]**2
                parz = somma/k
                fin = numpy.round(parz **(1/2),decimals=1)
                if fin>limite_sup_eff :
                    tkinter.messagebox.showwarning(title="VAL. EFF", message="Limite superiore superato")  
                if fin<limite_inf_eff :
                    tkinter.messagebox.showwarning(title="VAL. EFF", message="Limite inferiore superato")
                res.append(fin)
                #frquency:
                nuovo = []
                temp = 0
                for i in range(k):
                    nuovo.append(out[i])
                idx = np.argwhere(np.diff(np.sign(nuovo - zero))).flatten()
                temp=idx[4]-idx[2]
                temp=temp/freq
                single_freq=1/temp
0                if single_freq>limite_sup_freq :
                    tkinter.messagebox.showwarning(title="FREQ", message="Limite superiore superato")  
                if single_freq<limite_inf_freq :
                    tkinter.messagebox.showwarning(title="FREQ", message="Limite inferiore superato")
                frequenze.append(single_freq)
                #average effective value
                eff_for_avg[contatore]=fin
                #average frequency
                freq_for_avg[contatore]=single_freq
                #graphic
                cont+=1
                asse_x.append(cont)
                contatore+=1
                if contatore == time_for_avg:
                    contatore = 0
                    asse_x_2.append(contatore2)
                    contatore2 +=1
                    somma_freq = 0
                    somma_eff = 0
                    for i in range(time_for_avg) :
                        somma_freq += freq_for_avg[i]
                        somma_eff += eff_for_avg[i]
                    avg_freq.append(somma_freq/time_for_avg)
                    avg_eff.append(somma_eff/time_for_avg)
                self.on_running(asse_x, res, frequenze, limite_sup_eff, limite_inf_eff, limite_sup_freq, limite_inf_freq, avg_eff, avg_freq, asse_x_2)
                time.sleep(1)
            except KeyboardInterrupt:
                print ("ending")
                keep = 0
d = DynamicUpdate()
d()