import numpy as np
import pandas as pd


# target CSV is always e.g. 'expDescr_YYYY-MM-DD.csv'.
# here return a string expID = YYYY-MM-DD_XX
# if input is ('expDescr_2022-03-11.csv',1) output is '2022-03-11_01'
def getExpID(targetCSV, site):
    # date = extract date from targetCSV
    # site = zero padded two digit format of site, e.g. '01'
    # expID = date + '_' + site
    # return expID
    date = targetCSV.replace('expDescr_', '')
    datef = date.replace('.csv', '')
    print(datef)
    pew = datef + '_' + '{:02d}'.format(site)
    pass
    return pew


# read in CSV file, extract "Site" column to form the experiment ID then store that with  "Cell_Type" column into both a list and a dictionary
# return the  (list,dictionary) as a tuple
def lxdxCellType(targetCSV):
    # use pandas data  frame to parse excel
    pdFrame = pd.read_csv(targetCSV)
    # get result as a dictionary
    pdDict = pdFrame.to_dict()
    # iterate over pdDict, building lx and dx output structures
    lx = []
    dx = {

    }
    pdDict1 = pdDict[['date']]
    date = pdFrame['date'].values.tolist()
    for count, values in enumerate(pdDict):
        lx.append(values)
        dx[count] = values

    # enumerate the pdDict, building lx and dx as you go: hint1 = type(pdDict['Site']) look at hint1 in the
    # debugger/console. Goal is to combine the site XX with the date from the targetCSV filename hint2 = type(pdDict[
    # 'Cell_Type']) look at hint2 in the debugger/console. Goal is to store cell type with experiment ID,
    # both as a list of tuples and also as a dictionary.

    # KEY CHALLENGE -- use debugger / wits to find the right iterator here spend some time on this. In the in-lab
    # practical we are going to ask you to write a similar iterator but for a different csv spreadsheet... there will
    # be an enumerator just like this on the lab practical...
    for i, j in enumerate(pdDict['Cell_Type']):  # !!! your code here !!!

        # you need the experimentID from the pdDict['Site'] column with the filename to make the experiment ID (see
        # function above) as the key you need the Cell_Type from the pdDict['Cell_Type'] column as the value write
        # this key,value to (1) a list of tuples and (2) a dictionary

        # hint, find the site using
        idx = 0  # !!! your code here !!! find the right enumerator above so that e.g. idx = i
        site = pdDict['Site'][idx]  # extract the same row from the Site column for this Cell_Type

        if np.isnan(site):  # sometimes pandas gives us an empty row
            # add your code here so we don't continue this loop and crash
            pass

        # now append the expID,Cell_Type as a tuple to a list of tuples, and add it as a key value pair to the dictionary
        # your code here

    # a tuple is handy for returning multiple values from a single function
    return (lx, dx)


# my zybooks grading script will import your file and call your functions above. if you don't have the
# if __name__ statement (below) then you may get confusing results from your zyBooks scoring....

if __name__ == "__main__":
    # for your debug use only
    # set a breakpoint, see what's what!
    targetCSV = 'expDescr_2022-03-11.csv'
    lxdx = lxdxCellType(targetCSV)

pass
