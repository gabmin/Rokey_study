import seaborn as sns
import matplotlib.pyplot as plt

# sns.set_theme(style="darkgrid")

# import numpy as np
#
# data_list = np.random.normal(loc=50, scale=10, size=1000)
#
# sns.histplot(data_list, kde=True)
#
# plt.show()


# tips = sns.load_dataset("tips")
#
# sns.boxplot(tips, x="day", y="total_bill", hue="day")
#
# plt.show()


import cv2

image = cv2.imread("./sample.jpg")
re_image = cv2.resize(image, (600, 400))
edges = cv2.Canny(re_image, 100, 200)

cv2.imshow("image", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
