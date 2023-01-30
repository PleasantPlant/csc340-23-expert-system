from expert import Expert


def main():
    print("Testing, I'm in main.")
    e1 = Expert(
        "csc340-23-expert-system/data/kb_fruit.json",
        "csc340-23-expert-system/data/dialogue_fruit.json",
    )
    e1.start()


if __name__ == "__main__":
    main()
