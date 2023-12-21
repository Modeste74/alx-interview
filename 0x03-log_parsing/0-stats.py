#!/usr/bin/python3
"""Reads the stdin line by line and computes metrics"""
import sys
from collections import defaultdict


def print_statistics(total_file_size, status_codes):
    """This is responsible for printing the total
    size and counts for different codes"""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if code in {200, 301, 400, 401, 403, 404, 405, 500}:
            print(f"{code}: {status_codes[code]}")


def main():
    """main function whwere the core logic
    of the script is"""
    total_file_size = 0
    count = 0
    status_codes = defaultdict(int)

    try:
        for line in sys.stdin:
            parts = line.split()

            if len(parts) > 4:
                status_code, file_size = parts[-2], parts[-1]

                if status_code.isdigit():
                    status_code = int(status_code)
                    if status_code in {200, 301, 400, 401, 403, 404, 405, 500}:
                        status_codes[status_code] += 1

                total_file_size += int(file_size)
                count += 1

                if count % 10 == 0:
                    print_statistics(total_file_size, status_codes)
                    count = 0

    except KeyboardInterrupt:
        pass

    finally:
        print_statistics(total_file_size, status_codes)


if __name__ == "__main__":
    main()
