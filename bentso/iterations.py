import pandas as pd
from bentso import CachingDataClient
c = CachingDataClient()

def InterateCountriesProduction(year):
    # countries = ['AT','BE','BA','BG','HR','CY','CZ','DK','EE','FI','FR','DE','GR','HU','IE','IS','IT','LV','LU','MK','ME','NL','NI','NO','PL','PT','RO','RS','SK','SI','SE','CH'];
    countries = ['ES','FR'];
    mom = list()
    for ctr in countries:
        ctr_year = c.get_generation(ctr, year)
        x = ctr_year.sum() # values in MWh
        x = x * 3600
        a = list(x.index)
        s = pd.Series(ctr)
        pap =  pd.DataFrame(data={'technology': list(x.index), 'country': list(s.repeat(len(x.index))), 'energy_MJ': list(x)})
        mom.append(pap)
    
    df = pd.concat(mom, ignore_index=True)
    return(df)
	
def InterateCountriesTrade(year):
    # countries = ['AT','BE','BA','BG','HR','CY','CZ','DK','EE','FI','FR','DE','GR','HU','IE','IS','IT','LV','LU','MK','ME','NL','NI','NO','PL','PT','RO','RS','SK','SI','SE','CH'];
    countries = ['ES','FR'];
    mom = list()
    for fromCtr in countries:
        for toCtr in countries:
            if(fromCtr != toCtr):
                trd_year = c.get_trade(fromCtr, toCtr, year)
                x = trd_year.sum() * 3600
                pap =  pd.DataFrame(data={'fromCountry': fromCtr, 'toCountry': toCtr, 'energy_MJ':x}, index=[0])
                mom.append(pap)
    
    df = pd.concat(mom, ignore_index=True)
    return(df)