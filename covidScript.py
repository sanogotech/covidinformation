# working with functions
#----------------------------------
# Best practices
# 1. Put most code into a function or class
# 2. Use if __name__ == '__main__' .. to control execution of code
# 3. Create a function calles main()  to contain the code we want to run 
# 4. Call Other functions from main() / Algorithm 
# ----------------------------------
# An algorithm is a procedure or formula for solving a problem,
# based on conducting a sequence of specified actions

# https://pypi.org/project/covid/

# Python SDK to get information regarding the novel corona virus 
#provided by Johns Hopkins university and worldometers.info
# import module
from covid import Covid
import time
import json
import csv
import pandas as pd

# variable
covid = Covid()

# Define a function
def displayMessage():
        print("--------------------------------")
        print("*** Akwaba Abidjan Python: Information About Covid19 . GOD Bless You !")
        print("--------------------------------")
        

def convertJsonFileToCsvTabularData():
        print("** ** **  convertJsonFileToCsvTabularData() **  ** ")
        # Opening JSON file and loading the data 
        # into the variable data 
        with open('allCovidData.json') as json_file: 
                allCovidData = json.load(json_file) 


        # now we will open a file for writing 
        allCovidData_file = open('allCovidData.csv', 'w') 
        # create the csv writer object 
        csv_writer = csv.writer(allCovidData_file) 

        # Counter variable used for writing 
        # headers to the CSV file 
        count = 0
        for emp in  allCovidData: 
                if count == 0: 

                        # Writing headers of CSV file 
                        header = emp.keys() 
                        csv_writer.writerow(header) 
                        count += 1

                # Writing data of CSV file 
                csv_writer.writerow(emp.values()) 

        allCovidData_file.close()
        
def convertAllCovidDataCsvToExcel ():
        print("** ** **  convertAllCovidDataCsvToExcel() **  ** ")
        read_csvfile = pd.read_csv (r'allCovidData.csv')
        read_csvfile.to_excel (r'allCovidData.xlsx', index = None, header=True)
                
        
def getStatusByCountryName(countryName):
        print("** ** **  getStatusByCountryName **  ** ")
        country_cases = covid.get_status_by_country_name(countryName)
        print("Covid19 Status :" , countryName, country_cases)
        print("** ** ** **  ** ")
        
def getAllCovidData():
        print("** ** **  getAllCovidData **  ** ")
        allCovidData = covid.get_data()
        return allCovidData 

def displayAllCovidData(allCovidData):
        # Pretty Printing JSON string 
        print("** ** **  displayAllCovidData **  ** ")
        print(json.dumps(allCovidData, indent = 4, sort_keys=True))

def createSimpleJsonFileForAllCovidData(allCovidData):
        print("** ** **  createSimpleJsonFileForAllCovidData **  ** ")
        with open("allCovidData.json", 'w') as json_file:
                json.dump(allCovidData, json_file,indent = 4, sort_keys=True)

def main():
        displayMessage()
        getStatusByCountryName("Cote d'Ivoire")
        #italy_cases = covid.get_status_by_country_id(115)
        allCovidData  = getAllCovidData()
        createSimpleJsonFileForAllCovidData(allCovidData)
        convertJsonFileToCsvTabularData()
        convertAllCovidDataCsvToExcel()
        sleepSeconds = 10
        print("Pause : ", sleepSeconds, "seconds")
        time.sleep(sleepSeconds)
        displayAllCovidData(allCovidData)

if __name__ == '__main__':
        main()