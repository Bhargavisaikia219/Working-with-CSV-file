import numpy as np
import urllib.request

#retrieve url of the CSV file
urllib.request.urlretrieve("https://raw.githubusercontent.com/Bhargavisaikia219/CSV_files/main/climate.csv","climate.txt")

#Save file in the current folder
climate_data = np.genfromtxt('climate.txt', delimiter=',', skip_header=1)
print("\nData from the file are given below:\n")
print(climate_data)     #prints the data from the txt file

#declaration of weights as w1, w2 and w3
w1, w2, w3 = 0.3, 0.2, 0.5
weights = np.array([w1, w2, w3])
print("\nWeights given are:\n")
print(weights)          #prints the weights

#matric multiplication to find out yields of apples
yields_of_apples = climate_data @ weights
print("\nYields of apples based on climatic conditions:\n")
print(yields_of_apples)     #prints the calculated result

#adds the yields_of_apples to climate_data as a fourth column
climate_data_final = np.concatenate((climate_data, yields_of_apples.reshape(10000,1)), axis=1)
print("\nFinal data:\n")
print(climate_data_final)   #prints the output

#write the final results from our computation above back in the CSV format to the file climate_data_final.txt

np.savetxt('climate_data_final.txt', climate_data_final, fmt='%.2f', delimiter=',', header='temperature,rainfall,humidity,yields_of_apples', comments="")