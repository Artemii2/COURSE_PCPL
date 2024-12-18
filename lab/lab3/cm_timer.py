from contextlib import contextmanager
import time

class cm_timer_1:
       def __enter__(self):
           self.start_time=time.time()
           return self  

       def __exit__(self, exc_type, exc_value, traceback):
             end_time=time.time()
             print(f"Время выполнения cm_timer_1: {end_time - self.start_time:.6f} секунд")

        
@contextmanager
def cm_timer_2():
    start_time = time.time()  
    yield  
    end_time = time.time()  
    print(f"Время выполнения cm_timer_2: {end_time - start_time:.6f} секунд")


if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(5.5)

    with cm_timer_2():
         time.sleep(5.5)