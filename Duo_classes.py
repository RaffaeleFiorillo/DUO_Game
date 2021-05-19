import Duo_functions as Df


class Player:
    total_points = 0
    turn_points = 0
    launches = 0
    launch = []

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def print_data(self, inside_turn=True):
        if inside_turn:
            print(Df.TURN_LINE)
            print(f"Cube 1 Value: {self.launch[0]} || Cube 2 Value: {self.launch[1]}")
        print(f"Player {self.code}: {self.name}->Total Points: {self.total_points} |"
              f" Turn Points: {self.turn_points} | Moves: {self.launches}")  # prints description player's current data
        if inside_turn:
            print(Df.TURN_LINE)

    def launch_cubes(self):
        self.launches += 1
        # code 1->play again; code 2->[1, x]; code 3->[1, 1]; code 4->pass turn; code 5->win; code 6->max launches
        self.launch = [Df.randint(1, 6) for _ in range(2)]
        self.turn_points += sum(self.launch)
        self.print_data()
        if self.launch == [1, 1]:
            return 3
        elif 1 in self.launch:
            return 2
        elif self.turn_points >= 20:
            return 4
        elif self.total_points >= 50:
            return 5
        elif self.launches == 100:
            return 6
        else:
            return self.pass_or_play()

    def pass_or_play(self):
        pass


class Human_Player(Player):
    def __init__(self, name, code):
        super().__init__(name, code)

    def pass_or_play(self):
        choice = input("Do you wish to pass the turn to the other player? (y/n): ")
        next_player = {1: 2, 2: 1}
        if choice.lower() == "y":
            print(f"# -> TURN PASSED TO PLAYER {next_player[self.code]}")
            return 4
        else:
            return 1


class Computer_Player(Player):
    def __init__(self, name, code):
        super().__init__(name, code)

    def pass_or_play(self):
        Df.wait(2)
        next_player = {1: 2, 2: 1}
        choice = Df.choice([1, 4])
        if choice == 4:
            print(f"# -> TURN PASSED TO PLAYER {next_player[self.code]}")
        return choice


class Mode1:
    turn = 0

    def __init__(self, name1, name2):
        if name1 == "CPU":
            player1 = Computer_Player("CPU", 1)
            player2 = Human_Player(name2, 2)
        else:
            player2 = Computer_Player("CPU", 2)
            player1 = Human_Player(name1, 1)
        self.players = {True: player1, False: player2}
        self.current_player_is_p1 = self.run = True

    def action1(self):
        pass

    def action2(self):
        # pass the points won in current turn to the other player
        self.players[not self.current_player_is_p1].total_points += self.players[self.current_player_is_p1].turn_points
        self.players[self.current_player_is_p1].turn_points = 0  # player loses all points won in this turn
        self.current_player_is_p1 = not self.current_player_is_p1  # pass turn to the other player

    def action3(self):
        # pass all points won by current player to the other player
        self.players[not self.current_player_is_p1].total_points += self.players[self.current_player_is_p1].total_points
        self.players[self.current_player_is_p1].turn_points = 0  # player loses all points won in this turn
        self.players[self.current_player_is_p1].total_points = 0  # player loses all points
        self.current_player_is_p1 = not self.current_player_is_p1  # pass turn to the other player

    def action4(self):
        # points won in this turn are added up to the total amount of points
        self.players[self.current_player_is_p1].total_points += self.players[self.current_player_is_p1].turn_points
        self.players[self.current_player_is_p1].turn_points = 0  # points won in this turn are set to 0
        self.current_player_is_p1 = not self.current_player_is_p1  # pass turn to the other player

    def action5(self):
        self.run = False

    def action6(self):
        self.action4()  # make current player add his turn points to his total amount of points
        # check_for_winner and make it his turn (program assumes that winner is the one who played last)
        if self.players[True] > self.players[False]:
            self.current_player_is_p1 = True
        else:
            self.current_player_is_p1 = False  # if there is a draw, player 2 wins because he is 1 turn behind
        self.run = False

    def take_action(self, code):
        # code 1->play again; code 2->[1, x]; code 3->[1, 1]; code 4->pass turn; code 5->win; code 6->max launches
        actions = {1: self.action1, 2: self.action2, 3: self.action3, 4: self.action4, 5: self.action5, 6: self.action6}
        actions[code]()

    def print_update(self):
        print(Df.TURN_LINE)
        print(f"#################--> UPDATE BLOCK: TURN {self.turn} <--#################\n")
        print("# PLAYING #")
        self.players[self.current_player_is_p1].print_data(False)
        print("# WAITING #")
        self.players[not self.current_player_is_p1].print_data(False)
        print(Df.TURN_LINE)

    def update(self):
        self.turn += 1
        # self.current_player_is_p1 = not self.current_player_is_p1  # passes the turn to the other player
        self.print_update()

    def print_win(self):
        print(Df.BLOCK_LINE)
        print(f"      #####---> Player {self.players[self.current_player_is_p1]} WON!!! <---- #####")
        self.players[self.current_player_is_p1].print_data()
        self.players[not self.current_player_is_p1].print_data()
        print(Df.BLOCK_LINE)

    def play(self):
        self.print_update()
        while self.run:
            action_code = self.players[self.current_player_is_p1].launch_cubes()  # makes current player launch
            self.take_action(action_code)
            self.update()
        self.print_win()


class Mode2:
    def __init__(self, name1, name2):
        player1 = Human_Player(name1)
        player2 = Human_Player(name2)

    def play(self):
        pass
