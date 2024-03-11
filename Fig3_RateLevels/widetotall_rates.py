import pandas as pd

tiered= pd.read_excel('Consolidated Rate Info.xlsx',sheet_name='New-Tiered',nrows=9)
tou=pd.read_excel('Consolidated Rate Info.xlsx',sheet_name='TOU',nrows=9)
evtou = pd.read_excel('Consolidated Rate Info.xlsx',sheet_name='TOU-EV',nrows=9)

with pd.ExcelWriter('Consolidated Rate Info - tall.xlsx') as writer:
    pd.melt(tiered, value_vars=['Tier 1 Rate ($/kWh)','Tier 2 Rate ($/kWh)','Tier 3 Rate ($/kWh)'],
                        id_vars=tiered.columns.difference(['Tier 1 Rate ($/kWh)','Tier 2 Rate ($/kWh)','Tier 3 Rate ($/kWh)']), 
                        var_name='Tier', value_name='Rate ($/kWh)').to_excel(writer,sheet_name='Tiered')

    pd.melt(tou, value_vars=['Low Peak','Mid Peak','Peak'],
                        id_vars=tou.columns.difference(['Low Peak','Mid Peak','Peak']), 
                        var_name='PeakLevel', value_name='Rate ($/kWh)').to_excel(writer,sheet_name='TOU')

    pd.melt(evtou, value_vars=['Low Peak','Mid Peak','Peak'],
                        id_vars=evtou.columns.difference(['Low Peak','Mid Peak','Peak']), 
                        var_name='PeakLevel', value_name='Rate ($/kWh)').to_excel(writer,sheet_name='TOU-EV')