from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class TicTacToeGame(BoxLayout):
    def __init__(self, **kwargs):
        super(TicTacToeGame, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.player_scores = {'X': 0, 'O': 0}

        # Buttons layout
        buttons_layout = BoxLayout(orientation='vertical')
        for row in range(3):
            button_row = BoxLayout(orientation='horizontal')
            for col in range(3):
                button = Button(font_size = 50)
                button.bind(on_press=self.on_button_press)
                self.buttons[row][col] = button
                button_row.add_widget(button)
            buttons_layout.add_widget(button_row)
        self.add_widget(buttons_layout)

        # Labels layout
        turn_labels_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=44)
        labels_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=44)
        self.score_label_x = Label(text='Player X: 0')
        self.score_label_o = Label(text='Player O: 0')
        self.turn_label = Label(text=f"{self.current_player}'s turn")
        labels_layout.add_widget(self.score_label_x)
        labels_layout.add_widget(self.score_label_o)
        turn_labels_layout.add_widget(self.turn_label)
        self.add_widget(labels_layout)
        self.add_widget(turn_labels_layout)

    def on_button_press(self, instance):
        self.update_turn_label()
        row, col = self.get_button_position(instance)
        if self.buttons[row][col].text == '':
            self.buttons[row][col].text = self.current_player
            if self.check_winner(row, col):
                print(f'Player {self.current_player} wins!')
                self.update_scores()
                self.reset_board()
            elif self.is_board_full():
                print('It\'s a draw!')
                self.reset_board()
            else:
                self.switch_player()

    def update_turn_label(self):
        if self.current_player == 'X':
            self.turn_label.text = "O's turn"
        else:
            self.turn_label.text = "X's turn"

    def get_button_position(self, button):
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col] == button:
                    return row, col

    def check_winner(self, row, col):
        # Check row
        if all(self.buttons[row][i].text == self.current_player for i in range(3)):
            return True
        # Check column
        if all(self.buttons[i][col].text == self.current_player for i in range(3)):
            return True
        # Check diagonals
        if all(self.buttons[i][i].text == self.current_player for i in range(3)) or \
                all(self.buttons[i][2 - i].text == self.current_player for i in range(3)):
            return True
        return False

    def is_board_full(self):
        return all(self.buttons[row][col].text != '' for row in range(3) for col in range(3))

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].text = ''
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def update_scores(self):
        self.player_scores[self.current_player] += 1
        self.score_label_x.text = f'Player X: {self.player_scores["X"]}'
        self.score_label_o.text = f'Player O: {self.player_scores["O"]}'