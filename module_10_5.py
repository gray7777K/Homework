from multiprocessing import Pool
import datetime

def read_info(name):
    all_data =[]
    with open(name, 'r', encoding = 'utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

filenames = [f'./file {number}.txt' for number in range(1, 5)]

start_time = datetime.datetime.now()
for filename in filenames:
    read_info(filename)
finish_time = datetime.datetime.now()
run_time = finish_time - start_time
print(run_time)

if __name__ == '__main__':

    start_time = datetime.datetime.now()
    with Pool(processes = 4) as pool:
        pool.map(read_info, filenames)
    finish_time = datetime.datetime.now()
    run_time = finish_time - start_time
    print(run_time)