import copy
from queue import PriorityQueue
from typing import List, Tuple

from game.sliding_puzzle.engine.pboard import PBoard, Move, Direction
from game.sliding_puzzle.engine.pnode import PNode


def manhattan(start: List, goal: List, dimen: int) -> int:
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
    res = _solve(current_board, goal_board, manhattan)
    print(f"res: {res}, depth: {res.depth}, history:{res.history}")
    return res.history


def generate_pnode(node: PNode, play: Tuple[Move, Direction], goal: List, heuristic):
    new_node = copy.deepcopy(node)
    move, direction = play
    new_node.play_move(move)
    new_node.heuristic = heuristic(new_node.puzzle, goal, new_node.size)
    new_node.depth += 1
    new_node.history += play,
    return new_node


def _solve(s_board: PBoard, goal: List[int], heuristic):
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

        max_search_depth = max(curr_node.depth, max_search_depth)

        if curr_node in visited:
            continue
        visited.add(curr_node)

        if curr_node.is_goal(goal):
            return curr_node

        nodes_expanded += 1
        for play in curr_node.generate_moves():
            child_node = generate_pnode(curr_node, play, goal, heuristic)

            if child_node not in visited:
                node_queue.put(child_node)

    return start_node


if __name__ == "__main__":
    cboard = PBoard([1, 0, 3, 4, 2, 5, 7, 8, 6], 3)

    ai_play(cboard)
