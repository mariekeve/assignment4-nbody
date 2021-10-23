import os
from time import perf_counter
#import nbody.py

steps = 5000;
steps = 50000;
steps = 500000;


start = perf_counter()
#os.system(f'c:\\Users\\marie\\git-course-2021\\nbody\\cmake-build-release\\nbody.exe {steps}')
os.system(f'c:\\Users\\marie\\git-course-2021\\nbody\\cmake-build-debug\\nbody.exe {steps}')
stop = perf_counter()

print(f'Elapsed time: {start} {stop} {stop-start}')