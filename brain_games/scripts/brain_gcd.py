#!/usr/bin/env python3

from brain_games.game_engine import play
from brain_games.games import gcd_logic


def main():
    play(gcd_logic)


if __name__ == '__main__':
    main()
