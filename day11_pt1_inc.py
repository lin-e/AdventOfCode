# floors start at 0
# let each component be represented as [x, y], where x is the element (first 2 chars) and y is chip (m) or gen (g)
# my answer for p1 is 31, my answer for p2 is 55 (p_tseng)
# THIS IS UNSTABLE. THE CODE RUNS OVER HOURS DUE TO INEFFICIENT PRUNING.
class game_state:
    def __init__(self):
        self.floors = list()
        for i in range(0, 4):
            self.floors.append(list())
        self.elevator = 0
    def same(self, compare):
        if self.elevator == compare.elevator:
            for floor in range(0, 4):
                if not sorted(self.floors[floor]) == sorted(compare.floors[floor]):
                    return False
            return True
        return False
    def copy(self, contents, elevation_change):
        new = game_state()
        new.elevator  = self.elevator + elevation_change
        for i in range(0, 4):
            for item in self.floors[i]:
                new.floors[i].append(item)
        for i in contents:
            new.floors[self.elevator].remove(i)
            new.floors[new.elevator].append(i)
        return new
    def complete(self):
        for i in range(0, 3):
            if not len(self.floors[i]) == 0:
                return False
        return True
class manager:
    def __init__(self):
        #contents = [[["hy", "m"], ["li", "m"]], [["hy", "g"]], [["li", "g"]], []]
        #contents = [[["hy", "g"], ["po", "g"]], [["hy", "m"], ["po", "m"]], [], []]
        contents = [[["th", "g"], ["th", "m"], ["pl", "g"], ["st", "g"]], [["pl", "m"], ["st", "m"]], [["pr", "g"], ["pr", "m"], ["ru", "g"], ["ru", "m"]], []]
        #contents = [[["st", "g"], ["st", "m"], ["pl", "g"], ["pl", "m"]], [["th", "g"], ["ru", "g"], ["ru", "m"], ["cu", "g"], ["cu", "m"]], [["th", "m"]], []]
        self.active = list()
        self.past_states = list()
        self.moves = 0
        self.solved = False
        current_state = game_state()
        for i in range(0, 4):
            for component in contents[i]:
                current_state.floors[i].append(component)
        self.active.append(current_state)
        self.past_states.append(current_state)
    def visited(self, new_state):
        for i in self.past_states:
            if i.same(new_state):
                return True
        return False
    def solve(self):
        while not self.solved:
            new_states = list()
            for state in self.active:
                if state.complete():
                    return self.moves
                elevator_moves = [-1, 1]
                skip_down = True
                for i in range(0, state.elevator):
                    if not len(state.floors[i]) == 0:
                        skip_down = False
                if skip_down or state.elevator == 0:
                    elevator_moves.remove(-1)
                if state.elevator == 3:
                    elevator_moves.remove(1)
                if not len(state.floors[state.elevator]) == 0:
                    floor_contents = state.floors[state.elevator]
                    for move in elevator_moves:
                        for a in floor_contents:
                            for b in floor_contents:
                                if a[1] == b[1] or a[0] == b[0]:
                                        new_states.append(state.copy(([a, b] if not a == b else [a]), move))
            del self.active[:]
            for state in new_states:
                if not self.legal(state):
                    continue
                if self.visited(state):
                    continue
                self.active.append(state)
                self.past_states.append(state)
            self.moves += 1
            print(self.moves, len(self.active))
        return self.moves
    def legal(self, state):
        # what do we know?
        # gens can be anywhere
        # gens paired with chip still damages other non-paired chips
        # gens paired with chip moves together
        for floor in state.floors:
            if len(floor) == 0:
                continue
            chips = list()
            gens = list()
            unpaired_chips = 0
            for i in floor:
                if i[1] == "m":
                    chips.append(i[0])
                else:
                    gens.append(i[0])
            for chip in chips:
                if not chip in gens:
                    unpaired_chips += 1
            if not (unpaired_chips == 0 or len(gens) == 0):
                return False
        return True
game = manager()
print("Solved in", game.solve(), "moves")
