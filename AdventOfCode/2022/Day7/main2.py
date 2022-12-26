def readdir(lines_iter):
    dir = {}
    while True:
        line = next(lines_iter, None)
        if line == None:
            return dir
        line = line.strip()
        if line.startswith("$ cd"):
            command = line.split(" ")[2]
            if command == "..":
                return dir
            else:
                dir[command] = readdir(lines_iter)
        if not line.startswith("$") and not line.startswith("dir"):
            size = int(line.split(" ")[0])
            dir.setdefault("size", 0)
            dir["size"] += size


def cal_size(dir: dict):
    if len(dir) == 1 and "size" in dir:
        return dir["size"]
    size = 0
    for k, v in dir.items():
        if k != "size":
            size += cal_size(v)
    dir.setdefault("size", 0)
    dir["size"] += size
    return dir["size"]


def cal_result(dir, need):
    if len(dir) == 1 and dir["size"] >= need:
        return dir["size"]

    minimum = 70_000_000
    for k, v in dir.items():
        if k != "size":
            value = cal_result(v, need)
            if value < minimum:
                minimum = value
    if dir["size"] >= need and dir["size"] < minimum:
        minimum = dir["size"]
    return minimum


def main():
    with open("data.txt") as file:
        result = 0
        lines = file.readlines()
        result = readdir(iter(lines))
        cal_size(result)
        total = result["/"]["size"]
        left = 70_000_000 - total
        need = 30_000_000 - left
        print(total, left, need)
        print(cal_result(result, need))


if __name__ == "__main__":
    main()
