from board_components.board_edge import BoardEdge
from board_components.board_node import BoardNode
from board_components.hex import Hex
from board_components.road import Road
from board_components.robber import Robber
from board_components.settlement import Settlement

class CatanBoard:
    def __init__(self):
        print("Created Catan Board")
        self.initialize_board()

    def generate_hexes(self): 
        hex_list = []
        center_hex = Hex(value=0)
        hex_list.append(center_hex)

        # Iterate through all the positions around the center position
        last_hex = None
        for i, position in enumerate(Hex.positions):
            print(f"--Generating hex: {i+1}--")
            # The center position is represented by the oposite side
            # of the hex being created.
            center_position = Hex.positions[(i + 3) % 6]
            print(f"Setting center hex as '{center_position}' of the new hex")
            new_hex = Hex({center_position: center_hex}, i + 1)
            hex_list.append(new_hex)
            print(f"Setting the new hex as '{position}' of the center hex")
            center_hex.set_neighbour(position, new_hex)
            
            # If there was a previous hex (i.e current hex is not the first)
            # Link the previous hex that was created to the current one.
            if last_hex is not None:
                print(f"Setting the previous hex as the '{Hex.positions[(i-2)%6]}' of the new hex")
                new_hex.set_neighbour(Hex.positions[(i - 2) % 6], last_hex)
                print(f"Setting the new hex as the '{Hex.positions[(i+1)%6]}' of the previous hex")
                last_hex.set_neighbour(Hex.positions[(i + 1) % 6], new_hex)

            # If this is the last hex, also set the first one that was created.
            if i == 5:
                print(f"Setting the first hex as 'ne' of the new hex")
                first_hex = center_hex.get_neighbour("nw")
                new_hex.set_neighbour("ne", first_hex)
                print(f"Setting the new hex as 'sw' of the first hex")
                first_hex.set_neighbour("sw", new_hex)
                  
            last_hex = new_hex

        breakpoint()
        return hex_list

    def initialize_board(self):
        self.center_hex = self.generate_hexes()
        self.graph = self.generate_graph()

