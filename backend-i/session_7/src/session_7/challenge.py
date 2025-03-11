from contextlib import contextmanager
import logging

@contextmanager
def open_file(filename, mode):
    print(f"Opening file {filename}")
    f = open(filename, mode)
    try:
        yield f

    except Exception as e:
        logging.error(f"Exception occurred while handling file {filename}: {e}")
    finally:
        print(f"Closing file {filename}")
        f.close()


if __name__ == "__main__":
    with open_file("example.txt", "a") as f:
        try:
            f.write("\nAppending with context manager using @contextmanager.")
        except Exception as e:
            print(f"Caught exception: {e}")