import seaborn as sns
import matplotlib.pyplot as plt


# tips = sns.load_dataset("tips")
# print(tips.head())
#
# g = sns.FacetGrid(tips, col="sex", hue="time")
# g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
# g.add_legend()
#
# plt.show()


iris = sns.load_dataset("iris")
g = sns.FacetGrid(iris, col="species", height=4, aspect=1)
g.map_dataframe(sns.histplot, x="sepal_length", kde=True)
g.set_titles("{col_name}")
g.add_legend()

plt.show()
