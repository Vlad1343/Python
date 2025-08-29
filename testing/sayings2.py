import sys
from testing.sayings1 import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])
