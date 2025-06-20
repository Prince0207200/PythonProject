from sys import argv
from src import service

def process_file(file_path):

    with open(file_path, "r") as file:
        for line in file:
            arr = line.strip().split()
            if not arr:
                continue
            command = arr[0]
            if command == "BALANCE":
                service.balance(arr[1], arr[2])
            elif command == "CHECK_IN":
                service.check_in(arr[1], arr[2], arr[3])
            elif command == "PRINT_SUMMARY":
                service.summary()

def main():
    if len(argv) != 2:
        raise Exception("Usage: python main.py <input_file_path>")
    file_path = argv[1]
    process_file(file_path)

if __name__ == "__main__":
    main()
