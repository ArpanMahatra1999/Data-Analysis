import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use("fivethirtyeight")

country = pd.DataFrame({"Country Name":["Nepal", "India"], 2010:[1,2], 2011:[4,5]})
df = country.head(2)
df = df.set_index(["Country Name"])
sd = df.reindex(columns=[2010, 2011])
db = sd.diff(axis=1)
db.plot(kind='bar')
plt.show()
