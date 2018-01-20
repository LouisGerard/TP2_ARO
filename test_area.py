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
    return capacity, sorted(objects, reverse=True)


def bound(objects, capacity_left, start):
    total_weight = 0
    total_value = 0
    for i in range(start, len(objects)):
        o = objects[i]
        if total_weight + o.weight >= capacity_left:
            place_left = capacity_left - total_weight
            ratio = place_left / o.weight
            total_value += o.value * ratio
            break
        total_value += o.value
        total_weight += o.weight
    return total_value


def branch(objects, max_value=0, deepness=0, weight=0, value=0):
    if deepness == len(objects):
        return value

    o = objects[deepness]

    b1 = value + bound(objects, capacity-weight, deepness)
    if b1 > max_value and weight+o.weight <= capacity:
        v1 = branch(objects, max_value, deepness+1, weight+o.weight, value+o.value)
        if v1 > max_value:
            max_value = v1

    b0 = value + bound(objects, capacity-weight, deepness+1)
    if b0 > max_value:
        v0 = branch(objects, max_value, deepness+1, weight, value)
        if v0 > max_value:
            max_value = v0

    return max_value


if __name__ == '__main__':
    capacity, objects = read_file('data/sac0.txt')
    print(branch(objects))


