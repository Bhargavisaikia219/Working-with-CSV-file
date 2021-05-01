import numpy as np
import urllib.request

urllib.request.urlretrieve("https://raw.githubusercontent.com/Bhargavisaikia219/CSV_files/main/climate.csv","climate.txt")

climate_data = np.genfromtxt('climate.txt', delimiter=',', skip_header=1)

w1, w2, w3 = 0.3, 0.2, 0.5
weights=np.array([w1, w2, w3])
print(weights)

yields= climate_data @ weights
print(yields)