import scipy as sp
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import UnivariateSpline
import pandas as pd
from scipy.signal import savgol_filter
from scipy.integrate import simpson, cumtrapz
df = pd.read_excel(r'C:\Users\alexa\Documents\Git\sensor_data.xlsx', sheet_name='val',names=['ms', 'v'])
# Definieer de gegevenspunten
x1 = np.array([3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7 ,7.5, 8, 8.5, 9 ,9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13])
y1 = np.array([1.54, 1.38, 1.21, 1.12, 1.05, 0.97, 0.91, 0.87, 0.83, 0.79, 0.75, 0.73, 0.71, 0.69, 0.67, 0.63, 0.61, 0.59, 0.58, 0.57, 0.56])
spline = UnivariateSpline(x1, y1, s=2)
y_spline = spline(x1)
def find_x(y_waarde, spline, x_start=0):
    root_func = lambda x: spline(x) - y_waarde
    x_value = sp.optimize.fsolve(root_func, x_start)
    return x_value[0]
afstanden = []
lijst =[i*5/1023 for i in df['v']]
for i in lijst:
    x_value = find_x(float(i), spline)
    afstanden.append(x_value)
afstanden = np.array(afstanden)
subtrahend = 0.07148430266839831
afstanden3 = (afstanden*.01)- subtrahend
t = (np.array(df["ms"])*1e-3)
r=9.81/0.009732380403975477

a = afstanden3*r
a2 = savgol_filter(a,polyorder=4,window_length=100)

arr = np.logical_and(t>0,t<6)
velocity = cumtrapz(a2[arr]-9.82, t[arr], initial=0)
dist2 = cumtrapz(velocity[arr],t[arr], initial=0)
dist = simpson(velocity[arr], t[arr])
average_v=np.average(velocity)
average_a = np.average(a2)
average_dist = np.sum(dist)



plt.plot(t,a, alpha=.4)
plt.plot(t,a2, linewidth=2)
plt.plot(t, velocity)
plt.plot(t,dist2)
plt.title('Gooien test #1')
plt.xlabel('t (s)')
plt.ylabel('a (m/s^2)')
plt.legend(['Unfiltered acceleration',f'Average acceleration={"%.2f"% average_a}(m/s^2)',f'Average velocity={"%.2f"% average_v}(m/s)',f'Distance: {"%.2f"% average_dist} m'])









### PLOTTING SPLINE ###
# plt.plot(x1, y1, 'o', label='gemeten punten')
# plt.plot(x1, y_spline, label='spline fit')
# plt.grid(True)
# plt.legend()
# plt.show()


### 57CM RECHTS ###
# arr = np.logical_and(t>5,t<8)
# plt.title('57cm-rechts')
# plt.xlabel('t (s)')
# plt.ylabel('a (m/s^2)')
# plt.legend(['Unfiltered acceleration',f'Average acceleration={"%.2f"% average_a}(m/s^2)',f'Average velocity={"%.2f"% average_v}(m/s)'])
# plt.text(7.8,14,f'Distance: {"%.2f"% integral} m')

### 57CM HEEN WEER ###
# arr = np.logical_and(t>3,t<9)
# plt.title('57cm-heen-terug')
# plt.xlabel('t (s)')
# plt.ylabel('a (m/s^2)')
# plt.legend(['Unfiltered acceleration',f'Average acceleration={"%.2f"% average_a}(m/s^2)',f'Average velocity={"%.2f"% average_v}(m/s)'])
# plt.text(7.8,28,f'Distance: {"%.2f"% integral} m')

### G-WAARDE ###
# arr = np.logical_and(t>18,t<26)
# plt.title('G-waarde')
# plt.xlabel('t (s)')
# plt.ylabel('a (m/s^2)')
# plt.legend(['Unfiltered acceleration',f'Average acceleration={"%.2f"% average_a}(m/s^2)',f'Average velocity={"%.2f"% average_v}(m/s)'])


plt.show()