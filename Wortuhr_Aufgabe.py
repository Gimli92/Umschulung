import tkinter as tk
import time

letters = [
    ['E', 'S', 'K', 'I', 'S', 'T', 'A', 'F', 'Ü', 'N', 'F'],
    ['Z', 'E', 'H', 'N', 'Z', 'W', 'A', 'N', 'Z', 'I', 'G'],
    ['D', 'R', 'E', 'I', 'V', 'I', 'E', 'R', 'T', 'E', 'L'],
    ['V', 'O', 'R', 'F', 'U', 'N', 'K', 'N', 'A', 'C', 'H'],
    ['H', 'A', 'L', 'B', 'A', 'E', 'L', 'F', 'Ü', 'N', 'F'],
    ['E', 'I', 'N', 'S', 'X', 'A', 'M', 'Z', 'W', 'E', 'I'],
    ['D', 'R', 'E', 'I', 'P', 'M', 'J', 'V', 'I', 'E', 'R'],
    ['S', 'E', 'C', 'H', 'S', 'N', 'L', 'A', 'C', 'H', 'T'],
    ['S', 'I', 'E', 'B', 'E', 'N', 'Z', 'W', 'Ö', 'L', 'F'],
    ['Z', 'E', 'H', 'N', 'E', 'U', 'N', 'K', 'U', 'H', 'R']
]
words = ["ES", "IST", "VOR", "HALB", "NACH", "VIERTEL", "DREIVIERTEL",
         "EINS", "ZWEI", "DREI", "VIER", "FÜNF", "SECHS", "SIEBEN",
         "ACHT", "NEUN", "ZEHN", "ELF", "ZWÖLF", "ZWANZIG", "UHR"]


# Methode: Wörter finden
def find_words(grid, words):
    results = {}

    for word in words:
        results[word] = []
        for r, row in enumerate(grid):
            row_string = "".join(row)
            start = 0

            while True:
                start = row_string.find(word, start)
                if start == -1:
                    break

                positions = []
                for i in range(len(word)):
                    positions.append((r, start + i))

                results[word].append(positions)
                start += 1

    return results


# Methoden: Farben ändern
def set_color(positions, color):
    for r, c in positions:
        label_grid[r][c].config(fg=color)


def reset_color_bg():

    for lbl2 in label_grid_min:
        lbl2.config(fg="black")


def set_color_bg(positions, color):
    for r, c in positions:
        label_grid_min[r][c].config(fg=color)


def reset_color():
    for row in label_grid:
        for lbl in row:
            lbl.config(fg="white")


# Methode: Uhrzeitanzeige
def update_time():
    reset_color()
    reset_color_bg()

    jetzt = time.localtime()
    stunden = jetzt.tm_hour
    minuten = (jetzt.tm_min // 5) * 5
    rest = jetzt.tm_min % 5
    set_color(es_ist, "purple")

    if minuten == 0:
        set_color(uhr_anzeige, "purple")

    elif minuten == 5:
        set_color(fuenf_min, "purple")
        set_color(nach, "purple")

    elif minuten == 10:
        set_color(zehn_min, "purple")
        set_color(nach, "purple")

    elif minuten == 15:
        set_color(viertel, "purple")
        set_color(nach, "purple")

    elif minuten == 20:
        set_color(zwanzig, "purple")
        set_color(nach, "purple")

    elif minuten == 25:
        set_color(fuenf_min, "purple")
        set_color(vor, "purple")
        set_color(halb, "purple")

    elif minuten == 30:
        set_color(halb, "purple")

    elif minuten == 35:
        set_color(fuenf_min, "purple")
        set_color(nach, "purple")
        set_color(halb, "purple")

    elif minuten == 40:
        set_color(zehn_min, "purple")
        set_color(nach, "purple")
        set_color(halb, "purple")

    elif minuten == 45:
        set_color(dreiviertel, "purple")

    elif minuten == 50:
        set_color(zehn_min, "purple")
        set_color(vor, "purple")

    elif minuten == 55:
        set_color(fuenf_min, "purple")
        set_color(vor, "purple")

    for i in range(rest):
        label_grid_min[i].config(fg="purple")

    anzeige_stunde = stunden

    if minuten >= 25:
        anzeige_stunde += 1
    anzeige_stunde %= 12

    stunden_dict = {
        0: zwoelf,
        1: eins,
        2: zwei,
        3: drei,
        4: vier,
        5: fuenf,
        6: sechs,
        7: sieben,
        8: acht,
        9: neun,
        10: zehn,
        11: elf
    }

    set_color(stunden_dict[anzeige_stunde], "purple")

    uhr.after(1000, update_time)


label_grid = []
label_grid_min = []
# Fenster Erstellung
uhr = tk.Tk()
uhr.title("Wort Uhr")
uhr.config(bg="black")
uhr.geometry("290x460")
uhr.resizable(False, False)

# Buchstaben erzeugen
for r, row in enumerate(letters):
    label_row = []
    for c, char in enumerate(row):
        lbl = tk.Label(uhr, text=char, fg="white", bg="black",
                       font=("Courier", 25))
        lbl.grid(row=r, column=c)
        label_row.append(lbl)
    label_grid.append(label_row)

# Gefundene Wörter Variablen zuweisen
word_pos = find_words(letters, words)

es_ist = word_pos["ES"][0] + word_pos["IST"][0]
viertel = word_pos["VIERTEL"][0]
dreiviertel = word_pos["DREIVIERTEL"][0]
uhr_anzeige = word_pos["UHR"][0]
eins = word_pos["EINS"][0]
zwei = word_pos["ZWEI"][0]
drei = word_pos["DREI"][1]
vier = word_pos["VIER"][1]
fuenf = word_pos["FÜNF"][1]
fuenf_min = word_pos["FÜNF"][0]
sechs = word_pos["SECHS"][0]
sieben = word_pos["SIEBEN"][0]
acht = word_pos["ACHT"][0]
neun = word_pos["NEUN"][0]
zehn = word_pos["ZEHN"][1]
zehn_min = word_pos["ZEHN"][0]
elf = word_pos["ELF"][0]
zwoelf = word_pos["ZWÖLF"][0]
zwanzig = word_pos["ZWANZIG"][0]
nach = word_pos["NACH"][0]
halb = word_pos["HALB"][0]
vor = word_pos["VOR"][0]

# Punkte für Minuten erstellen
for i in range(4):
    lbl2 = tk.Label(uhr, text="●", bg="black", fg="black",
                    font=("Courier", 20))
    lbl2.grid(row=11, column=2 + i * 2)
    label_grid_min.append(lbl2)


minute1 = [(11, 2)]
minute2 = [(11, 4)]
minute3 = [(11, 6)]
minute4 = [(11, 8)]

aktuelle_zeit = time.localtime()
stunden = aktuelle_zeit.tm_hour
minuten = aktuelle_zeit.tm_min


update_time()

uhr.mainloop()
