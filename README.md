# pyfont

библиотека для консольных шрифтов

`font.load(path, name)` - загрузить шрифт по пути path с именем name

`font.render(text, name)` - рендер строки текста text шрифтом с именем name

пример использования:
```py
import font

def main():
    font.load("fonts/basic.pyfont", "basic")
    while True:
        answer = input()
        print(font.render(answer, "basic"))

if __name__ == "__main__":
    main()
```
