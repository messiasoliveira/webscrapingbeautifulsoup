import pandas as pd
import seaborn as sns
soybean = pd.read_csv('./sojasidra.csv')
soybean.head()


sns.set_theme(style="whitegrid")
g = sns.catplot(
 data=soybean, kind="bar",
 x="ano", y="Produção",
 palette="dark", alpha=.6, height=6
)
g.despine(left=True)
g.set_axis_labels("Production (kg/ha)")