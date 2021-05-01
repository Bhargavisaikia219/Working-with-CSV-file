import numpy as np
import urllib.request

urllib.request.urlretrieve("https://raw.githubusercontent.com/Bhargavisaikia219/CSV_files/main/climate.csv","climate.txt")

climate_data = np.genfromtxt('climate.txt', delimiter=',', skip_header=1)
print("\nData from the file are given below:\n")
print(climate_data)

w1, w2, w3 = 0.3, 0.2, 0.5
weights = np.array([w1, w2, w3])
print("\nWeights given are:\n")
print(weights)

yields_of_apples = climate_data @ weights
print("\nYields of apples based on climatic conditions:\n")
print(yields_of_apples)

climate_data_final = np.concatenate((climate_data, yields_of_apples.reshape(10000,1)), axis=1)
print("\nFinal data:\n")
print(climate_data_final)

