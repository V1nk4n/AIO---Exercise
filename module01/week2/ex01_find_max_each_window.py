
def find_max_each_window(num_list, window_size):
    max_each_window = []
    n = len(num_list)
    for start in range(n-window_size+1):
        max_each_window.append(max(num_list[start:start+window_size]))

    return max_each_window

assert find_max_each_window([3 , 4 , 5 , 1 , -44] , 3) == [5 , 5 , 5]
num_list = [3 , 4 , 5 , 1 , -44 , 5 ,10 , 12 ,33 , 1]
k  = 3
print(find_max_each_window(num_list, k))