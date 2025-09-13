import tokenizer_n_logic 
import os, sys

def run_my_language(file_path):

    expected_extension = '.psc'

    if not file_path.endswith(expected_extension):
        print(f"Error:'{expected_extension}' extension error.")
        return

    if not os.path.isfile(file_path):
        print(f"Error:'{file_path}' does not exist.")
        return

    try:
        with open(file_path, 'r') as file:
            code = file.read()
            tokenizer_n_logic.tokenizer(code)
            

    except Exception as e:
            print(f"{e}")

if __name__ == "__main__":

    if len(sys.argv) != 2:
        file_path = input("enter file path: ")
    else:
        file_path = sys.argv[1]
    run_my_language(file_path)
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nexiting program.")
