# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 22:26:51 2024

@author: rahul
"""

import numpy as np
import matplotlib.pyplot as plt


t = np.arange(0, 272, 0.1, dtype=float)

Coeff = np.load('data/Coeff.npy')


t1 = np.arange(0, 40.3, 0.1, dtype=float)
t2 = np.arange(40.3,146.6,0.1, dtype=float)
t3 = np.arange(146.6,196.6,0.1, dtype=float)
t4 = np.arange(196.6,219.1,0.1, dtype=float)
t5 = np.arange(219.1,225.8,0.1, dtype=float)
t6 = np.arange(225.8,271.8,0.1, dtype=float)

Input1 = np.linspace(300,953.15,len(t1))
Input2 = np.linspace(953.15,1123.15,len(t2))
Input3 = np.linspace(1123.15,1123.15,len(t3))
Input4 = np.linspace(1123.15,943.15,len(t4))
Input5 = np.linspace(943.15,668.15,len(t5))
Input6 = np.linspace(668.15,300,len(t6))


result = np.concatenate((Input1, Input2, Input3, Input4, Input5, Input6))

result_input = result[0:1001]


plt.figure(figsize=(8, 5))
plt.plot(t[0:1001], Coeff[0,:]/max(Coeff[0,:]),
         linestyle='-',
         linewidth=2.5,
         color='red',
         label='Coeff1')
plt.plot(t[0:1001], Coeff[1,:]/max(Coeff[1,:]),
         linestyle='-',
         linewidth=2.5,
         color='red',
         label='Coeff2')
plt.plot(t[0:1001], Coeff[2,:]/max(Coeff[2,:]),
         linestyle='-',
         linewidth=2.5,
         color='black',
         label='Coeff3')
plt.plot(t[0:1001], Coeff[3,:]/max(Coeff[3,:]),
         linestyle='-',
         linewidth=2.5,
         color='green',
         label='Coeff4')



plt.xlabel('time',fontsize=20)
plt.ylabel('Normalized Coeff', fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# legend settings
plt.ylim(-3, 6)
plt.xlim(0, 100)

plt.grid(linestyle='dotted')
plt.legend(ncol=2, loc=9, fontsize=20) # 9 means top center
plt.tight_layout()
plt.savefig('results/coeff.png', dpi=300)




