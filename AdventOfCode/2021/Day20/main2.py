import copy

def parse_iea(file):
    line = file.readline()
    result = []
    while len(line) != 1:
        for letter in line:
            if letter == '.':
                result.append('0')
            elif letter == '#':
                result.append('1')
        line = file.readline()
    return result

def parse_image(file):
    result = []
    for line in file.readlines():
        tab = []
        for letter in line:
            if letter == '.':
                tab.append('0')
            elif letter == '#':
                tab.append('1')
        result.append(tab)
    return result

def enlarge_image(image, enlargement):
    new_size = len(image[0]) + enlargement * 2
    for sub in image:
        for _ in range(enlargement):
            sub.insert(0, '0')
            sub.append('0')
    for _ in range(enlargement):
        image.insert(0, ['0' for _ in range(new_size)])
        image.append(['0' for _ in range(new_size)])
    return image

def get_bin_number(image, i, j):
    height = len(image)
    width = len(image[0])
    bin_num = list('.........')
    letter = image[i][j]
    if i - 1 >= 0 and j - 1 >= 0:
        bin_num[0] = image[i - 1][j - 1]
    if i - 1 >= 0:
        bin_num[1] = image[i - 1][j]
    if i - 1 >= 0 and j + 1 < width:
        bin_num[2] = image[i - 1][j + 1]
    if j - 1 >= 0:
        bin_num[3] = image[i][j - 1]
    bin_num[4] = image[i][j]
    if j + 1 < width:
        bin_num[5] = image[i][j + 1]
    if i + 1 < height and j - 1 >= 0:
        bin_num[6] = image[i + 1][j - 1]
    if i + 1 < height:
        bin_num[7] = image[i + 1][j]
    if i + 1 < height and j + 1 < width:
        bin_num[8] = image[i + 1][j + 1]
    return ''.join(bin_num).replace('.', letter)
    
def enhance(image, iea):
    new_image = copy.deepcopy(image)
    for i, line in enumerate(image):
        for j, _ in enumerate(line):
            bin_num = get_bin_number(image, i, j)
            new_image[i][j] = iea[int(bin_num, 2)]
    return new_image

def print_image(image):
    for line in image:
        for pixel in line:
            if pixel == '0':
                print('.', end='')
            else:
                print('#', end='')
        print()            

def count_pixel(image):
    result = 0
    for line in image:
        for pixel in line:
            result += int(pixel)
    return result

def main():
    with open('data.txt') as file:
        iea = parse_iea(file)
        image = parse_image(file)
        times = 50
        image = enlarge_image(image, times + 1)
        for _ in range(50):
            image = enhance(image, iea)
            print(count_pixel(image))

if __name__ == '__main__':
    main()