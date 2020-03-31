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

# variable
covid = Covid()

# Define a function
def displayMessage():
	print("--------------------------------")
	print("*** Akwaba Abidjan Python: Information About Covid19 . GOD Bless You !")
	print("--------------------------------")

def  getStatusByCountryName(countryName):
		country_cases = covid.get_status_by_country_name(countryName)
	
		print("Covid19 Status :" , countryName, country_cases)
		print("** ** ** **  ** ")

def displayAllCovidData():
	allCovidData = covid.get_data()
	print("Covid data/Contries :" ,allCovidData)

def createSimpleTxtFile(allCovidData):
    f = open("allCovidData.txt", "a")
    f.write(allCovidData)
    f.close()

def main():
	displayMessage()
	getStatusByCountryName("Cote d'Ivoire")
	#italy_cases = covid.get_status_by_country_id(115)
	#displayCovidData()

if __name__ == '__main__':
	main()