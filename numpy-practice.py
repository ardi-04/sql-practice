import numpy as np

grades = np.array([[90, 99, 80,70], [100,67,54,87],[95,76,77,88], [50,74,33,98]])
print(np.average(grades, axis=1))

def analyze_class(grades):

    studDict = {'top_student' : np.argmax(np.average(grades, axis=1)), 
    'hardest_exam' :  np.argmin(np.average(grades, axis=0)), 
    'passing_stundents' : np.argwhere(np.average(grades, axis=1) >= 75) ,
    'class_average' : np.round(np.average(grades), decimals=2) ,
    'normalized' : np.round((grades - np.min(grades)) / (np.max(grades) - np.min(grades)), decimals=2)}

    return studDict

print(analyze_class(grades))