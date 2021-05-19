import Duo_functions as Df
import Duo_classes as Dc
import sys


def main():
    name1, name2, mode = Df.get_input(sys.argv)
    Df.clear_screen()
    Df.print_game_start()
    # print(f"Player1: {name1}\nPlayer2: {name2}\nMode: {mode}")
    modes = {1: Dc.Mode1, 2: Dc.Mode2}
    game = modes[mode](name1, name2)
    game.play()


main()
