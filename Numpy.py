import numpy as np
random_vector = np.random.uniform(1, 20, 20)  # In the range of 1 to 20 creating a random vector with size 20
print('Random vector of size  20: \n', random_vector)
reshape_array = random_vector.reshape((4, 5))  # changing the array size from 5 to 4
print('Reshaping the  array to 4 by 5: \n', reshape_array)
max_replace = np.where(reshape_array == np.amax(reshape_array, axis=1).reshape(-1, 1), 0, reshape_array)
# changing every max value from each rom to zero using axis=1)
print('Replacing the  maximum in each row by 0: \n', max_replace)