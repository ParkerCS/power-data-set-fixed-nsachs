'''
Use the power_data.csv file AND the zipcode database
to answer the questions below.  Make sure all answers
are printed in a readable format. (i.e. "The city with the highest electricity cost in Illinois is XXXXX."

The power_data dataset, compiled by NREL using data from ABB,
the Velocity Suite and the U.S. Energy Information
Administration dataset 861, provides average residential,
commercial and industrial electricity rates by zip code for
both investor owned utilities (IOU) and non-investor owned
utilities. Note: the file includes average rates for each
utility, but not the detailed rate structure data found in the
OpenEI U.S. Utility Rate Database.

This is a big dataset.
Below are some questions that you likely would not be able
to answer without some help from a programming language.
It's good geeky fun.  Enjoy

FOR ALL THE RATES, ONLY USE THE BUNDLED VALUES (NOT DELIVERY).  This rate includes transmission fees and grid fees that are part of the true rate.
'''

#1  What is the average residential rate for YOUR zipcode? You will need to read the power_data into your program to answer this.  (7pts)

#2 What is the MEDIAN rate for all BUNDLED RESIDENTIAL rates in Illinois? Use the data you extracted to check all "IL" zipcodes to answer this. (10pts)

#3 What city in Illinois has the lowest residential rate?  Which has the highest?  You will need to go through the database and compare each value for this one. Then you will need to reference the zipcode dataset to get the city.  (15pts)


#FOR #4  CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS. The first one is easier than the second.
#4  (Easier) USING ONLY THE ZIP CODE DATA... Make a scatterplot of all the zip codes in Illinois according to their Lat/Long.  Make the marker size vary depending on the population contained in that zip code.  Add an alpha value to the marker so that you can see overlapping markers.

#4 (Harder) USING BOTH THE ZIP CODE DATA AND THE POWER DATA... Make a scatterplot of all zip codes in Illinois according to their Lat/Long.  Make the marker red for the top 25% in residential power rate.  Make the marker yellow for the middle 25 to 50 percentile. Make the marker green if customers pay a rate in the bottom 50% of residential power cost.  This one is very challenging.  You are using data from two different datasets and merging them into one.  There are many ways to solve. (20pts)

import csv
import matplotlib.pyplot as plt
from operator import itemgetter
import statistics

file = open("power_data.csv", "r")
file2 = open("free-zipcode-database-Primary.csv", "r")

# ------- Problem # 1 ------- #
# Reading the file into a list
power_data = []
reader = csv.reader(file, delimiter = ',')
for line in reader:
    power_data.append(line)

#Parsing the headers out from the data
headers = power_data[0]
data = power_data[1:]
#print("\nHeaders list: ", end = "")
#print(headers, "\n")
#print("\nPower Data list: ", end = "")
#print(data, "\n")

#Finding the rate given the zipcode and "bundled" element
for i in range(len(data)):
    if data[i][0] == "60610" and data[i][4] == "Bundled":
        print("Average residential rate for 60610: ", data[i][-1])

# ------- Problem #2 -------- #
il_bund_list = []

for i in range(len(data)):
    if data[i][3] == "IL" and data[i][4] == "Bundled":
        il_bund_list.append(data[i][8])

il_bund_list.sort()
#print(il_bund_list)


bundled_rates = []
for i in range(len(data)):
    if data[i][4] == "Bundled" and data[i][3] == "IL":
        bundled_rates.append(power_data[i][8])

median = statistics.median(bundled_rates)

print("The median bundled residential rate in Illinois is", median, "\n")

# -------- Problem #3 -------- #

#Putting zip code file into a readable list
zip_codes_list = []
reader = csv.reader(file2, delimiter = ',')
for line in reader:
    zip_codes_list.append(line)
#print(zip_codes_list)

#Creating a list for the all of the Illinois, bundled information
il_bund_res = []
for i in range(len(power_data)):
    if power_data[i][3] == "IL" and power_data[i][4] == "Bundled":
        il_bund_res.append(power_data[i])
#print(il_bund_res)

#Identifying the highest and lowest rates
lowest_rate_zip = il_bund_res[0][0]
highest_rate_zip = il_bund_res[len(il_bund_res)-1][0]

#Ordering the lists and finding the city which correlates with the highest/lowest rate
zip_codes_list.sort(key = itemgetter(0))
for j in zip_codes_list:
    if j[0] == lowest_rate_zip:
        lowest_city = j[2]
        print("The city in Illinois with the lowest residential rate is " + str(lowest_city))
    elif j[0] == highest_rate_zip:
        highest_city = j[2]
        print("The city in Illinois with the highest residential rate is " + str(highest_city))


# -------- Problem #4 (easier) -------- #
#Making different lists for longitude, latitude, size, and more specific zip_code information
longitude_list = []
latitude_list = []
new_zip_list = []
size_list = []

for i in range(len(zip_codes_list)):
    if zip_codes_list[i][3] == "IL":
        if zip_codes_list[i][10]:
            longitude_list.append(zip_codes_list[i][6])
            latitude_list.append(zip_codes_list[i][5])
            new_zip_list.append((zip_codes_list[i][0]))
            size_list.append(float(zip_codes_list[i][10])/90)

#Visual effects: plotting, sizing
plt.figure(1, figsize=[4.3*2, 6.6], tight_layout = True)
plt.subplot(1, 2, 1)
plt.scatter(longitude_list, latitude_list, size_list, alpha = .5)

#Labeling
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Population By Zipcode")

plt.show()





