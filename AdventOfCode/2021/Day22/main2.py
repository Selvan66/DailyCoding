class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"{self.x[0]} {self.x[1]} {self.y[0]} {self.y[1]} {self.z[0]} {self.z[1]}"

    def __hash__(self) -> int:
        return hash((tuple(self.x), tuple(self.y), tuple(self.z)))

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y and self.z == __o.z

    def get_width(self) -> int:
        return self.x[1] - self.x[0]

    def get_height(self) -> int:
        return self.y[1] - self.y[0]

    def get_deep(self) -> int:
        return self.z[1] - self.z[0]

    def get_volume(self) -> int:
        return self.get_width() * self.get_height() * self.get_deep()

    def point_is_intersect(self, point) -> bool:
        if self.x[0] > point[0] or point[0] > self.x[1]:
            return False
        if self.y[0] > point[1] or point[1] > self.y[1]:
            return False
        if self.z[0] > point[2] or point[2] > self.z[1]:
            return False
        return True

    def point_inside_box(self, point) -> bool:
        if self.x[0] >= point[0] or point[0] >= self.x[1]:
            return False
        if self.y[0] >= point[1] or point[1] >= self.y[1]:
            return False
        if self.z[0] >= point[2] or point[2] >= self.z[1]:
            return False
        return True

    def point_on_box(self, point) -> bool:
        return self.point_is_intersect(point) and not self.point_inside_box(point)

    def is_intersect(self, box) -> bool:
        counter = 0
        for x in box.x:
            for y in box.y:
                for z in box.z:
                    if self.point_inside_box([x, y, z]):
                        return True
                    if self.point_on_box([x, y, z]):
                        counter += 1
        return counter > 4

    def is_intersect_box(self, box) -> bool:
        if (self.x[1] <= box.x[0]) or (box.x[1] <= self.x[0]) or (self.z[1] <= box.z[0]) or (box.z[1] <= self.z[0]) or (self.y[1] <= box.y[0]) or (box.y[1] <= self.y[0]):
            return False
        return True

    def split_by_point(self, point):
        if not self.point_is_intersect(point):
            return set()
        result = set()
        # Front
        result.add(Box([self.x[0], point[0]], [
            self.y[0], point[1]], [self.z[0], point[2]]))
        result.add(Box([point[0], self.x[1]], [
            self.y[0], point[1]], [self.z[0], point[2]]))
        result.add(Box([self.x[0], point[0]], [
            point[1], self.y[1]], [self.z[0], point[2]]))
        result.add(Box([point[0], self.x[1]], [
            point[1], self.y[1]], [self.z[0], point[2]]))

        # Back
        result.add(Box([self.x[0], point[0]], [
            self.y[0], point[1]], [point[2], self.z[1]]))
        result.add(Box([point[0], self.x[1]], [
            self.y[0], point[1]], [point[2], self.z[1]]))
        result.add(Box([self.x[0], point[0]], [
            point[1], self.y[1]], [point[2], self.z[1]]))
        result.add(Box([point[0], self.x[1]], [
            point[1], self.y[1]], [point[2], self.z[1]]))

        return {i for i in result if i.x[0] != i.x[1] and i.y[0] != i.y[1] and i.z[0] != i.z[1]}

    def split_box_if_arg_intersect(self, arg):
        all_box = set()
        queue = [self]
        while len(queue) > 0:
            value = queue.pop(0)
            for x in arg.x:
                for y in arg.y:
                    for z in arg.z:
                        result = value.split_by_point([x, y, z])
                        if len(result) > 1:
                            queue.extend([i for i in result])
                            all_box.update(result)

        ret = set()
        for i in all_box:
            to_add = True
            for j in all_box:
                if i == j:
                    continue
                if arg.is_intersect(i) or (i.is_intersect(j) and i.get_volume() > j.get_volume()):
                    to_add = False
                    break
            if to_add:
                ret.add(i)

        return ret

    def split_box_if_self_intersect_and_not_box(self, box):
        new_box = Box([max(self.x[0], box.x[0]), min(self.x[1], box.x[1])], [max(self.y[0], box.y[0]), min(
            self.y[1], box.y[1])], [max(self.z[0], box.z[0]), min(self.z[1], box.z[1])])
        if new_box == self:
            return set()
        return self.split_by_box(new_box)

    def split_by_box(self, box):
        if self.is_intersect(box):
            return self.split_box_if_arg_intersect(box)
        elif box.is_intersect_box(self):
            return self.split_box_if_self_intersect_and_not_box(box)
        return {self}


def parse_line(line: str):
    mods = line.split(" ")
    mod = mods[0]
    ranges = mods[1].split(",")
    x = ranges[0].split("=")[1].split("..")
    y = ranges[1].split("=")[1].split("..")
    z = ranges[2].split("=")[1].split("..")

    x = [int(x[0]), int(x[1]) + 1]
    y = [int(y[0]), int(y[1]) + 1]
    z = [int(z[0]), int(z[1]) + 1]

    return (mod == "on", x, y, z)


def main():
    with open("data.txt") as file:
        all_box = set()
        for line in file.readlines():
            line = line.strip()
            (mod, x, y, z) = parse_line(line)
            print(mod, x, y, z)
            new = Box(x, y, z)
            if len(all_box) < 1:
                all_box.add(new)
                continue

            temp_set = set()
            for box in all_box:
                temp_set.update(box.split_by_box(new))

            if mod:
                temp_set.add(new)
            all_box = temp_set

        sum_volume = 0
        for box in all_box:
            sum_volume += box.get_volume()
        print(sum_volume)


if __name__ == "__main__":
    main()
