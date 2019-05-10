from multiprocessing import Pool
import time
import random

def proc_t(num):
    sec = random.randint(0,15)
    time.sleep(sec)
    print("proc %s sleep %s sec"%(num,sec))

if __name__ == '__main__':
    pool = Pool(4)
    for i in range(10):
        print("proc %s start"%(i,))
        pool.apply_async(proc_t,args=(i,))

    pool.close()
    pool.join()