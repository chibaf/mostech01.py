def Q(t):
  import math
  R1=1;R2=1;Vx=1;C0=1;C1=1
  q1=(C0*R2*Vx)/(R1 + R2) + C1/math.exp(((R1 + R2)*t)/(C0*R1*R2))
  return q1

import matplotlib.pyplot as plt
import numpy as np

y=100*[0]
x=100*[0]
for i in range(0,100):
  y[i]=Q(float(i)/10.)
  x[i]=float(i)/10.
plt.plot(x,y)
plt.show()