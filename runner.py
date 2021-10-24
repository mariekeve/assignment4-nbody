import os
from time import perf_counter
from nbody import main

steps = 5000;
#steps = 50000;
#steps = 500000;
#steps = 5000000;


start = perf_counter()
os.system(f'c:\\Users\\marie\\git-course-2021\\nbody\\cmake-build-release\\nbody.exe {steps}')
#os.system(f'c:\\Users\\marie\\git-course-2021\\nbody\\cmake-build-debug\\nbody.exe {steps}')
#os.system(f'c:\\Users\\marie\\git-course-2021\\nbody\\dist\\nbody.exe {steps}')
main(steps)
stop = perf_counter()

print(f'Elapsed time: {start} {stop} {stop-start}')



'''
         c++ release     c++ debug   python script  python exe 
5,000       0.020           0.047       0.062       0.448
50,000      0.023           0.087       0.409       1.030
500,000     0.062           0.518       3.778       7.577
5,000,000   0.446           4.628      44.650      66.306
'''