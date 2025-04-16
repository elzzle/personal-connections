import random
from game.puzzle_data import source_arr, word_containers
from utils.container_utils import build_text, TEXT_COLOR_NORMAL

def shuffle(e):
    random.shuffle(source_arr)
    for i in range(16):
        word_containers[i][0].content = build_text(source_arr[i], TEXT_COLOR_NORMAL)
        word_containers[i][0].update()

