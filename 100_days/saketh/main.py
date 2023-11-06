import pandas as pd
import nltk
saketh= pd.read_csv("123.csv")
saketh=pd.DataFrame(saketh)
saketh=saketh.dropna(axis=1, how="all")
saketh.groupby('What are your Professional goals? This is all about you! Some ideas to think about: What do you want to professionally achieve in the next 5 years? Career movement or skill development? Flexible work arrangements, retirement. What does excite you about coming to work? What would excite you about coming to work?e.g., cross-unit project involvement To help you think about your professional goals, try using this tool. LINK| GROW MODEL	')
print(saketh)