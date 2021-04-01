from copy import deepcopy
from collections import deque
import sys
import time


class State(object):
    def __init__(self, missionaries, cannibals, boats):
        self.missionaries = missionaries or 0
        self.cannibals = cannibals or 0
        self.boats = boats or 0

    def successors(self):
        if self.boats is 1:
            sign = -1
            direction = "Original shore to the new shore"
        else:
            sign = 1
            direction = "New shore to the original shore"

        for m in range(3):
            for c in range(3):
                new_state = State(self.missionaries + sign * m, self.cannibals + sign * c, self.boats + sign * 1)

                if m + c >= 1 and m + c <= 2 and new_state.is_valid():
                    action = "Take %d missionaries and %d cannibals %s. %r" % (m, c, direction, new_state)
                    yield action, new_state

    def is_valid(self):
        if (self.missionaries < 0 or self.cannibals < 0 or
            self.missionaries > 3 or self.cannibals > 3 or 
            not self.boats and self.boats != 0):
            return False

        if self.cannibals > self.missionaries and self.missionaries > 0: return False
        if self.cannibals < self.missionaries and self.missionaries < 3: return False

        return True

    def is_goal_state(self):
        return self.cannibals == 0 and self.missionaries == 0 and self.boats == 0

    def __str__(self):
        return "State(missionaries=%d, cannibals=%d, boats=%d)" % (self.missionaries, self.cannibals, self.boats)

    def __repr__(self):
        return "State(missionaries=%d, cannibals=%d, boats=%d)" % (self.missionaries, self.cannibals, self.boats)


class Node(object):
    def __init__(self, parent_node, state, action, depth):
        self.parent_node = parent_node
        self.state = state
        self.action = action
        self.depth = depth

    def expand(self):
        for (action, next_state) in self.state.successors():
            next_node = Node(
                parent_node=self,
                state=next_state,
                action=action,
                depth=self.depth + 1)

            yield next_node

    def extract_solution(self):
        solution = []
        node = self

        while node.parent_node is not None:
            solution.append(node.action)
            node = node.parent_node

        solution.reverse()

        return solution


def bfs(start_state):
    initial_node = Node(parent_node=None, state=start_state, action=None, depth=0)

    fifo = deque([initial_node])
    num_expansions = 0
    max_depth = -1

    while True:
        if not fifo:
            print("%d expansions" % num_expansions)

            return None

        node = fifo.popleft()

        if node.depth > max_depth:
            max_depth = node.depth

        if node.state.is_goal_state():
            solution = node.extract_solution()

            return solution

        num_expansions += 1

        fifo.extend(node.expand())


if __name__ == "__main__":
    start_state = State(3, 3, 1)
    solution = bfs(start_state)

    if solution is None:
        print("no solution")
    else:
        print("solution (%d steps):" % len(solution))
        for step in solution:
            print("%s" % step)
