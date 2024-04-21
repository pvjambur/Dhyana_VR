
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import time
import csv
import sys
import random

L_lat_p = []
L_long_p = []

with open('heart_rate_final.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        L_lat_p.append(float(lines[0]))
        L_long_p.append(float(lines[1]))


file.close()

L_lat_y = []
L_long_x = []

with open('heart_rate_final.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        L_lat_y.append(float(lines[0]))
        L_long_x.append(float(lines[1]))


file.close()

black_list = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,187]


fig, ax = plt.subplots()

L_lat_new = []
L_long_new = []

for lat in L_lat_p:
    L_lat_new.append(lat)
    
for long in L_long_p:
    L_long_new.append(long)

L_black_x = []
L_black_y = []
for elex in black_list:
    L_black_x.append(L_lat_y[elex - 1])
for eley in black_list:
    L_black_y.append(L_long_x[eley-1])


xpoints = np.array(L_black_x)
ypoints = np.array(L_black_y)

xaxis = np.array(L_long_x)
yaxis = np.array(L_lat_y)



ax.plot(yaxis, xaxis, color = 'red', marker = 'o',markersize = 6)

plt.plot(xpoints, ypoints, color = 'black', marker = 'o',markersize = 2)

plt.xlabel("Time (t) in s")
plt.ylabel("Heart Rate (HR) in BPM")


    
ax.set_title("Heart Rate Monitor")




l = len(L_lat_y)


k = 0

D_ref = ((L_long_x[1]-L_long_x[0])**2 + (L_lat_y[1]-L_lat_y[0])**2)**0.5
frame_ref = 25
bs = 10
term = ""


while k < l - 1:
    black = False
    term = L_long_x[k+1]
    

    for ele in black_list:
        if k == ele - 3 or k == ele - 2:
            frame_ref = 25
            my_text = fr'   Heart Rate:' +'\n' + str(term) + 'BPM'
            black = True
            break
    else:
        frame_ref = 25
        my_text = fr'   Heart Rate:' + '\n' + str(term) + 'BPM'
        black = False
    
    def f(x):
        
        return ((L_long_x[k+1]-L_long_x[k])/(L_lat_y[k+1]-L_lat_y[k])*(x - L_lat_y[k]))+ L_long_x[k]

    def animate(i):
        x = x_range[i]
        y = f(x)
        point.set_data(x,y)
        return point,

    D_new = ((L_long_x[k+1]-L_long_x[k])**2 + (L_lat_y[k+1]-L_lat_y[k])**2)**0.5
    frame_new = (D_new*frame_ref)//D_ref
    frame_new = int(frame_new)
        
    plt.ioff()
    x_range = np.linspace(L_lat_y[k],L_lat_y[k+1],frame_new)


    line = ax.plot(x_range,f(x_range), lw=4, color = 'yellow')

    
  

    point, = ax.plot([],[],color = 'magenta',marker = 'o',markersize = 9)
    
    anim = animation.FuncAnimation(fig, animate, frames=(len(x_range)), interval=20, repeat = False)
    plt.ion()

    props = dict(boxstyle='round', facecolor='green')  # bbox features
    props1 = dict(boxstyle='square', facecolor='black')
    props2 = dict(boxstyle='square', facecolor='orange')
    props3 = dict(boxstyle='square', facecolor='pink')
    ax.text(0.73, 0.98, my_text, transform=ax.transAxes, fontsize=30, verticalalignment='top', bbox=props)
    if black == True:
        my_text_1 = "Blood Oxygen: \n" + "    " + str(random.randint(91,95))
        ax.text(0.73, 0.78, my_text_1, transform=ax.transAxes, fontsize=28, verticalalignment='top', bbox=props1, color = "red")
        bs += -0.5
        my_text_5 = "Blood Pressure: \n" + "    " + str(random.randint(122,127))
        ax.text(0.73, 0.58, my_text_5, transform=ax.transAxes, fontsize=28, verticalalignment='top', bbox=props2, color = "red")
        
    else:
        my_text_1 = "Blood Oxygen: \n" + "    " + str(random.randint(96,99))
        ax.text(0.73, 0.78, my_text_1, transform=ax.transAxes, fontsize=28, verticalalignment='top', bbox=props1, color = "white")
        my_text_5 = "Blood Pressure: \n" + "    " + str(random.randint(122,127))
        ax.text(0.73, 0.58, my_text_5, transform=ax.transAxes, fontsize=28, verticalalignment='top', bbox=props2, color = "red")
    my_text_5 = "Frequency of\nmusic:\n" + "    " + str(random.randint(428,512))
    ax.text(0.9, 0.38, my_text_5, transform=ax.transAxes, fontsize=28, verticalalignment='top', bbox=props3, color = "red")


    
    
    plt.show()
    fig.canvas.draw()
    fig.canvas.flush_events()
    k+=1

    
    
    

       
        

    





