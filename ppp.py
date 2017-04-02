import matplotlib
# Force matplotlib to not use any Xwindows backend.
import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
import os.path


url = "http://data.kk.dk/dataset/9070067f-ab57-41cd-913e-bc37bfaf9acd/resource/9fbab4aa-1ee0-4d25-b2b4-b7b63537d2ec/download/befkbhalderkoencivst.csv"
response = requests.get(url, params={'downloadformat' : 'csv'})

fname = "befkbhalderkoencivst.csv"

if response.ok:
    with open(fname, 'wb') as f:
        f.write(response.content)
csv = pd.read_csv(fname)
dd = csv.as_matrix()

male1830 = np.array(dd[(dd[:,2] > 17) & (dd[:,2] < 31) & (dd[:,4] == 1)]);
female1830 = np.array(dd[(dd[:,2] > 17) & (dd[:,2] < 31) & (dd[:,4] == 2)]);
female50 = np.array(dd[(dd[:,2] > 50) & (dd[:,4] == 2)]);
male50 = np.array(dd[(dd[:,2] > 50) & (dd[:,4] == 1)]);
years = np.unique(dd[:,0])
male1830sum = np.array([np.sum(male1830[(male1830[:,0] == year)][:,5]) for year in years])
female1830sum = np.array([np.sum(female1830[(female1830[:,0] == year)][:,5]) for year in years])
female50sum = np.array([np.sum(female50[(female50[:,0] == year)][:,5]) for year in years])
male50sum = np.array([np.sum(male50[(male50[:,0] == year)][:,5]) for year in years])

plt.figure()
plt.plot(years, female1830sum, label="Females 18-30")
plt.plot(years, male1830sum, label="Males 18-30")
plt.plot(years, male50sum, label="Males 50+")
plt.plot(years, female50sum, label="Females 50+")
plt.legend(loc='upper left')
plt.show()
