# Information About Covid19 . GOD Bless You !")

##  Akwaba Abidjan Python

- "Python Script to get information regarding the novel corona virus " 

https://www.linkedin.com/in/souleymanesanogo/

## Getting Started

https://pypi.org/project/covid/

** Python SDK to get information regarding the novel corona virus provided by Johns Hopkins university and worldometers.info

### Prerequisites

 - Python  3.x (3.6+)

## Pip install

'''
pip install  covid

'''

## Code

'''
def  getStatusByCountryName(countryName):

		country_cases = covid.get_status_by_country_name(countryName)	
		print("Covid19 Status :" , countryName, country_cases)
		
'''

## Run
python  covidScript.py

## Result
