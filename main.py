print("Starting banker's algorithm")

n = 5  # Number of processes
m = 3  # Number of resource types

# Available Vector (initially total resources available)
available = [3, 3, 2]

# Maximum Matrix
max = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]

# Allocation Matrix
allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

# Need Matrix (Max – Allocation)
need = [
    [7, 4, 3],
    [1, 2, 2],
    [6, 0, 0],
    [0, 1, 1],
    [4, 3, 1]
]

finished = [False] * n

"""
algorithm is to find something where need <= avail for all resources
allocate said resources to the process which means the process is finished
add the max back to the available
repeat until all processes are finished

well define each row to be a process and each column to be a resource
"""
def can_finish(process_index, available):
    # determien if need[resource indx] <= available for all resources of soem process pi
    for ri in range(len(available)):
        if need[process_index][ri] > available[ri]:
            return False
    return True

def find_process_to_finish(available):
    # find the first process whicih has need <= available for all resources
    for pi in range(len(need)):
        if finished[pi]:
            continue
        if can_finish(pi, available):
            return pi
    return -1

def finish_process(process_index, available):
    # reclaim the allocated resources
    for ri in range(len(available)):
        available[ri] += allocation[process_index][ri]
    finished[process_index] = True


def request_resources(process_index, request):
    # check if we can request the resource then perform the reqeust
    for ri in range(len(request)):
        if request[ri] > need[process_index][ri]:
            raise Exception("Request is greater than need for process " + str(process_index))
        if request[ri] > available[ri]:
            raise Exception("Not enough resources available")
    # perform the request
    for ri in range(len(request)):
        available[ri] -= request[ri]
        allocation[process_index][ri] += request[ri]

def test_safe_sequence(sequence):
    for pi in sequence:
        if finished[pi]:
            continue
        if can_finish(pi, available):
            finish_process(pi, available)
        else:
            return False
    return True 

def find_safe_sequence():
    global available, need, allocation, finished
    # need to copy bc were gonna mutate it 
    temp_available = available.copy()
    temp_need = need.copy()
    temp_allocation = allocation.copy()
    temp_finished = finished.copy()
    temp_sequence = []

    while len(temp_sequence) < n:
        pi = find_process_to_finish(temp_available)
        if pi == -1:
            return None
        temp_sequence.append(pi)
        finish_process(pi, temp_available)

    # restore the original values
    available = temp_available
    need = temp_need
    allocation = temp_allocation
    finished = temp_finished

    return temp_sequence

def main():
    # main loop
    while True:
        print("1. Find safe sequence")
        print("2. Request resources")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(find_safe_sequence())
        elif choice == 2:
            process_index = int(input("Enter the process index: "))
            request = list(map(int, input("Enter the request: ").split()))
            try:
                request_resources(process_index, request)
                print("Request successful")
                print(find_safe_sequence())
            except Exception as e:
                print(e)
        elif choice == 3:
            break
    print(find_safe_sequence())
main()