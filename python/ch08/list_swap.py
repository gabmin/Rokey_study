ca = [10, 11]
print("ca[0] =", ca[0])
print("ca[1] =", ca[1])

temp = ca[0]
ca[0] = ca[1]
ca[1] = temp

print("ca[0] =", ca[0])
print("ca[1] =", ca[1])


cb = [10, 11]
cc = cb
print("cb[0] =", cb[0])
print("cb[1] =", cb[1])
print("cb id값:", id(cb))
print("cc id값:", id(cc))
print("cb[0] id값:", id(cb[0]))
print("cc[0] id값:", id(cc[0]))

cc[0] = 20
print("cb[0] id값:", id(cb[0]))
print("cc[0] id값:", id(cc[0]))
temp = cc[0]
cc[0] = cc[1]
cc[1] = temp

print("cb =", cb)
print("cc =", cc)
