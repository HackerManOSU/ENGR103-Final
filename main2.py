import pandas as pd
import numpy as np
import mainlibrary as ml
import math
import matplotlib.pyplot as mpl
import operator

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

amountNeighborhoods = crimeData['Neighborhood'].nunique()

print(f'This data collection splits portland into and polls from {amountNeighborhoods} unique neighborhoods')

#Compare neighborhoods using nunique function to generate array

allNeighborhoods = crimeData['Neighborhood'].unique()

tester = []

print(neighborhood)

grouped = crimeData.groupby('Neighborhood')['Case Number'].apply(list)

for neighborhood, case_numbers in grouped.items():

    print(f"{neighborhood}: {len(case_numbers)} cases")



Eastmoreland = []
Eliot =[]
FarSouthwest =[]
ForestPark =[]
FosterPowell =[]
Glenfair =[]
GooseHollow =[]
GrantPark =[]
HaydenIsland =[]
Hazelwood =[]
Portsmouth =[]
Overlook =[]
Parkrose =[]
ParkroseHeights =[]
Pearl =[]
Piedmont =[]
PleasantValley =[]
PowellhurstGilbert =[]
Reed =[]
Richmond =[]
RoseCityPark =[]
Roseway =[]
Russell =[]
SellwoodMoreland =[]
SouthPortland =[]
SouthTabor =[]
StJohns =[]
SullivansGulch =[]
Sumner =[]
Sunderland =[]
Sunnyside =[]
UniversityPark =[]
WestPortlandPark =[]
Wilkes =[]
Woodlawn =[]
Woodstock =[]
ArborLodge =[]
Argay =[]
ArnoldCreek =[]
Ashcreek =[]
BeaumontWilshire =[]
Boise =[]
BrentwoodDarlington =[]
Bridgeton =[]
Bridlemile =[]
Brooklyn =[]
BuckmanEast =[]
BuckmanWest =[]
CathedralPark =[]
Centennial =[]
Concordia =[]
CrestonKenilworth =[]
Crestwood =[]
Cully =[]
Hillsdale =[]
Hillside =[]
HosfordAbernethy =[]
Irvington =[]
Kenton =[]
Kerns =[]
King =[]
Lents =[]
Linnton =[]
Lloyd =[]
MarshallPark =[]
MillPark =[]
Montavilla =[]
MtScottArleta =[]
MtTabor =[]
NorthTabor =[]
Northwest =[]
OldTownChinatown =[]
Sabin =[]
Downtown =[]
Hollywood =[]
Humboldt =[]
MadisonSouth =[]
Multnomah =[]
Hayhurst =[]
SylvanHighlands =[]
Alameda =[]
ArlingtonHeights =[]
SouthwestHills =[]
Maplewood =[]
Homestead =[]
CollinsView =[]
EastColumbia =[]
Vernon =[]
Laurelhurst =[]
Ardenwald =[]
NorthwestIndustrial =[]
WoodlandPark =[]
NorthwestHeights =[]
SouthBurlingame =[]
Markham =[]
HealyHeights =[]

allNeighborhoodArrays = [Eastmoreland, Eliot, FarSouthwest, ForestPark, FosterPowell, Glenfair, GooseHollow, GrantPark, HaydenIsland, Hazelwood, Portsmouth, Overlook, Parkrose, ParkroseHeights, Pearl, Piedmont, PleasantValley, PowellhurstGilbert, Reed, Richmond, RoseCityPark, Roseway, Russell, SellwoodMoreland, SouthPortland, SouthTabor, StJohns, SullivansGulch, Sumner, Sunderland, Sunnyside, UniversityPark, WestPortlandPark, Wilkes, Woodlawn, Woodstock, ArborLodge, Argay, ArnoldCreek, Ashcreek, BeaumontWilshire, Boise, BrentwoodDarlington, Bridgeton, Bridlemile, Brooklyn, BuckmanEast, BuckmanWest, CathedralPark, Centennial, Concordia, CrestonKenilworth, Crestwood, Cully, Hillsdale, Hillside, HosfordAbernethy, Irvington, Kenton, Kerns, King, Lents, Linnton, Lloyd, MarshallPark, MillPark, Montavilla, MtScottArleta, MtTabor, NorthTabor, Northwest, OldTownChinatown, Sabin, Downtown, Hollywood, Humboldt, MadisonSouth, Multnomah, Hayhurst, SylvanHighlands, Alameda, ArlingtonHeights, SouthwestHills, Maplewood, Homestead, CollinsView, EastColumbia, Vernon, Laurelhurst, Ardenwald, NorthwestIndustrial, WoodlandPark, NorthwestHeights, SouthBurlingame, Markham, HealyHeights,]

monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] #For zip print statement