import pandas as pd
import numpy as np
import mainlibrary as ml
import math
import matplotlib.pyplot as mpl
import operator
import seaborn as sns

filePath = "/workspaces/ENGR103-Final/Open_Data_Sheet_data.csv"
crimeData = pd.read_csv(filePath)


caseNumber = crimeData.loc[:, 'Case Number']
crimeAgainst = crimeData.loc[:, 'Crime Against']
neighborhood = crimeData.loc[:, 'Neighborhood']
occurDate = crimeData.loc[:, 'Occur Date']
occurMonthYear = crimeData.loc[:, 'Occur Month Year']
occurTime = crimeData.loc[:, 'Occur Time']
offenseCategory = crimeData.loc[:, 'Offense Category']

crimeData['Occur Month Year'] = pd.to_datetime(crimeData['Occur Month Year']) #Converts date column to a pandas datetime datatype

crimeData.sort_values(by='Occur Month Year', inplace = True) #Sorts dataframe by date column (asceneding)

amountNeighborhoods = crimeData['Neighborhood'].nunique() #Finds number of unique neighborhood values in dataframe

print(f'This data collection splits portland into and polls from {amountNeighborhoods} unique neighborhoods')

monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] #For zip print statement

################################################################## 2015 ########################################################################################

dec2015 = []
nov2015 = []
oct2015 = []
sep2015 = []
aug2015 = []
jul2015 = []
jun2015 = []
may2015 = []

for i in range(len(occurMonthYear)) :
    if occurMonthYear[i] == "5/1/2015" :
        may2015.append(caseNumber[i])
    elif occurMonthYear[i] == "6/1/2015" :
        jun2015.append(caseNumber[i])
    elif occurMonthYear[i] == "7/1/2015" :
        jul2015.append(caseNumber[i])
    elif occurMonthYear[i] == "8/1/2015" :
        aug2015.append(caseNumber[i])
    elif occurMonthYear[i] == "9/1/2015" :
        sep2015.append(caseNumber[i])
    elif occurMonthYear[i] == "10/1/2015" :
        oct2015.append(caseNumber[i])
    elif occurMonthYear[i] == "11/1/2015" :
        nov2015.append(caseNumber[i])
    elif occurMonthYear[i] == "12/1/2015" :
        dec2015.append(caseNumber[i])

year2015 = [may2015, jun2015, jul2015, aug2015, sep2015, oct2015, nov2015, dec2015] #Array of new appended arrays
lenYear2015 = ml.lenfunc(year2015) #Function that generates the length (number of crimes) of each month array
monthNames2015 = ['May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ]

for i,j in zip(year2015, monthNames) :
    print(f'There was {len(i)} crimes reported in the month of {j}')

total2015 = []

for i in year2015 :
    total2015.append(len(i))

print(f'There was {np.sum(total2015)} crimes reported in Portland from May - December in 2015')

################################################################## 2016 ########################################################################################

dec2016 = []
nov2016 = []
oct2016 = []
sep2016 = []
aug2016 = []
jul2016 = []
jun2016 = []
may2016 = []
apr2016 = []
mar2016 = []
feb2016 = []
jan2016 = []

year2016 = [jan2016, feb2016, mar2016, apr2016, may2016, jun2016, jul2016, aug2016, sep2016, oct2016, nov2016, dec2016] #Array of new appended arrays

for i in range(len(occurMonthYear)) :
    if occurMonthYear[i] == "1/1/2016" :
        jan2016.append(caseNumber[i]) #adding case number of each crime committed in month of january 2018 and so on
    elif occurMonthYear[i] == "2/1/2016" :
        feb2016.append(caseNumber[i])
    elif occurMonthYear[i] == "3/1/2016" :
        mar2016.append(caseNumber[i])
    elif occurMonthYear[i] == "4/1/2016" :
        apr2016.append(caseNumber[i])
    elif occurMonthYear[i] == "5/1/2016" :
        may2016.append(caseNumber[i])
    elif occurMonthYear[i] == "6/1/2016" :
        jun2016.append(caseNumber[i])
    elif occurMonthYear[i] == "7/1/2016" :
        jul2016.append(caseNumber[i])
    elif occurMonthYear[i] == "8/1/2016" :
        aug2016.append(caseNumber[i])
    elif occurMonthYear[i] == "9/1/2016" :
        sep2016.append(caseNumber[i])
    elif occurMonthYear[i] == "10/1/2016" :
        oct2016.append(caseNumber[i])
    elif occurMonthYear[i] == "11/1/2016" :
        nov2016.append(caseNumber[i])
    elif occurMonthYear[i] == "12/1/2016" :
        dec2016.append(caseNumber[i])

year2016 = [jan2016, feb2016, mar2016, apr2016, may2016, jun2016, jul2016, aug2016, sep2016, oct2016, nov2016, dec2016] #Array of new appended arrays
lenYear2016 = ml.lenfunc(year2016) #Function that generated the length (number of crimes) of each month array for plotting

for i,j in zip(year2016, monthNames) :
    print(f'There was {len(i)} crimes reported in the month of {j}')

total2016 = []

for i in year2016 :
    total2016.append(len(i))

print(f'There was {np.sum(total2016)} crimes reported in Portland in 2016')

################################################################## 2017 ########################################################################################

dec2017 = []
nov2017 = []
oct2017 = []
sep2017 = []
aug2017 = []
jul2017 = []
jun2017 = []
may2017 = []
apr2017 = []
mar2017 = []
feb2017 = []
jan2017 = []

for i in range(len(occurMonthYear)) :
    if occurMonthYear[i] == "1/1/2017" :
        jan2017.append(caseNumber[i]) #adding case number of each crime committed in month of january 2018 and so on
    elif occurMonthYear[i] == "2/1/2017" :
        feb2017.append(caseNumber[i])
    elif occurMonthYear[i] == "3/1/2017" :
        mar2017.append(caseNumber[i])
    elif occurMonthYear[i] == "4/1/2017" :
        apr2017.append(caseNumber[i])
    elif occurMonthYear[i] == "5/1/2017" :
        may2017.append(caseNumber[i])
    elif occurMonthYear[i] == "6/1/2017" :
        jun2017.append(caseNumber[i])
    elif occurMonthYear[i] == "7/1/2017" :
        jul2017.append(caseNumber[i])
    elif occurMonthYear[i] == "8/1/2017" :
        aug2017.append(caseNumber[i])
    elif occurMonthYear[i] == "9/1/2017" :
        sep2017.append(caseNumber[i])
    elif occurMonthYear[i] == "10/1/2017" :
        oct2017.append(caseNumber[i])
    elif occurMonthYear[i] == "11/1/2017" :
        nov2017.append(caseNumber[i])
    elif occurMonthYear[i] == "12/1/2017" :
        dec2017.append(caseNumber[i])

year2017 = [jan2017, feb2017, mar2017, apr2017, may2017, jun2017, jul2017, aug2017, sep2017, oct2017, nov2017, dec2017] #Array of new appended arrays
lenYear2017 = ml.lenfunc(year2017) #Function that generated the length (number of crimes) of each month array

for i,j in zip(year2017, monthNames) :
    print(f'There was {len(i)} crimes reported in the month of {j}')

total2017 = []

for i in year2017 :
    total2017.append(len(i))

print(f'There was {np.sum(total2017)} crimes reported in Portland in 2017')


################################################################## 2017 ########################################################################################

sep2018 = []
aug2018 = []
jul2018 = []
jun2018 = []
may2018 = []
apr2018 = []
mar2018 = []
feb2018 = []
jan2018 = []

for i in range(len(occurMonthYear)) :
    if occurMonthYear[i] == "1/1/2018" :
        jan2018.append(caseNumber[i]) #adding case number of each crime committed in month of january 2018 and so on
    elif occurMonthYear[i] == "2/1/2018" :
        feb2018.append(caseNumber[i])
    elif occurMonthYear[i] == "3/1/2018" :
        mar2018.append(caseNumber[i])
    elif occurMonthYear[i] == "4/1/2018" :
        apr2018.append(caseNumber[i])
    elif occurMonthYear[i] == "5/1/2018" :
        may2018.append(caseNumber[i])
    elif occurMonthYear[i] == "6/1/2018" :
        jun2018.append(caseNumber[i])
    elif occurMonthYear[i] == "7/1/2018" :
        jul2018.append(caseNumber[i])
    elif occurMonthYear[i] == "8/1/2018" :
        aug2018.append(caseNumber[i])
    elif occurMonthYear[i] == "9/1/2018" :
        sep2018.append(caseNumber[i])


year2018 = [jan2018, feb2018, mar2018, apr2018, may2018, jun2018, jul2018, aug2018, sep2018] #Array of new appended arrays
lenYear2018 = ml.lenfunc(year2018) #Function that generated the length (number of crimes) of each month array
monthNames2018 = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September'] #For zip print statement


for i,j in zip(year2018, monthNames2018) :
    print(f'There was {len(i)} crimes reported in the month of {j}')

total2018 = []

for i in year2018 :
    total2018.append(len(i))

print(f'There was {np.sum(total2018)} crimes reported in Portland from January - September in 2018')

################################################################## PLOT ########################################################################################

fig1 = mpl.subplots()

mpl.title('Crime in Portland by Year')
mpl.plot(monthNames2018, lenYear2018, color = 'purple', marker = 'P', label = '2018')
mpl.plot(monthNames, lenYear2017, color = 'blue', marker = 'P', label = '2017')
mpl.plot(monthNames, lenYear2016, color = 'red', marker = 'P', label = '2016')
mpl.plot(monthNames2015, lenYear2015, color = 'green', marker = 'P', label = '2015')
mpl.xlabel('Month')
mpl.ylabel('Cumulative Crime')
mpl.legend()
mpl.show()

#################################################################################################################################################################
                                                                #Section 2#
#################################################################################################################################################################

janArray = [jan2016, jan2017, jan2018]
febArray = [feb2016, feb2017, feb2018]
marArray = [mar2016, mar2017, mar2018]
aprArray = [apr2016, apr2017, apr2018]
mayArray = [may2015, may2016, may2017, may2018]
junArray = [jun2015,jun2016, jun2017, jun2018]
julArray = [jul2015, jul2016, jul2017, jul2018]
augArray = [aug2015, aug2016, aug2017, aug2018]
sepArray = [sep2015, sep2016, sep2017, sep2018]
octArray = [oct2015, oct2016, oct2017]
novArray = [nov2015, nov2016, nov2017]
decArray = [dec2015, dec2016, dec2017]

janCrimeNumbers = ml.lenfunc(janArray)
janMean = np.mean(janCrimeNumbers)
febCrimeNumbers = ml.lenfunc(febArray)
febMean = np.mean(febCrimeNumbers)
marCrimeNumbers = ml.lenfunc(marArray)
marMean = np.mean(marCrimeNumbers)
aprCrimeNumbers = ml.lenfunc(aprArray)
aprMean = np.mean(aprCrimeNumbers)
mayCrimeNumbers = ml.lenfunc(mayArray)
mayMean = np.mean(mayCrimeNumbers)
junCrimeNumbers = ml.lenfunc(junArray)
junMean = np.mean(junCrimeNumbers)
julCrimeNumbers = ml.lenfunc(julArray)
julMean = np.mean(julCrimeNumbers)
augCrimeNumbers = ml.lenfunc(augArray)
augMean = np.mean(augCrimeNumbers)
sepCrimeNumbers = ml.lenfunc(sepArray)
sepMean = np.mean(sepCrimeNumbers)
octCrimeNumbers = ml.lenfunc(octArray)
octMean = np.mean(octCrimeNumbers)
novCrimeNumbers = ml.lenfunc(novArray)
novMean = np.mean(novCrimeNumbers)
decCrimeNumbers = ml.lenfunc(decArray)
decMean = np.mean(decCrimeNumbers)

monthMeans = [janMean, febMean, marMean, aprMean, mayMean, junMean, julMean, augMean, sepMean, octMean, novMean, decMean]
monthMeansDaily = [janMean/31, febMean/28.33333333, marMean/31, aprMean/31, mayMean/31, junMean/30, julMean/31, augMean/31, sepMean/30, octMean/31, novMean/30, decMean/31]

fig2 = mpl.subplots()

mpl.title('Average Crime in Portland by Month (2015-2018)')
mpl.plot(monthNames, monthMeans, color = 'purple', marker = 'P', label = 'Crime')
mpl.xlabel('Month')
mpl.ylabel('Average crime reported')
mpl.legend()
mpl.show()

fig2 = mpl.subplots()

mpl.title('Average Daily Crime in Portland by Month (2015-2018)')
mpl.plot(monthNames, monthMeansDaily, color = 'Red', marker = 'P', label = 'Crime')
mpl.xlabel('Month')
mpl.ylabel('Average crime reported daily')
mpl.legend()
mpl.show()


#################################################################################################################################################################
                                                                #Section 3#
#################################################################################################################################################################


allOffenseTypes = crimeData['Offense Category'].unique()

sexNonforcible = []
sex = []
larceny = []
humanTrafficking = []
pornobscene = []
fraud = []
embezzlement = []
motorVehicleTheft = []
assault = []
counterfeitingForgery = []
prostitution = []
burglary = []
animalCruelty = []
vandalism = []
kidnappingAbduction = []
arson = []
robbery = []
drugNarcotic = []
extortionBlackmail = []
stolenProperty = []
weaponLaw = []
homicide = []
bribery = []
gambling = []

for i in range(len(offenseCategory)) :
    if offenseCategory[i] == 'Sex Offenses, Nonforcible':
        sexNonforcible.append(caseNumber[i])
    elif offenseCategory[i] == 'Sex Offenses':
        sex.append(caseNumber[i])
    elif offenseCategory[i] == 'Larceny Offenses':
        larceny.append(caseNumber[i])
    elif offenseCategory[i] == 'Human Trafficking Offenses':
        humanTrafficking.append(caseNumber[i])
    elif offenseCategory[i] == 'Pornography/Obscene Material':
        pornobscene.append(caseNumber[i])
    elif offenseCategory[i] == 'Fraud Offenses':
        fraud.append(caseNumber[i])
    elif offenseCategory[i] == 'Embezzlement':
        embezzlement.append(caseNumber[i])
    elif offenseCategory[i] == 'Motor Vehicle Theft':
        motorVehicleTheft.append(caseNumber[i])
    elif offenseCategory[i] == 'Assault Offenses':
        assault.append(caseNumber[i])
    elif offenseCategory[i] == 'Counterfeiting/Forgery':
        counterfeitingForgery.append(caseNumber[i])
    elif offenseCategory[i] == 'Prostitution Offenses':
        prostitution.append(caseNumber[i])
    elif offenseCategory[i] == 'Burglary':
        burglary.append(caseNumber[i])
    elif offenseCategory[i] == 'Animal Cruelty Offenses':
        animalCruelty.append(caseNumber[i])
    elif offenseCategory[i] == 'Vandalism':
        vandalism.append(caseNumber[i])
    elif offenseCategory[i] == 'Kidnapping/Abduction':
        kidnappingAbduction.append(caseNumber[i])
    elif offenseCategory[i] == 'Arson':
        arson.append(caseNumber[i])
    elif offenseCategory[i] == 'Robbery':
        sex.append(caseNumber[i])
    elif offenseCategory[i] == 'Drug/Narcotic Offenses':
        drugNarcotic.append(caseNumber[i])
    elif offenseCategory[i] == 'Extortion/Blackmail':
        extortionBlackmail.append(caseNumber[i])
    elif offenseCategory[i] == 'Stolen Property Offenses':
        stolenProperty.append(caseNumber[i])
    elif offenseCategory[i] == 'Weapon Law Violations':
        weaponLaw.append(caseNumber[i])
    elif offenseCategory[i] == 'Homicide Offenses':
        homicide.append(caseNumber[i])
    elif offenseCategory[i] == 'Bribery':
        bribery.append(caseNumber[i])
    elif offenseCategory[i] == 'Gambling Offenses':
        gambling.append(caseNumber[i])

allOffenses = [sexNonforcible, sex, larceny, humanTrafficking, pornobscene, fraud, embezzlement, motorVehicleTheft, assault, counterfeitingForgery, prostitution, burglary, animalCruelty, vandalism, kidnappingAbduction, arson, robbery, drugNarcotic, extortionBlackmail, stolenProperty, weaponLaw, homicide, bribery, gambling]
#Array of newly appended indivudal arrays

lenAllOffenses = ml.lenfunc(allOffenses) #Find the length (amount of case #s) in each array

top6offenses = [larceny, motorVehicleTheft, assault, vandalism, fraud, burglary]
lenTop6Offenses = ml.lenfunc(top6offenses)
top6OffenseTypes = ['Larceny', 'Motor Vehicle Theft', 'Assault', 'Vandalism', 'Fraud', 'Burglary']

height = lenTop6Offenses
bars = top6OffenseTypes

yPos = np.arange(len(bars))

mpl.title('Crime Numbers of the Top 6 Crimes Types in Portland (May 2015 - Sep 2018)')
mpl.bar(yPos, height, color = 'purple')
mpl.xticks(yPos, bars)
mpl.xlabel('Crime Types')
mpl.ylabel('Number of Crimes')
mpl.show()

#Heller