from pathlib import Path
from collections import defaultdict


def get_absolute_cd_path(path_string: Path, pwd: Path) -> Path:
    return path_string if path_string.is_absolute() else Path((pwd / path_string).resolve())

folders = defaultdict(lambda: 0)
current_directory = Path("/")

with open("input") as input_file:
    for line_with_newline in input_file:
        line = line_with_newline[:-1]
        if line.startswith("$ cd"):
            current_directory = get_absolute_cd_path(Path(line[5:]), current_directory)
        elif line[0].isdigit():
            size = int(line.split(" ")[0])
            folders[current_directory] += size
            for parent in current_directory.parents:
                folders[Path(parent)] += size

minimum_disk_space_to_free_up = 30000000 - (70000000 - folders[Path("/")])

print(sum(size for size in folders.values() if size <= 100000))
print(min(size for size in folders.values() if size >= minimum_disk_space_to_free_up))