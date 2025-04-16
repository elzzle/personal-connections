puzzle = {
    "yellow": ["Yellow One", "Yellow Two", "Yellow Three", "Yellow Four"],
    "green": ["Green One", "Green Two", "Green Three", "Green Four"],
    "blue": ["Blue One", "Blue Two", "Blue Three", "Blue Four"],
    "purple": ["Purple One", "Purple Two", "Purple Three", "Purple Four"]
}

source_arr = puzzle["yellow"] + puzzle["green"] + puzzle["blue"] + puzzle["purple"]
word_containers = []

word_map = {}
word_map_calculated = False

def get_word_map():
    if word_map_calculated:
        return word_map

    for i in range(len(4)):
        yellow_word = puzzle["yellow"][i]
        green_word = puzzle["green"][i]
        blue_word = puzzle["blue"][i]
        purple_word = puzzle["purple"][i]

        word_map[yellow_word] = "yellow"
        word_map[green_word] = "green"
        word_map[blue_word] = "blue"
        word_map[purple_word] = "purple"
    word_map_calculated = True
    return word_map