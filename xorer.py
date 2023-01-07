import sys
import os


def validate_arguments():
    if not len(sys.argv) == 3:
        print("Need two arguments: inputfile outputfile")
        exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    if not os.path.exists(input_path):
        print(f"No such file as {input_path}")
        exit(1)
    
    if os.path.exists(output_path):
        print(f"Are you sure you want to overwrite {output_path}")
        is_sure = input("y/n ").lower()
        
        if is_sure != "y":
            exit(1)
            
    return input_path, output_path


def load_file(input_file):
    with open(input_file, "rb") as f:
        input_in_bytes = f.read()
    return input_in_bytes


def xor_bytes(input_in_bytes):
    return [bytes((byte ^ 69,)) for byte in input_in_bytes]


def save_file(xored_file_data, output_file):
    with open(output_file, "wb") as out:
        for byte in xored_file_data:
            out.write(byte)
    return


def main():
    input_file, output_file = validate_arguments()
    input_in_bytes = load_file(input_file)
    xored_file_data = xor_bytes(input_in_bytes)
    save_file(xored_file_data, output_file)
    return


main()
