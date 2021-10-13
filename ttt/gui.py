#!/usr/bin/env python
import PySimpleGUI as sg

GRAPH_SIZE = 300
BOX_SIZE = GRAPH_SIZE / 3
S_MARGIN = 5
G_MARGIN = 20

class Gui():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    youreFirst = None
    yourTurn = False

    def __init__(self):
        layout = [
            [sg.Button('Go First'), sg.Button('Go Second'), sg.Button('Reset')],
            [sg.Graph(canvas_size=(GRAPH_SIZE, GRAPH_SIZE), graph_bottom_left=(0, GRAPH_SIZE), graph_top_right=(GRAPH_SIZE, 0), key='-GRAPH-',
                change_submits=True, drag_submits=False, background_color='#ffffff')],
        ]
        self.window = sg.Window('Tic Tac Toe', layout, margins=(G_MARGIN, G_MARGIN), finalize=True)
        self.graph = self.window['-GRAPH-']
        self.drawGrid()
        self.startUp()
    
    def startUp(self):
        while True:
            event, values = self.window.read()
            if event == (sg.WIN_CLOSED):
                break
            if event == 'Reset':
                self.window['-GRAPH-'].erase()
                self.drawGrid()
                self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                self.youreFirst = None
                self.yourTurn = None
            if event == 'Go First' and self.youreFirst is None:
                self.youreFirst = True
                self.yourTurn = True
            if event == 'Go Second' and self.youreFirst is None:
                self.youreFirst = False
                self.yourTurn = False
                self.goComputer()
            mouse = values['-GRAPH-']
            if event == '-GRAPH-':
                if mouse == (None, None):
                    continue
                mouse_x = mouse[0]
                mouse_y = mouse[1]
                if self.yourTurn:
                    self.goPlayer(mouse_x, mouse_y)

        self.window.close()

    def drawGrid(self):
        for row in range(3):
            for col in range(3):
                self.graph.DrawRectangle((BOX_SIZE * row, BOX_SIZE * col), (BOX_SIZE * row + BOX_SIZE, BOX_SIZE * col + BOX_SIZE), line_color="black")

    def goPlayer(self, mouse_x, mouse_y):
        self.drawShape(mouse_x, mouse_y, self.youreFirst)
        self.yourTurn = False
        self.goComputer()

    def goComputer(self):
        self.drawShape(200, 100, not self.youreFirst)
        self.yourTurn = True

    def drawShape(self, mouse_x, mouse_y, areYouX):
        index = (int((mouse_y - (mouse_y % BOX_SIZE)) / BOX_SIZE),
                int((mouse_x - (mouse_x % BOX_SIZE)) / BOX_SIZE))
        xPos = index[0] * BOX_SIZE
        yPos = index[1] * BOX_SIZE
        if self.board[index[0]][index[1]] == 1: return
        else: self.board[index[0]][index[1]] = 1

        if areYouX:
            self.graph.DrawLine((yPos + S_MARGIN, xPos + S_MARGIN), (yPos + BOX_SIZE - S_MARGIN,
                        xPos + BOX_SIZE - S_MARGIN), color="#f5594e", width=2)
            self.graph.DrawLine((yPos + BOX_SIZE - 5, xPos + S_MARGIN), (yPos + S_MARGIN,
                        xPos + BOX_SIZE - S_MARGIN), color="#f5594e", width=2)

        else:
            self.graph.DrawCircle((yPos + BOX_SIZE/2, xPos + BOX_SIZE/2), BOX_SIZE / 3, line_width=2, line_color='#5b81cf')

Gui()


