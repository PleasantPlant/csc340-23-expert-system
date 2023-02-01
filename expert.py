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
        contribution = False
        keep_going = True
        print(f'{self.dialogue["intro"]}\n')
        while keep_going:
            fruit_color = input(f'{self.dialogue["q1"]}\n').lower()
            fruit_shape = (
                1 if input(f'{self.dialogue["q2"]}\n').lower()[0] == "y" else 0
            )
            fruit_sweet = (
                1 if input(f'{self.dialogue["q3"]}\n').lower()[0] == "y" else 0
            )

            fruit_key = f"{fruit_color}-{fruit_shape}-{fruit_sweet}"

            fruit_value = self.kb.get(fruit_key)

            if fruit_value:
                print(f'\n{self.dialogue["conclusion"]} {fruit_value.get("name")}.\n')

            else:
                new_fruit = input(f'\n{self.dialogue["not_found"]}\n').lower()
                self.kb[fruit_key] = {"name": new_fruit}
                with open(self.kb_path, "w") as kb_file:
                    json.dump(self.kb, kb_file)
                contribution = True

            keep_going = input(f'{self.dialogue["repeat"]}\n').lower()[0] == "y"

        if contribution:
            print(self.dialogue["contribution"])
            print(self.dialogue["farewell"])
        else:
            print(self.dialogue["farewell"])


def main():
    pass


if __name__ == "__main__":
    main()
