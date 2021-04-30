This is a practice problem to try out the use of NumPy while tackling a problem in a better approach. Before starting the problem, let's have a look at what CSV means:

CSVs: A comma-separated values (CSV) file is a delimited text file that uses a comma to separate values. Each line of the file is a data record. Each record consists of one or more fields, separated by commas. A CSV file typically stores tabular data (numbers and text) in plain text, in which case each line will have the same number of fields. (Wikipedia)

In this practice problem:

The CSV file named climate.txt, contains 10,000 climate measurements (temperature, rainfall & humidity) which is stored at different place and is retrieved using the url given below to use the data:

-->https://raw.githubusercontent.com/Bhargavisaikia219/CSV_files/main/climate.csv

Here, we are supposed to use climate data like the temperature, rainfall, and humidity to determine if a region is well suited for growing apples. A simple approach for doing this would be to formulate the relationship between the annual yield of apples (tons per hectare) and the climatic conditions like the average temperature (in degrees Fahrenheit), rainfall (in millimeters) & average relative humidity (in percentage) as a linear equation.

What are we going to do in this problem?
1) Retrieve the climate.csv file and save as .txt file in the folder.
2) Read this file into a numpy array. 
3) Perform a operation to predict the yield of apples for the entire dataset using a given set of weights.
4) Add the yields to climate_data as a fourth column.