import json


class Expert:
    def __init__(self, kb_path, dialogue_path):
        self.kb_path = kb_path
        self.dialogue_path = dialogue_path
        with open(self.kb_path) as kb_file:
            self.kb = json.load(kb_file)
        with open(self.dialogue_path) as d_file:
            self.dialogue = json.load(d_file)

    def start(self):
        keep_going = True
        print(self.dialogue["intro"])
        while keep_going:
            print(self.dialogue["q1"])
            fruit_color = input({self.dialogue["q1"]}).lower()
            print(fruit_color)
            fruit_shape = 1 if input({self.dialogue["q2"]}).lower()[0] == "y" else 0
            print(fruit_shape)
            keep_going = input(f'{self.dialogue["repeat"]}\n').lower()[0] == "y"


def main():
    pass


if __name__ == "__main__":
    main()
