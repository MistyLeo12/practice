import time
import concurrent.futures
 
start = time.perf_counter()

def doSomething(seconds):
    print(f"Waiting {seconds} second(s)")
    time.sleep(seconds)
    return "Done Waiting"

with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [5, 4, 3, 2, 1]
    results = executor.map(doSomething, seconds)
    for x in results:
        print(x)
    

# Pre 3.2 way of doing threading using threading in std lib
# for _ in range(100):
#     t = threading.Thread(target=doSomething, args=[12])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} seconds")