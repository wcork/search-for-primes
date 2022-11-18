import multiprocessing as mp
import time
import sys

# max number to look up to
max_number = 10000
# four processes per cpu
num_processes = mp.cpu_count() * 4


def chunks(seq, chunks):
    size = len(seq)
    start = 0
    for i in range(1, chunks + 1):
        stop = i * size // chunks
        yield seq[start:stop]
        start = stop


def calc_primes(numbers):
    num_primes = 0
    primes = []

    # Loop through each number, then through the factors to identify prime numbers
    for candidate_number in numbers:
        found_prime = True
        for div_number in range(2, candidate_number):
            if candidate_number % div_number == 0:
                found_prime = False
                break
        if found_prime:
            primes.append(candidate_number)
            num_primes += 1
    return num_primes


def main():
    print(num_processes)
    if len(sys.argv) > 1:
        max_number = int(sys.argv[1])

    # Record the test start time
    start = time.time()

    pool = mp.Pool(num_processes)

    # 0 and 1 are not primes
    parts = chunks(range(2, max_number, 1), num_processes)
    # run the calculation
    results = pool.map(calc_primes, parts)
    total_primes = sum(results)

    pool.close()

    # Once all numbers have been searched, stop the timer
    end = round(time.time() - start, 2)

    # Display the results, uncomment the last to list the prime numbers found
    print('Find all primes up to: ' + str(max_number) + ' using ' + str(num_processes) + ' processes.')
    print('Time elasped: ' + str(end) + ' seconds')
    print('Number of primes found ' + str(total_primes))


if __name__ == "__main__":
    main()
