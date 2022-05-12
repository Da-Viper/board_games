import sys
import time
from enum import Enum, unique
from math import inf
from queue import PriorityQueue
from typing import List, Tuple

from anytree.exporter import DotExporter

from teon.game.sliding_puzzle.engine.pboard import PBoard, Move, Direction
from teon.game.sliding_puzzle.engine.pnode import PNode

sys.setrecursionlimit(100000)


@unique
class Heuristic(Enum):
    MANHATTAN = 0
    MISPLACED = 1


@unique
class Search(Enum):
    DFS = 0
    ASTAR = 1
    IDASTAR = 2


def manhattan(start: List[int], goal: List[int], dimen: int) -> int:
    res = 0
    for idx in range(1, len(start)):
        b_row, b_col = divmod(start.index(idx), dimen)
        g_row, g_col = divmod(goal.index(idx), dimen)
        res += abs(b_row - g_row) + abs(b_col - g_col)
    return res


def misplaced(start: List[int], goal: List[int], dimen: int = 3) -> int:
    return sum(b != g for b, g in zip(start, goal))


def generate_goal_board(board_dimen: int) -> List[int]:
    size = board_dimen * board_dimen
    goal_board = list(range(1, size))
    goal_board.append(0)

    return goal_board


def ai_play(current_board: PBoard, search_type: Search, h_type: Heuristic = Heuristic.MANHATTAN) -> \
        Tuple[Move, Direction]:
    goal_board = generate_goal_board(current_board.size)

    start = time.perf_counter()
    heur = manhattan if h_type is Heuristic.MANHATTAN else misplaced
    if search_type is Search.ASTAR:
        res = _solve_astar(current_board, goal_board, heur)
        # res = _solve_ida_star2(current_board, goal_board, heur)
    elif search_type is Search.IDASTAR:
        res = _solve_ida_star(current_board, goal_board, heur)
    else:
        res = _solve_dfs(current_board, goal_board, heur)
    end = time.perf_counter()

    print(f"total time taken : {end - start}")
    print(f"res: {res}, depth: {res.n_depth}, history:{res.history}")
    draw_node(res, search_type.name)
    return res.history


def draw_node(c_node: PNode, search_name: str):
    p_node = c_node
    p_node.color = "green"
    print(f"the childrens {p_node.children}")
    while p_node.parent:
        p_node.parent.color = "lightgreen"
        p_node = p_node.parent

    def set_colour(node: PNode):
        attrs = ["style=filled"]
        if not node.children:
            attrs += [f"fillcolor=lightblue2"]
        if hasattr(node, "color"):
            attrs += [f"fillcolor={node.color}"]
        if node.parent is None:
            attrs += [f"fillcolor=yellow"]
        return ", ".join(attrs)

    DotExporter(p_node, options=["label=Search_Tree", "labelloc=t", "fontsize=60"], nodeattrfunc=set_colour,
                edgeattrfunc=lambda parent, child: "style=bold").to_picture(f"{search_name}.svg")


def generate_pnode(node: PNode, play: Tuple[Move, Direction], goal: List, heuristic):
    node_board = node.board()
    new_board = PBoard(node_board.puzzle[:], node_board.size)
    new_node = PNode(new_board, node.n_depth + 1, 0, node.history[:])
    move, direction = play
    new_node.play_move(move)
    new_node.history += play,
    new_node.heuristic = heuristic(new_node.puzzle, goal, new_node.size)

    return new_node


def _solve_dfs(s_board: PBoard, goal: List[int], heuristic, depth_limit=30):
    start_node = PNode(s_board, 0)

    stack = [start_node]
    visited = set()
    visited.add(start_node)
    stack.append(start_node)
    current_depth = start_node.n_depth

    while len(stack):
        node = stack.pop()

        if current_depth != node.n_depth:
            current_depth = node.n_depth

        if node.is_goal(goal):
            return node
        print(f"the depth {node.n_depth}")

        for play in node.generate_moves():
            child_node = generate_pnode(node, play, goal, heuristic)
            if child_node.n_depth <= depth_limit and child_node.__hash__() not in visited:
                visited.add(child_node)
                stack.append(child_node)

    return start_node


def _solve_astar(s_board: PBoard, goal: List[int], heuristic) -> PNode:
    start_depth = 0
    dimension = s_board.size
    f_val = heuristic(s_board.puzzle, goal, dimension)

    start_node = PNode(s_board, start_depth, heuristic=f_val)
    node_queue = PriorityQueue()
    node_queue.put(start_node)
    visited = set()
    nodes_expanded = 0
    max_search_depth = 0

    while len(node_queue.queue):
        curr_node: PNode = node_queue.get()

        max_search_depth = max(curr_node.n_depth, max_search_depth)

        c_node_hash = curr_node.__hash__()
        if c_node_hash in visited:
            continue
        visited.add(c_node_hash)

        if curr_node.is_goal(goal):
            return curr_node

        nodes_expanded += 1
        for play in curr_node.generate_moves():
            child_node = generate_pnode(curr_node, play, goal, heuristic)

            if child_node.__hash__() not in visited:
                child_node.parent = curr_node
                node_queue.put(child_node)

    return start_node


def _solve_ida_star(s_board: PBoard, goal: List[int], heuristic):
    dimension = s_board.size
    s_bound = heuristic(s_board.puzzle, goal, dimension)
    # start_
    root = PNode(s_board, 0, s_bound)
    s_path = [root]
    visited = set()
    visited.add(root.__hash__())

    def _search(path: List[PNode], g: int, bound: int):
        node = path[-1]
        f = heuristic(node.puzzle, goal, dimension) + g

        # global node_explored

        # print(node_explored)
        # if node_explored % 100000 == 0:
        #     print(f"node explored {node_explored}")
        if f > bound:
            return f

        if node.is_goal(goal):
            return True

        b_min = inf
        for play in node.generate_moves():
            child_node: PNode = generate_pnode(node, play, goal, heuristic)
            child_node_hash = child_node.__hash__()

            if child_node_hash not in visited:
                child_node.parent = node
                path.append(child_node)
                visited.add(child_node_hash)

                t = _search(path, g + 1, bound)

                if t == True:
                    return t
                if t < b_min:
                    b_min = t

                path.pop()
                visited.remove(child_node_hash)

        return b_min

    while True:
        t = _search(s_path, 0, s_bound)
        if t == True:
            return s_path[-1]
        if t == inf:
            return False
        s_bound = t


# def _solve_ida_star2(s_board: PBoard, goal: List[int], heuristic) -> PNode:
#     node_explored = 0
#     dimension = s_board.size
#     cutoff = heuristic(s_board.puzzle, goal, dimension)
#     start_node = PNode(s_board, 0, cutoff)
#
#     while True:
#         node_queue = PriorityQueue()
#         node_queue.put(start_node)
#
#         visited = set()
#         min_above = inf
#         snode_hash = start_node.__hash__()
#         visited.add(snode_hash)
#
#         while len(node_queue.queue):
#             current_node: PNode = node_queue.get()
#             node_explored += 1
#
#             if node_explored % 100000 == 0:
#                 print(f"node explored :{node_explored}")
#
#             if current_node.is_goal(goal):
#                 return current_node
#
#             for play in current_node.generate_moves():
#                 child_node = generate_pnode(current_node, play, goal, heuristic)
#
#                 child_node_hash = child_node.__hash__()
#                 if child_node_hash in visited:
#                     continue
#                 child_node.parent = current_node
#                 c_node_fval = child_node.f_value
#                 if cutoff < c_node_fval:
#                     if c_node_fval < min_above:
#                         min_above = c_node_fval
#                     continue
#
#                 node_queue.put(child_node)
#                 visited.add(child_node_hash)
#         cutoff = min_above
#

if __name__ == "__main__":
    # s_puzzle = [8, 1, 5, 6, 3, 2, 4, 7, 0]
    s_puzzle = [1, 2, 3, 4, 0, 5, 7, 8, 6]
    # s_puzzle = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1]
    # s_puzzle = [5, 12, 10, 7, 15, 11, 14, 0, 8, 2, 1, 13, 3, 4, 9, 6]
    # s_puzzle = [14, 13, 15, 7, 11, 12, 9, 5, 6, 0, 2, 1, 4, 8, 10, 3]
    # s_puzzle = [1, 2, 3, 4, 0, 5, 7, 8, 6]
    # print(f"start board : {s_puzzle}")
    # cboard = PBoard(s_puzzle, 4)
    cboard = PBoard(s_puzzle, 3)
    # sys.exit(app.exec_())

    # result = ai_play(cboard, True)
    # print(f"\n Ida search ")
    start = time.perf_counter_ns()
    result = ai_play(cboard, Search.ASTAR, Heuristic.MANHATTAN)
    # result = ai_play(cboard, Search.ASTAR, Heuristic.MANHATTAN)
    end = time.perf_counter_ns()
    print(f"total time taken {end - start}")
    print(f"length:{len(result)}")
    # for _, direction in result:
    #     print(direction)
