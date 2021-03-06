from PySide2.QtCore import Slot, Signal, QObject
from PySide2.QtWidgets import QMessageBox

from teon.game.n_queens.engine import algorithm
from teon.game.n_queens.engine.board import NQueen
from teon.game.n_queens.gui.queenscene import NQueenScene
from teon.game.n_queens.gui.tile import Tile


class QueenController(QObject):
    update_gui = Signal(tuple)
    signal_is_solved = Signal()

    def __init__(self, scene: NQueenScene, size: int, parent=None):
        super(QueenController, self).__init__(parent)
        self.scene = scene
        board = self.scene.init_grid(size)

        self.board = NQueen(board, size)

        self.solution_idx = 0
        self.board_solutions = []
        self._init_connection()

    @Slot(Tile)
    def update_cell(self, clicked_tile: Tile):
        """Update board from the value of the clicked tile"""
        pos = clicked_tile.pos
        tile_piece = clicked_tile.p_pos
        game_board = self.board

        if tile_piece.has_queen:
            game_board.remove_queen(pos)
        elif tile_piece.conflicts > 0:
            return
        else:
            game_board.place_queen(pos)
        if game_board.is_solved():
            self.signal_is_solved.emit()

    @Slot(tuple)
    def slot_update_gui(self):
        """Update the scene on the computer"""
        print(f"board {self.board.pos_states}")
        print(f"conflicts {self.board.queens_pos}")
        self.scene.update()

    @Slot()
    def slot_game_over(self):
        """Launch a dialog box if the game is over"""
        print("game is solved ")
        msg_box = QMessageBox(QMessageBox.Information, "Game-over", "You Win")
        msg_box.exec_()
        self.scene.enable_mouse_press = False

    def show_solution(self, next_solution: bool):
        """Gets all the solution for the current state of the board"""
        self.solution_idx += 1 if next_solution else - 1
        no_of_sol = len(self.board_solutions)
        if no_of_sol < 1:
            return
        self.solution_idx = min(self.solution_idx, no_of_sol - 1)
        self.solution_idx = max(self.solution_idx, 0)

        self.scene.draw_board_solution(self.board_solutions[self.solution_idx])

    def generate_solution(self):
        self.scene.enable_mouse_press = False
        self.board.set_default_queens()
        self.board_solutions = algorithm.get_sol(self.board, True)
        self.solution_idx = 0
        print(f"board solution {self.board_solutions}")
        if len(self.board_solutions) < 1:
            return
        self.scene.draw_board_solution(self.board_solutions[self.solution_idx])

    def slot_simulate(self):
        self.scene.enable_mouse_press = False
        print("got to simulate")
        self.board.set_default_queens()
        algorithm.get_sol(self.board, False)

    def reset_game(self):
        self.board_solutions = []
        self.solution_idx = 0
        self.board.reset()
        self.update_gui.emit((0, 0))
        self.scene.enable_mouse_press = True

    def _init_connection(self):
        self.scene.tile_clicked[Tile].connect(self.update_cell)
        self.update_gui.connect(self.slot_update_gui)
        self.signal_is_solved.connect(self.slot_game_over)
