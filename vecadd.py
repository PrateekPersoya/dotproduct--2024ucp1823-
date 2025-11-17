import numpy as np
#<<<<<<< HEAD
A = np.array([1,2,3,4,5]) 
#=======
#A = np.array([1,2,3,4])
#>>>>>>> parallel
C = np.array([1,2,3])
dot = np.dot(A,C)
D = np.array([1,3,5])
# E = np.array([1,7,5])
E = np.array([1,5,7])
# fixed the bug by correcly entering the E
dot = np.dot(A,E)
print(dot)

# fast computing
def compute_dot(A, B):
    return np.dot(A, B)
    
print(f"Tesiting the stash")
#testing the stash again
#Yugoslav changessssss this codeeee🛃️
