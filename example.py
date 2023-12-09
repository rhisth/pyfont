import font

def main():
    font.load("fonts/basic.pyfont", "basic")
    while True:
        answer = input()
        print(font.render(answer, "basic"))

if __name__ == "__main__":
    main()
