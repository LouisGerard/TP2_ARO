class Object:
    def __init__(self, weight, value) -> None:
        super().__init__()
        self.weight = weight
        self.value = value
        self.ratio = value / weight

    def __lt__(self, other):
        return self.ratio < other.ratio

    def __eq__(self, other):
        return self.ratio == other.ratio

    def __repr__(self):
        return "(" + str(self.weight) + ", " + str(self.value) + ") : " + "{0:.2f}".format(self.ratio)


def read_file(path):
    objects = []
    with open(path, 'r') as file:
        capacity = int(file.readline())
        for line in file:
            exploded = line.split(' ')
            weight = int(exploded[0])
            value = int(exploded[1])
            objects.append(Object(weight, value))
    return capacity, objects


if __name__ == '__main__':
    capacity, objects = read_file('data/sac0.txt')
    objects = sorted(objects, reverse=True)


