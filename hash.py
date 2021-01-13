import hashlib
import sys

if __name__ == "__main__":
    print(hashlib.sha1(sys.argv[1].encode()).hexdigest())