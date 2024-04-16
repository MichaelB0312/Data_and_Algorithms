import numpy as np


'''
# you have data matrix nX2. first column is insertion time of a mission to the cache.
# second col is time of duration in the cache.
# Additionally, we have queries arr. each element is a different time.
# we want for each time, output number of missions in the cache at this query[i] time
'''
# solotion based on data_structure course : Technion bridge capacity
def cache_breadth(data, queries):

    #change duration time to end time
    data[:,1] += data[:,0]
    print(data[:,0].shape)
    #add 0 flag for begin time. 1 flag for end_time
    #begin_time = np.concatenate((data[:,0], np.zeros_like(data[:,0])), axis= 0)
    begin_time = np.vstack((data[:,0],np.zeros_like(data[:,0])))
    end_time = np.vstack((data[:,1],np.ones_like(data[:,1])))
    ord_data = np.hstack((begin_time, end_time))
    #data = np.transpose(data)
    #print(data)
    # now, sort start and end time
    sorted_idx = np.argsort(ord_data[0])
    sorted_data = ord_data[:, sorted_idx]
    #print(sorted_data)

    output_list = []
    for query in queries:
        area = sorted_data[:, sorted_data[0,:] < query]
        missions_num = np.sum(area[1,:] == 0) - np.sum(area[1,:] == 1)
        output_list.append(missions_num)

    return output_list
        #missions_num = np.count(sorted_data<qu)




rows = 3
cols = 4
n = 5
num_queries = 5
# Generate a random matrix of integers between 1 and 10000
begin_time = np.random.randint(1, 1000, size=(n,1))
duration_time = np.random.randint(1, 600, size=(n,1))
queries = np.random.randint(1, 1000, size=(num_queries,1))

data = np.concatenate((begin_time,duration_time), axis=1)
data
queries
out_list = cache_breadth(data, queries)
out_list
print("out_list is:", out_list)