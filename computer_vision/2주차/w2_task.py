import pandas as pd

name = { "두" : "산", "로" : "키", "부" : "트", "캠" : "프" }
df = pd.DataFrame(list(name.items()), columns=['Key', 'Value'])

print(df)


import numpy as np

A = np.pi / 6
B = np.pi / 4

R = np.array([[np.cos(A), -np.sin(A)],
              [np.sin(A),  np.cos(A)]])

V = np.array([np.cos(B) ,np.sin(B)])

result = np.dot(R, V)

print(result)


x = 10 * np.cos(np.deg2rad(45))
y = 10 * np.sin(np.deg2rad(45))
point = np.array([x, y])

theta = np.deg2rad(30)

R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])


f1 = np.where(x>= 0, 1, 0)


r = 5
theta = np.deg2rad(30)

x = r * np.cos(theta)
y = r * np.sin(theta)

result = np.array([x, y])


x = 3
y = 4

r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)

result = np.array([r, theta])



x, y = 2, 4

r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)

theta_rot = theta + np.deg2rad(60)

x_rot = r * np.cos(theta_rot)
y_rot = r * np.sin(theta_rot)