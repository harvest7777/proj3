import copy
"""
ryan tran & phu quach
cecs326 project 3
"""
print("Starting banker's algorithm")

n = 5  # Number of processes
m = 3  # Number of resource types

# Available Vector (initially total resources available)
init_available = [3, 3, 2]

# Maximum Matrix
init_max = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]

# Allocation Matrix
init_allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

# Need Matrix (Max – Allocation)
init_need = [
    [7, 4, 3],
    [1, 2, 2],
    [6, 0, 0],
    [0, 1, 1],
    [4, 3, 1]
]

init_finished = [False] * n

"""
algorithm is to find something where need <= avail for all resources
allocate said resources to the process which means the process is finished
add the max back to the available
repeat until all processes are finished

well define each row to be a process and each column to be a resource
"""
def can_finish(process_index, available, need):
    # determien if need[resource indx] <= available for all resources of soem process pi
    for ri in range(len(available)):
        if need[process_index][ri] > available[ri]:
            return False
    return True

def find_process_to_finish(available, need, finished):
    # find the first process whicih has need <= available for all resources
    for pi in range(len(need)):
        if finished[pi]:
            continue
        if can_finish(pi, available, need):
            return pi
    return -1

def finish_process(process_index, available, need, allocation, finished):
    # reclaim the allocated resources
    for ri in range(len(available)):
        available[ri] += allocation[process_index][ri]
        need[process_index][ri] = 0
    finished[process_index] = True


def request_resources(process_index, request, available, need, allocation, finished):
    # check if we can request the resource then perform the reqeust
    for ri in range(len(request)):
        if request[ri] > need[process_index][ri]:
            raise Exception("Request is greater than need for process " + str(process_index))
        if request[ri] > available[ri]:
            raise Exception("Not enough resources available")

    if need[process_index]  == request:
        print("Request is equal to need for process " + str(process_index))
        finish_process(process_index, available, need, allocation, finished)
        return

    # perform the request
    for ri in range(len(request)):
        available[ri] -= request[ri]
        need[process_index][ri] -= request[ri]
        allocation[process_index][ri] += request[ri]


def find_safe_sequence(available, need, allocation, finished):
    # need to copy bc were gonna mutate it 
    temp_available = available.copy()
    temp_need = copy.deepcopy(need)
    temp_allocation = copy.deepcopy(allocation)
    temp_finished = finished.copy()

    temp_sequence = []

    while (temp_finished).count(True) < n:
        pi = find_process_to_finish(temp_available, temp_need, temp_finished)
        if pi == -1:
            return None
        temp_sequence.append(pi)
        finish_process(pi, temp_available, temp_need, temp_allocation, temp_finished)


    return temp_sequence

def main():
    # main loop
    while True:
        print()
        print("1. Find safe sequence")
        print("2. Request resources")
        print("3. Exit")
        print()
        choice = int(input("Enter your choice: "))
        print()
        if choice == 1:
            print("System in safe state")
            print(f"Safe sequence: {find_safe_sequence(init_available, init_need, init_allocation, init_finished)}")
        elif choice == 2:
            process_index = int(input("Enter the process index: "))
            request = list(map(int, input("Enter the request: ").split()))

            print()
            print(f"# Process {process_index} requested resources: {request}")
            try:
                request_resources(process_index, request, init_available, init_need, init_allocation, init_finished)
                print("System in safe state")
                print("Safe sequence: ", find_safe_sequence(init_available, init_need, init_allocation, init_finished))
                print(f"Resources successfully allocated to process: {process_index}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == 3:
            break
    
def test():
    request_resources(1, [1, 2, 2], init_available, init_need, init_allocation, init_finished)
    print(f"Available: {init_available}")
    print(f"Need: {init_need}")
    print(f"Allocation: {init_allocation}")
    print(f"Finished: {init_finished}")
    print(f"Safe sequence: {find_safe_sequence(init_available, init_need, init_allocation, init_finished)}")

main()
