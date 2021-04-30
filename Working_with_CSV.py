import numpy as np
import urllib.request

urllib.request.urlretrieve("https://raw.githubusercontent.com/Bhargavisaikia219/CSV_files/main/climate.csv","climate.txt")

climate_data = np.genfromtxt('climate.txt', delimiter=',', skip_header=1)

print(climate_data)