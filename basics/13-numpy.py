import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr)
print(arr.shape)
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)

zero_arr = np.zeros([10, 10, 10])
print(zero_arr.shape)

# ones_arr = np.ones(10)
# print(ones_arr)

empty_arr = np.empty(10)
print(empty_arr)

rand_arr = np.random.randint(0, 101, size=10)
print(rand_arr)
rand_arr_2 = np.random.random(10)
print(rand_arr_2)

print(rand_arr)
print('min', np.min(rand_arr))
print('max', np.max(rand_arr))
print('min index', np.argmin(rand_arr))
print('max index', np.argmax(rand_arr))
print('sum', np.sum(rand_arr))
print('mean', np.mean(rand_arr))
print('std', np.std(rand_arr))
print('var', np.var(rand_arr))


def calculate_stat_values(num_list):
    arr = np.array(num_list)
    return {
        'min': np.min(arr),
        'max': np.max(arr),
        'sum': np.sum(arr),
        'mean': np.mean(arr),
        'std': np.std(arr)
    }


print(calculate_stat_values([23, 45, 457, 23, 7, 26, 73]))
