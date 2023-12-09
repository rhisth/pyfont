# pyfont

![image](https://github.com/rhisth/pyfont/assets/96009471/5e969539-6fca-46ea-85b3-2c8d73bce6d3)

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
