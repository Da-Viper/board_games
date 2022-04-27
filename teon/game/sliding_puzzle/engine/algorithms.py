import time
from queue import PriorityQueue
from typing import List, Tuple

from anytree.exporter import DotExporter

from teon.game.sliding_puzzle.engine.pboard import PBoard, Move, Direction
from teon.game.sliding_puzzle.engine.pnode import PNode


def manhattan(start: Tuple[int], goal: Tuple[int], dimen: int) -> int:
    res = 0
    for idx in range(1, len(start)):
        b_row, b_col = divmod(start.index(idx), dimen)
        g_row, g_col = divmod(goal.index(idx), dimen)
        res += abs(b_row - g_row) + abs(b_col - g_col)
    return res


def generate_goal_board(board_dimen: int) -> List[int]:
    size = board_dimen * board_dimen
    goal_board = list(range(1, size))
    goal_board.append(0)

    return goal_board


def ai_play(current_board: PBoard) -> Tuple[Move, Direction]:
    goal_board = generate_goal_board(current_board.size)

    start = time.perf_counter()
    res = _solve(current_board, goal_board, manhattan)
    end = time.perf_counter()

    print(f"total time taken : {end - start}")
    print(f"res: {res}, depth: {res.n_depth}, history:{res.history}")
    draw_node(res)
    return res.history


def draw_node(c_node: PNode):
    p_node = c_node
    while p_node.parent:
        p_node = p_node.parent

    DotExporter(p_node, nodeattrfunc=lambda node: "width=1, height=1, shape=box",
                edgeattrfunc=lambda parent, child: "style=bold").to_picture("udo.svg")


def generate_pnode(node: PNode, play: Tuple[Move, Direction], goal: List, heuristic):
    node_board = node.board()
    new_board = PBoard(node_board.puzzle[:], node_board.size)
    new_node = PNode(new_board, node.n_depth + 1, 0, node.history[:], parent=node)
    move, direction = play
    new_node.play_move(move)
    new_node.history += play,
    new_node.heuristic = heuristic(new_node.puzzle, goal, new_node.size)
    return new_node


def _solve(s_board: PBoard, goal: List[int], heuristic) -> PNode:
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

            if child_node not in visited:
                node_queue.put(child_node)

    return start_node


if __name__ == "__main__":
    s_puzzle = [8, 1, 5, 6, 3, 2, 4, 7, 0]
    # s_puzzle = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1]
    # s_puzzle = [5, 12, 10, 7, 15, 11, 14, 0, 8, 2, 1, 13, 3, 4, 9, 6]
    print(f"start board : {s_puzzle}")
    cboard = PBoard(s_puzzle, 3)

    ai_play(cboard)
