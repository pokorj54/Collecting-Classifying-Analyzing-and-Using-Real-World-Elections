from preflibtools import instances
from pathlib import Path
from tqdm import tqdm
import glob
import sys

def convert_all(input_folder, output_folder):
    files = glob.glob(f"{input_folder}/**/*.soc", recursive=True)

    for file in tqdm(files):
        with open(file, "r") as f:
            lines = f.readlines()
        instance = instances.OrdinalInstance()
        instance.parse_old(lines)
        out_file = file.replace(input_folder, output_folder)
        Path(out_file).parent.mkdir(exist_ok=True, parents=True)
        instance.write(out_file)

def main():
    if len(sys.argv) != 3:
        print(f"Run this program as ./{sys.argv[0]} folder new_folder")
        exit(1)
    convert_all(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
