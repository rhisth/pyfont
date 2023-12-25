fonts = {}
indexes = {'': 0, ' ': 1, '!': 2, '"': 3, '#': 4, '$': 5, '%': 6, '&': 7, "'": 8, '(': 9, ')': 10, '*': 11, '+': 12, ',': 13, '-': 14, '.': 15, '/': 16, '0': 17, '1': 18, '2': 19, '3': 20, '4': 21, '5': 22, '6': 23, '7': 24, '8': 25, '9': 26, ':': 27, ';': 28, '<': 29, '=': 30, '>': 31, '?': 32, '@': 33, 'A': 34, 'B': 35, 'C': 36, 'D': 37, 'E': 38, 'F': 39, 'G': 40, 'H': 41, 'I': 42, 'J': 43, 'K': 44, 'L': 45, 'M': 46, 'N': 47, 'O': 48, 'P': 49, 'Q': 50, 'R': 51, 'S': 52, 'T': 53, 'U': 54, 'V': 55, 'W': 56, 'X': 57, 'Y': 58, 'Z': 59, '[': 60, '\\': 61, ']': 62, '^': 63, '_': 64, '`': 65, 'a': 66, 'b': 67, 'c': 68, 'd': 69, 'e': 70, 'f': 71, 'g': 72, 'h': 73, 'i': 74, 'j': 75, 'k': 76, 'l': 77, 'm': 78, 'n': 79, 'o': 80, 'p': 81, 'q': 82, 'r': 83, 's': 84, 't': 85, 'u': 86, 'v': 87, 'w': 88, 'x': 89, 'y': 90, 'z': 91, '{': 92, '|': 93, '}': 94, '~': 95, 'А': 96, 'Б': 97, 'В': 98, 'Г': 99, 'Д': 100, 'Е': 101, 'Ё': 102, 'Ж': 103, 'З': 104, 'И': 105, 'Й': 106, 'К': 107, 'Л': 108, 'М': 109, 'Н': 110, 'О': 111, 'П': 112, 'Р': 113, 'С': 114, 'Т': 115, 'У': 116, 'Ф': 117, 'Х': 118, 'Ц': 119, 'Ч': 120, 'Ш': 121, 'Щ': 122, 'Ъ': 123, 'Ы': 124, 'Ь': 125, 'Э': 126, 'Ю': 127, 'Я': 128, 'а': 129, 'б': 130, 'в': 131, 'г': 132, 'д': 133, 'е': 134, 'ё': 135, 'ж': 136, 'з': 137, 'и': 138, 'й': 139, 'к': 140, 'л': 141, 'м': 142, 'н': 143, 'о': 144, 'п': 145, 'р': 146, 'с': 147, 'т': 148, 'у': 149, 'ф': 150, 'х': 151, 'ц': 152, 'ч': 153, 'ш': 154, 'щ': 155, 'ъ': 156, 'ы': 157, 'ь': 158, 'э': 159, 'ю': 160, 'я': 161}

class FontNotFoundError(Exception):
    pass

class FontFormatError(Exception):
    pass

class NoFontDataError(Exception):
    pass

class NoFontError(Exception):
    pass

def load(path, name):
    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read().splitlines()
        text = content[0].split()
        height = int(text[0])
        cyrillic = int(text[1])
    except FileNotFoundError:
        raise FontNotFoundError(f'The font file by the path "{path}" was not found') from None
    except ValueError:
        raise FontFormatError(f'The font file by the path "{path}" has incorrect format') from None
    except IndexError:
        raise FontFormatError(f'The font file by the path "{path}" has not enough format data') from None
    flist = []
    element = ""
    i = 0
    for line in content[1:]:
        i += 1
        element += line + "\n"
        if i == height:
            flist.append(f"{element}")
            i = 0
            element = ""
    if not cyrillic and not len(flist) > 161:
        symbol = "\n" * height
        flist += [symbol] * 66
    if len(flist) < 162:
        raise NoFontDataError(f'The font file by the path "{path}" has not enough data')
    fonts[name] = flist

def render(text, name):
    if not text:
        return
    try:
        font = fonts[name]
    except KeyError:
        raise NoFontError(f'The font "{name}" was not loaded') from None
    split = font[indexes[""]]
    result = split
    split = split.splitlines()
    for symbol in text:
        result = result.splitlines()
        add = font[indexes[symbol]].splitlines()
        for i, val in enumerate(add):
            result[i] += add[i] + split[i]
        result = "\n".join(result) + "\n"
    return result[:-1]
