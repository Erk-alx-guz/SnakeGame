import snakeEnv
from snakeEnv import snake

def main():
    while True:
        snakePlayer = snake()

        snakePlayer.render()

if __name__ == '__main__':
    main()