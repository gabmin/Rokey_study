import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")


sns.set_theme(style="whitegrid", palette="colorblind")

# 산점도
sns.scatterplot(data=iris, x="sepal_length", y="sepal_width", hue="species")

# 선형 회귀선
# sns.lmplot(data=iris, x="sepal_length", y="sepal_width", hue="species", height=6)

# 히스토그램
# sns.histplot(data=iris, x="sepal_length", hue="species", kde=True)

# 상자 그림
# sns.boxplot(data=iris, x="sepal_length", y="sepal_width")

# 바이올린 플롯
# sns.violinplot(data=iris, x="sepal_length", y="sepal_width", inner="quart")

# 페어 플롯
# sns.pairplot(data=iris, hue="species")


plt.title("Iris Dataset")

plt.show()
