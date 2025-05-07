from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
import random

class RPSGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 20
        self.padding = 30
        
        #background
        Window.clearcolor = (0.1, 0.1, 0.2, 1)
        
        #Title
        self.title_label = Label(
            text='Rock Paper Scissors',
            font_size=40,
            bold=True,
            color=(1, 1, 1, 1))
        self.add_widget(self.title_label)
        
        #Score display
        self.score_label = Label(
            text='You: 0  |  Computer: 0',
            font_size=24,
            color=(0.8, 0.8, 1, 1))
        self.add_widget(self.score_label)
        
        #Choices display
        self.choices_label = Label(
            text='Make your choice!',
            font_size=26,
            color=(1, 1, 1, 1),
            markup=True)
        self.add_widget(self.choices_label)
        
        #Result display
        self.result_label = Label(
            text='',
            font_size=32,
            bold=True)
        self.add_widget(self.result_label)
        
        #Buttons
        self.button_layout = BoxLayout(spacing=10)
        for choice in ['Rock', 'Paper', 'Scissors']:
            btn = Button(
                text=choice,
                font_size=24,
                background_normal='',
                background_color=self.get_button_color(choice))
            btn.bind(on_press=self.play_round)
            self.button_layout.add_widget(btn)
        self.add_widget(self.button_layout)
        
        #Initialize scores
        self.player_score = 0
        self.computer_score = 0

    def get_button_color(self, choice):
        colors = {
            'Rock': (0.8, 0.3, 0.3, 1),
            'Paper': (0.3, 0.8, 0.3, 1),
            'Scissors': (0.3, 0.3, 0.8, 1)
        }
        return colors[choice]

    def play_round(self, instance):
        player_choice = instance.text
        computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
        
        #Display Text 
        self.choices_label.text = (
            f"Your choice: [color=00ff00]{player_choice}[/color]\n"
            f"Computer's choice: [color=ff0000]{computer_choice}[/color]")
        
        #Determine winner
        if player_choice == computer_choice:
            result = "TIE!"
            result_color = (1, 1, 0, 1)  # Yellow
        elif ((player_choice == 'Rock' and computer_choice == 'Scissors') or
              (player_choice == 'Paper' and computer_choice == 'Rock') or
              (player_choice == 'Scissors' and computer_choice == 'Paper')):
            result = "YOU WIN!"
            result_color = (0, 1, 0, 1)  # Green
            self.player_score += 1
        else:
            result = "COMPUTER WINS!"
            result_color = (1, 0, 0, 1)  # Red
            self.computer_score += 1
        
        #UI
        self.result_label.text = result
        self.result_label.color = result_color
        self.score_label.text = f'You: {self.player_score}  |  Computer: {self.computer_score}'

class RPSApp(App):
    def build(self):
        return RPSGame()

if __name__ == '__main__':
    RPSApp().run()