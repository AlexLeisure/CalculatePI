import sys
import time
from mpmath import mp
from mpmath import mpf

printpi = False

def main(digits) -> int:
    mp.dps = digits
    pi = 4 * ((mpf(4) * mp.atan(mpf(1)/5)) - mp.atan(mpf(1)/239))

    if(printpi):
        mp.pretty = True 
        mp.nprint(pi, digits)

    return 0

if __name__ == '__main__':
    digits = 100000

    t1 = time.perf_counter()
    code = main(digits)
    t2 = time.perf_counter()

    print(f"Calculated pi to {digits} digits in [{t2 - t1:0.4f}] seconds")

    sys.exit(code)

