    import threading
    import time
    import logging
    
    
    lock = threading.Lock()
    
    
    
    def run(i):
        logging.warning("lock")
        lock.acquire()
        time.sleep(2)
        print(i)
        logging.info("unlock")
        lock.release()
    
    
    def runtest():
        for i in myNames:
            check_threads()
            t = threading.Thread(target=run, args=(i,))
            t.start()
    
    
    with open('testtext', 'r') as f:
        myNames = [line.strip() for line in f]
    #print(myNames)
    
    def check_threads():
        while True:
            if threading.active_count() >= 10:
                pass
               # print("Max Threads excided", threading.active_count())
                time.sleep(5)
                check_threads()
            else:
                break
    runtest()
