import pyodbc
import pandas as pd
import seaborn as sns

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'stwssbsql02'
database = 'BAN5733'
username = 'bvenkat'
password = 'bvenkat_2045'
cnxn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
# select 26 rows from SQL table to insert in dataframe.
query_1 = "select  * from dbo.location_Planograms_Overview inner join dbo.Location_Adjustments on dbo.location_Planograms_Overview.store_code=dbo.Location_Adjustments.store_code "

df = pd.read_sql(query_1, cnxn)
print(df.isnull().sum())
print()
df1=df[['Fixture_Name','Total_Fixtures','Fixture_Width(ft)','Department_Name']]
print(df1)
