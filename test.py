import numpy as np

inter_val = np.array([0,2,4,9])
row3 = np.array([0,8,0,7,0,4,0,9,5])

# np.delete(inter_val, [0])


# removing 0 from inter_val if contained number 0
# if (np.where(inter_val == 0)[0].size != 0):
#   temp = inter_val
#   inter_val = np.delete(temp, [0])

interWithRow3 = np.intersect1d(inter_val, row3, assume_unique=False)

# dummyArr = np.array([], dtype=int)

# turn all value of inter_val that matched with interWithRow3, equal 0
for idx, i in np.ndenumerate(inter_val):
  for j in interWithRow3:
    if (i == j):
      inter_val[idx[0]] = 0

# deleting all element with value of 0, in array inter_val
inter_val = np.sort(inter_val)
while (np.where(inter_val == 0)[0].size != 0):
  temp = inter_val
  inter_val = np.delete(temp, [0])







print("####")
print(inter_val)

# print("----")
# print(interWithRow3)
