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


def cal_result(dir):
    if len(dir) == 1 and dir["size"] < 100000:
        return dir["size"]

    result = 0
    for k, v in dir.items():
        if k != "size":
            result += cal_result(v)
    if dir["size"] < 100000:
        result += dir["size"]
    return result


def main():
    with open("data.txt") as file:
        result = 0
        lines = file.readlines()
        result = readdir(iter(lines))
        cal_size(result)

        print(cal_result(result))


if __name__ == "__main__":
    main()
