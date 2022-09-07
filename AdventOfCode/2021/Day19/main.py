import math

def parse():
    with open("data.txt") as file:
        i = -1
        result = []
        for line in file.readlines():
            if line.startswith('---'):
                result.append([])
                i += 1
            elif not line.isspace():
                splited = line.split(',')
                result[i].append((int(splited[0]), int(splited[1]), int(splited[2])))
        return result

def point_distance(lhs, rhs):
    return math.sqrt(pow(lhs[0] - rhs[0], 2) + pow(lhs[1] - rhs[1], 2) + pow(lhs[2] - rhs[2], 2))

def diff_points(lhs, rhs):
    return tuple(a - b for a, b in zip(lhs, rhs))

def add_points(lhs, rhs):
    return tuple(a + b for a, b in zip(lhs, rhs))

def mult_points(lhs, rhs):
    return tuple(a * b for a, b in zip(lhs, rhs))

def distance_list(scanner, index):
    result = set()
    for s in scanner:
        result.add(point_distance(scanner[index], s))
    return result

def transform(scanner, points):
    p00 = points[0][0]
    p01 = points[0][1]
    p10 = points[1][0]
    p11 = points[1][1]
    rotate = [1, 1, 1]
    move = [0, 0, 0]
    column = [0, 1, 2]
    k = 0
    while True:
        diff1 = diff_points(p00, p01)
        diff2 = diff_points(p10, p11)

        rotate = [-1 if diff1[i] != diff2[i] else 1 for i in range(3)]
        r1 = mult_points(rotate, p01)
        r2 = mult_points(rotate, p11)
        p1 = diff_points(p00, r1)
        p2 = diff_points(p10, r2)
        
        if p1 == p2:
            move = p1
            break
        else:
            column[k % 3], column[(k + 2) % 3] = column[(k + 2) % 3], column[k % 3]
            p01 = tuple(points[0][1][j] for j in column)
            p11 = tuple(points[1][1][j] for j in column)
            k += 1

    print(move, rotate, column)
    for i in range(len(scanner)):
        p = tuple(scanner[i][j] for j in column)
        scanner[i] = add_points(mult_points(rotate, p), move)
    return scanner
    

def get_intersection_points(scaner1, scaner2):
    result = []
    for i in range(len(scaner1)):
        point_distance_scanner1 = distance_list(scaner1, i)
        for j in range(len(scaner2)):
            point_distance_scanner2 = distance_list(scaner2, j)
            if len(point_distance_scanner1.intersection(point_distance_scanner2)) >= 12:
                result.append([scaner1[i], scaner2[j]])       
    return result

def main():
    scanners = parse()
    points = set(scanners.pop(0))
    while len(scanners) > 0:
        scanner = scanners.pop(0)
        intersection = get_intersection_points(list(points), scanner);
        if len(intersection) >= 2:
            points.update(transform(scanner, intersection))
        else:
            scanners.append(scanner)
    for p in sorted(points):
        print(p)
    print(len(points))

if __name__ == '__main__':
    main()