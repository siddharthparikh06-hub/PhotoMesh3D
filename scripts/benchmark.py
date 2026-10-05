import time
from contextlib import contextmanager


@contextmanager
def timer(name):
    start_time = time.perf_counter()

    print()
    print(f"Starting: {name}")

    yield

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    print(f"Completed: {name}")
    print(f"Time taken: {elapsed_time:.2f} seconds")


def main():
    print("PhotoMesh3D - Benchmark Test")
    print("-----------------------------")

    with timer("Example operation"):
        time.sleep(2)

    print()
    print("Benchmark test complete.")


if __name__ == "__main__":
    main()