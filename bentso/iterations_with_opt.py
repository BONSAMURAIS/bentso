import pandas as pd
from bentso import CachingDataClient
from storage_abstract_model import *

c = CachingDataClient()

def InterateCountriesProduction(year):
    # toogle countries vector; short one just for test
    countries = ['AT','BA','BE','BG','BY','CH','CZ','DE','DK','EE','ES','FI','FR','GB','GB-NIR','GR','HR','HU','IE','IT','LT','LU','LV','ME','MK','MT','NL','NO','PL','PT','RO','RS','RU','RU-KGD','SE','SI','SK','TR','UA'];
    mom = list()
    country_not_included = {}
    for ctr in countries:
        try:
            ctr_year = c.get_generation(ctr, year)
        except:
            print('error after querring ', ctr)
            continue
        try:
            ctr_year = PHS_consumption_subtraction(ctr,year)
        except:
            print('error after opt ',ctr)
            country_not_included[ctr] = year
            continue
        x = ctr_year.sum() # values in MWh
        x = x * 3600
        a = list(x.index)
        s = pd.Series(ctr)
        pap =  pd.DataFrame(data={'technology': list(x.index), 'country': list(s.repeat(len(x.index))), 'energy_MJ': list(x)})
        pap.to_csv('gen_opt/'+'gen_'+ctr+'_'+str(year)+'.csv',index=False)
        mom.append(pap)
        
    f=open("gen_opt/countries_omitted.dat", "w+")
    for k, v in country_not_included.items():
         f.write("Omitted due to error in data of generation or prices during optimization %s := %d; \r\n"%(k,v))
    f.close()
    if len(mom) > 1:
        df = pd.concat(mom, ignore_index=True)
        df.to_csv('gen_opt/'+'gen_'+str(year)+'.csv',index=False)
    else:
        df = pd.DataFrame()
    return(df)
	
def InterateCountriesTrade(year):
    # toogle countries vector; short one just for test
    # countries = ['AT','BA','BE','BG','BY','CH','CZ','DE','DK','EE','ES','FI','FR','GB','GB-NIR','GR','HR','HU','IE','IT','LT','LU','LV','ME','MK','MT','NL','NO','PL','PT','RO','RS','RU','RU-KGD','SE','SI','SK','TR','UA'];
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
