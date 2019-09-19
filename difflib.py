import pandas as pd
pop=pd.read_csv("https://raw.githubusercontent.com/Dimanjan/csv/master/cgdppcMPD.csv",index_col=0)

import difflib
difflib.get_close_matches("sri lnka", pop.columns)
