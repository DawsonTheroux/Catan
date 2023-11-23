class Hex:
    positions = ["nw", "ne", "east", "se", "sw", "west"]
    def __init__(self, neighbours={}, value=-1):
        """ Creates a hex object
            
        n1 through n6 are the hex values starting from NW clockwise to W"""
        self.value = value
        self.neighbours = [None] * 6
        for position, hex_obj in neighbours.items():
            self.set_neighbour(position, hex_obj)

    def set_neighbour(self, position, hex_obj):
        match position:
            case "nw":
                self.neighbours[0] = hex_obj
            case "ne":
                self.neighbours[1] = hex_obj
            case "east":
                self.neighbours[2] = hex_obj
            case "se":
                self.neighbours[3] = hex_obj
            case "sw":
                self.neighbours[4] = hex_obj
            case "west":
                self.neighbours[5] = hex_obj

    def get_neighbour(self, position):
        match position:
            case "nw":
                return self.neighbours[0]
            case "ne":
                return self.neighbours[1]
            case "east":
                return self.neighbours[2]
            case "se":
                return self.neighbours[3]
            case "sw":
                return self.neighbours[4]
            case "west":
                return self.neighbours[5]

