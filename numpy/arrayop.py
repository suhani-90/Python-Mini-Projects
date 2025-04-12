import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])
arr2d=np.array([[1,2,3,4,5],[6,7,8,9,10]])

#append
new_arr=np.append(arr,[20,30,40])
print(new_arr)
#add
np.insert(arr,4,23)
np.insert(arr2d,1,3,23)

#delete

#update