import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from numba.tests.npyufunc.test_ufuncbuilding import equals
import matplotlib.patches as mpatches

def plotScatterPlots(finalStats, matchingAttri, title):
    
    x_labels = list(finalStats.keys())
    x_labels.remove(matchingAttri)
    x_labels = np.asarray(x_labels)
    
    y_labels = np.array(["", "", "", "", "", "", "", "", ""])
    
    radii = []
    clr = []
    
    for key in finalStats.keys():
        if key != matchingAttri:
            magni =  finalStats[key]
            if magni < 0:
                clr.append('r')
            elif magni > 0 :
                clr.append('g')
            else: 
                clr.append('y')
            radii.append(abs(magni))
            
    radii = np.asarray(radii)
    area = np.pi * (20 * radii)**2
    clr = np.asarray(clr)
    x = np.arange(9)
    y = np.random.rand(9)
    plt.scatter(x, y, s=area, c=clr, alpha=0.5)
    plt.yticks(y, y_labels, size= 'small')
    plt.xticks(x, x_labels, size='small')
    plt.title(title)
    plt.ylabel(matchingAttri)
    classes = ['Negative Correlation','Positive Correlation']
    colors = ['r', 'g']
    recs = []
    for i in range(0,len(colors)):
        recs.append(mpatches.Rectangle((0,0),1,1,fc=colors[i]))
    plt.legend(recs, classes, loc = 1)
    plt.show()
    

USOpenDF = pd.read_csv("C:/Users/abhin/workspace/DVAssignment1/src/USOpenFinals_2016.csv")

year = USOpenDF['year']
gender = USOpenDF['gender']

USOpenWinner = USOpenDF.filter(regex = '^winner')
USOpenLoser = USOpenDF.filter(regex = '^loser')

USOpenWinner.insert(0, 'year', year)
USOpenWinner.insert(1, 'gender', gender)

USOpenLoser.insert(0, 'year', year)
USOpenLoser.insert(1, 'gender', gender)

USOpenWinnerStats = USOpenWinner.ix[:, 'winner_firstServe':]
USOpenLoserStats = USOpenLoser.ix[:, 'loser_firstServe':]

######## Winner stats ################################
######## converting strings to int ###################

USOpenWinnerStats['winner_firstServe'] = USOpenWinnerStats['winner_firstServe'].map(lambda x: x.rstrip('%'))
USOpenWinnerStats['winner_firstPointWon'] = USOpenWinnerStats['winner_firstPointWon'].map(lambda x: x.rstrip('%'))
USOpenWinnerStats['winner_secPointWon'] = USOpenWinnerStats['winner_secPointWon'].map(lambda x: x.rstrip('%'))
USOpenWinnerStats['winner_break'] = USOpenWinnerStats['winner_break'].map(lambda x: x.rstrip('%'))
USOpenWinnerStats['winner_return'] = USOpenWinnerStats['winner_return'].map(lambda x: x.rstrip('%'))

USOpenWinnerStats[['winner_firstServe', 'winner_firstPointWon', 'winner_secPointWon', 'winner_break', 'winner_return']] = USOpenWinnerStats[['winner_firstServe', 'winner_firstPointWon', 'winner_secPointWon', 'winner_break', 'winner_return']].astype(int)

USOpenWinnerStatsMen = USOpenWinnerStats[0:10]
USOpenWinnerStatsWomen = USOpenWinnerStats[10:]

print("### Winner Men's corr coeff ###")
print((USOpenWinnerStatsMen.corr()['winner_totalPointWon']))
#plotScatterPlots(USOpenWinnerStatsMen.corr()['winner_totalPointWon'], "winner_totalPointWon", "US Open Men's Winners Correlation Coefficient")

print("### Winner Women's corr coeff ###")
print((USOpenWinnerStatsWomen.corr()['winner_totalPointWon']))
#plotScatterPlots(USOpenWinnerStatsWomen.corr()['winner_totalPointWon'], "winner_totalPointWon", "US Open Women's Winners Correlation Coefficient")

######## Loser stats #################################
######## converting strings to int ###################

USOpenLoserStats['loser_firstServe'] = USOpenLoserStats['loser_firstServe'].map(lambda x: x.rstrip('%'))
USOpenLoserStats['loser_firstPointWon'] = USOpenLoserStats['loser_firstPointWon'].map(lambda x: x.rstrip('%'))
USOpenLoserStats['loser_secPointWon'] = USOpenLoserStats['loser_secPointWon'].map(lambda x: x.rstrip('%'))
USOpenLoserStats['loser_break'] = USOpenLoserStats['loser_break'].map(lambda x: x.rstrip('%'))
USOpenLoserStats['loser_return'] = USOpenLoserStats['loser_return'].map(lambda x: x.rstrip('%'))

USOpenLoserStats[['loser_firstServe', 'loser_firstPointWon', 'loser_secPointWon', 'loser_break', 'loser_return']] = USOpenLoserStats[['loser_firstServe', 'loser_firstPointWon', 'loser_secPointWon', 'loser_break', 'loser_return']].astype(int)

USOpenLoserStatsMen = USOpenLoserStats[0:10]
USOpenLoserStatsWomen = USOpenLoserStats[10:]

print("### Loser Men's corr coeff ###")
print((USOpenLoserStatsMen.corr()['loser_totalPointWon']))
#plotScatterPlots(USOpenLoserStatsMen.corr()['loser_totalPointWon'], "loser_totalPointWon", "US Open Men's Runners Correlation Coefficient")

print("### Loser Women's corr coeff ###")
print((USOpenLoserStatsWomen.corr()['loser_totalPointWon']))
#plotScatterPlots(USOpenLoserStatsWomen.corr()['loser_totalPointWon'], "loser_totalPointWon", "US Open Women's Runners Correlation Coefficient")

