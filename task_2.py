import multiprocessing
import time


# Реалізація синхронної версії функції "factorize"
def factorize(num):
    start_time = time.time()  # Початок вимірювання часу
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    end_time = time.time()  # Кінець вимірювання часу 
    print("Функція 'factorize' виконалась за:", end_time - start_time, "секунд")
    return factors

# Реалізуємо асинхронну версію функції "factorize" використовуючи паралельні обчислення 
# з використанням кількох ядер процесора
def factorize_parallel(*numbers):
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    results = pool.map(factorize, numbers)
    pool.close()
    pool.join()
    return results


if __name__ == '__main__':
    multiprocessing.freeze_support()


    start_time = time.time()
    a, b, c, d = factorize_parallel(128, 255, 99999, 10651060)
    end_time = time.time()
    print("Асинхронна версія виконалась за:", end_time - start_time, "секунд")

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158,
             304316, 380395, 532553, 760790, 1065106, 1521580, 2130212,
             2662765, 5325530, 10651060]