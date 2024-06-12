from tkinter import *
import os
from PIL import ImageTk, Image
import random
from tkinter import messagebox
import sys

# Get the username from command-line arguments
username = sys.argv[1]

# Read scores from the file
def read_scores():
    scores = {}
    try:
        with open("scores.txt", "r") as f:
            for line in f:
                data = line.strip().split(", ")
                if len(data) == 3:
                    user = data[0].split(": ")[1]
                    score = int(data[2].split(": ")[1])
                    scores[user] = score
    except FileNotFoundError:
        pass
    return scores

# Update score in the file
def update_score(username, score):
    scores = read_scores()
    scores[username] = score
    with open("scores.txt", "w") as f:
        for user, scr in scores.items():
            f.write(f"Username: {user}, Score: {scr}\n")
    # Update highest score if needed
    highest_score_user, highest_score = get_highest_score()
    if score > highest_score:
        write_highest_score(username, score)

# Write the highest score to the file
def write_highest_score(username, score):
    with open("highest_score.txt", "w") as f:
        f.write(f"Highest Score User: {username}, Score: {score}\n")

# Get the highest score and player name
def get_highest_score():
    try:
        with open("highest_score.txt", "r") as f:
            line = f.readline()
            data = line.strip().split(", ")
            highest_score_user = data[0].split(": ")[1]
            highest_score = int(data[1].split(": ")[1])
            return highest_score_user, highest_score
    except FileNotFoundError:
        return None, 0

# FRAME 3
# flat, groove, raised, ridge, solid, or sunken
def a_btn(event=""):
    letter = "A"
    check(letter)


def b_btn(event=""):
    letter = "B"
    check(letter)


def c_btn(event=""):
    letter = "C"
    check(letter)


def d_btn(event=""):
    letter = "D"
    check(letter)


def e_btn(event=""):
    letter = "E"
    check(letter)


def f_btn(event=""):
    letter = "F"
    check(letter)


def g_btn(event=""):
    letter = "G"
    check(letter)


def h_btn(event=""):
    letter = "H"
    check(letter)


def i_btn(event=""):
    letter = "I"
    check(letter)


def j_btn(event=""):
    letter = "J"
    check(letter)


def k_btn(event=""):
    letter = "K"
    check(letter)


def l_btn(event=""):
    letter = "L"
    check(letter)


def m_btn(event=""):
    letter = "M"
    check(letter)


def n_btn(event=""):
    letter = "N"
    check(letter)


def o_btn(event=""):
    letter = "O"
    check(letter)


def p_btn(event=""):
    letter = "P"
    check(letter)


def q_btn(event=""):
    letter = "Q"
    check(letter)


def r_btn(event=""):
    letter = "R"
    check(letter)


def s_btn(event=""):
    letter = "S"
    check(letter)


def t_btn(event=""):
    letter = "T"
    check(letter)


def u_btn(event=""):
    letter = "U"
    check(letter)


def v_btn(event=""):
    letter = "V"
    check(letter)


def w_btn(event=""):
    letter = "W"
    check(letter)


def x_btn(event=""):
    letter = "X"
    check(letter)


def y_btn(event=""):
    letter = "Y"
    check(letter)


def z_btn(event=""):
    letter = "Z"
    check(letter)


hint_chance = 2

def hint_btn():
    global hint_chance
    if 0 < hint_chance <= 2:
        reveal_word = random.randint(0, len(letter_into_word) - 1)
        check(letter_into_word[reveal_word])
        hint_chance -= 1
    else:
        messagebox.showerror("error", "you exceed the hint limit")

answers = ['ANT', 'BABOON', 'BAT', 'CAMEL', 'DONKEY', 'EAGLE', 'GOOSE', 'HAWK', 'MONKEY', 'MOUSE', 'FISH',
           'PYTHON', 'PIGEON', 'RHINOCEROS', 'HIPPOPOTAMUS', 'ZEBRA', 'PANDA', 'RAVEN', 'HUMAN', 'OWL', 'SHARK',
           'PIZZA', 'BURGER', 'SAMOSA', 'BUTTER', 'CHUTNEY', 'NOODLES', 'DOSA',
           'MANGO', 'BANANA', 'POMEGRANATE', 'PAPAYA', 'WATERMELON', 'MUSKMELON', 'DATES',
           'MAGNETISM', 'ELECTRICITY']
import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk

letter_into_word = [0]
variable = [0]
chance = 1
total_score = 0

def check(press_button):
    global chance, total_score, hangman_image

    if chance <= 6:
        numeric_val = ord(press_button) - 65

        try:
            no_of_times = letter_into_word.count(press_button)
            letter_into_word.index(press_button)

            for repeat in range(no_of_times):
                pos = letter_into_word.index(press_button)
                variable[pos].config(text=press_button)
                button_variable_list[numeric_val].config(state="disable", bg="green", fg="white")
                letter_into_word.pop(pos)
                variable.pop(pos)

            if not letter_into_word:
                messagebox.showinfo("WIN!!!", "You Win!! :-)")
                total_score += 5
                update_score(username, total_score) 
                score.destroy()
                exitbutton.destroy()
                hangman_image_label.destroy()
                frame1.destroy()
                frame2.destroy()
                frame3.destroy()
                letter_into_word.clear()
                button_variable_list.clear()
                variable.clear()
                main()
                chance = 1

        except:
            chance += 1
            button_variable_list[numeric_val].config(state="disable", bg="red", fg="white")
            hangman_imagelocation = os.path.abspath(f'hangman_visual\\{chance}.png')
            hangman_image_open = Image.open(hangman_imagelocation)
            hangman_image_resize = hangman_image_open.resize((300, 300))
            hangman_image = ImageTk.PhotoImage(hangman_image_resize)
            hangman_image_label.config(image=hangman_image)

    else:
        messagebox.showerror("LIMIT EXCEED", "you exceed the limit computer win the game")
        update_score(username, total_score) 
        score.destroy()
        exitbutton.destroy()
        hangman_image_label.destroy()
        frame1.destroy()
        frame2.destroy()
        frame3.destroy()
        chance = 1
        letter_into_word.clear()
        button_variable_list.clear()
        variable.clear()
        main()

def main_word():
    global hint_chance
    word_pos = random.randint(0, len(answers) - 1)
    words = answers[word_pos]
    hint_chance = 2

    letter_into_word.clear()
    variable.clear()

    for word in words:
        letter_into_word.append(word)

    for_column_start_pos = round((12 - len(letter_into_word)) / 2)
    for position in range(len(letter_into_word)):
        variable.append(chr(random.randint(65, 91)))
        variable[position] = tk.Label(frame3, relief="solid", width=8, bd=4)
        variable[position].grid(row=0, column=for_column_start_pos + position, ipady=5, pady=10)



def main():
    def frames():
        global frame1, frame2, frame3, left_side, right_side
        
        frame1 = Frame(root,bg="#F49DA2")
        frame1.pack()
        left_side = Frame(frame1,bg="#F49DA2")
        left_side.pack(side=LEFT, ipadx=128)
        right_side = Frame(frame1,bg="#F49DA2")
        right_side.pack(side=LEFT)
        frame2 = Frame(root)
        frame2.pack()
        frame3 = Frame(root,bg="#F49DA2")
        frame3.pack(pady=15)

    global score, exitbutton, hangman_image_label

    frames()
    main_word()
    #  FRAME 1
    score = Label(left_side, text=f"Score : {total_score}", width=10)
    score.pack(padx=30, side="left", ipady=5)

    billlogin_btn_image_location = os.path.abspath('hangman_visual\\Hangman.png')
    billlogin_btn_opened_image = Image.open(billlogin_btn_image_location)
    billlogin_btn_resize_image = billlogin_btn_opened_image.resize((400, 100))
    global bill_login_image
    bill_login_image = ImageTk.PhotoImage(billlogin_btn_resize_image)
    score = Label(left_side, image=bill_login_image, bg="#F49DA2")
    score.pack(ipadx=60, pady=10)

    exitbutton = Button(right_side, text="Exit", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=exit)
    exitbutton.pack(side="right", ipady=5, padx=15)
    #  FRAME 2
    hangman_imagelocation = os.path.abspath('hangman_visual\\1.png')
    hangman_image_open = Image.open(hangman_imagelocation)
    hangman_image_resize = hangman_image_open.resize((300, 300))
    global hangman_image
    hangman_image = ImageTk.PhotoImage(hangman_image_resize)
    hangman_image_label = Label(frame2, image=hangman_image)
    hangman_image_label.pack()

    a_button = Button(frame3, text="A", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=a_btn)
    a_button.grid(row=1, column=0, ipady=5)
    button_variable_list.append(a_button)
    b_button = Button(frame3, text="B", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=b_btn)
    b_button.grid(row=1, column=1, ipady=5)
    button_variable_list.append(b_button)
    c_button = Button(frame3, text="C", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=c_btn)
    c_button.grid(row=1, column=2, ipady=5)
    button_variable_list.append(c_button)
    d_button = Button(frame3, text="D", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=d_btn)
    d_button.grid(row=1, column=3, ipady=5)
    button_variable_list.append(d_button)
    e_button = Button(frame3, text="E", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=e_btn)
    e_button.grid(row=1, column=4, ipady=5)
    button_variable_list.append(e_button)
    f_button = Button(frame3, text="F", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=f_btn)
    f_button.grid(row=1, column=5, ipady=5)
    button_variable_list.append(f_button)
    g_button = Button(frame3, text="G", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=g_btn)
    g_button.grid(row=1, column=6, ipady=5)
    button_variable_list.append(g_button)
    h_button = Button(frame3, text="H", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=h_btn)
    h_button.grid(row=1, column=7, ipady=5)
    button_variable_list.append(h_button)
    i_button = Button(frame3, text="I", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=i_btn)
    i_button.grid(row=1, column=8, ipady=5)
    button_variable_list.append(i_button)
    j_button = Button(frame3, text="J", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=j_btn)
    j_button.grid(row=1, column=9, ipady=5)
    button_variable_list.append(j_button)
    k_button = Button(frame3, text="K", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=k_btn)
    k_button.grid(row=1, column=10, ipady=5)
    button_variable_list.append(k_button)
    l_button = Button(frame3, text="L", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=l_btn)
    l_button.grid(row=1, column=11, ipady=5)
    button_variable_list.append(l_button)
    m_button = Button(frame3, text="M", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=m_btn)
    m_button.grid(row=2, column=1, ipady=5)
    button_variable_list.append(m_button)
    n_button = Button(frame3, text="N", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=n_btn)
    n_button.grid(row=2, column=2, ipady=5)
    button_variable_list.append(n_button)
    o_button = Button(frame3, text="O", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=o_btn)
    o_button.grid(row=2, column=3, ipady=5)
    button_variable_list.append(o_button)
    p_button = Button(frame3, text="P", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=p_btn)
    p_button.grid(row=2, column=4, ipady=5)
    button_variable_list.append(p_button)
    q_button = Button(frame3, text="Q", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=q_btn)
    q_button.grid(row=2, column=5, ipady=5)
    button_variable_list.append(q_button)
    r_button = Button(frame3, text="R", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=r_btn)
    r_button.grid(row=2, column=6, ipady=5)
    button_variable_list.append(r_button)
    s_button = Button(frame3, text="S", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=s_btn)
    s_button.grid(row=2, column=7, ipady=5)
    button_variable_list.append(s_button)
    t_button = Button(frame3, text="T", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=t_btn)
    t_button.grid(row=2, column=8, ipady=5)
    button_variable_list.append(t_button)
    u_button = Button(frame3, text="U", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=u_btn)
    u_button.grid(row=2, column=9, ipady=5)
    button_variable_list.append(u_button)
    v_button = Button(frame3, text="V", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=v_btn)
    v_button.grid(row=3, column=3, ipady=5)
    button_variable_list.append(v_button)
    w_button = Button(frame3, text="W", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=w_btn)
    w_button.grid(row=3, column=4, ipady=5)
    button_variable_list.append(w_button)
    x_button = Button(frame3, text="X", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=x_btn)
    x_button.grid(row=3, column=5, ipady=5)
    button_variable_list.append(x_button)
    y_button = Button(frame3, text="Y", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=y_btn)
    y_button.grid(row=3, column=6, ipady=5)
    button_variable_list.append(y_button)
    z_button = Button(frame3, text="Z", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=z_btn)
    z_button.grid(row=3, column=7, ipady=5)
    button_variable_list.append(z_button)
    hint_button = Button(frame3, text="Hint", bg="peachpuff", relief="groove", font=("century",9,"bold"), bd=4, width=8, command=hint_btn)
    hint_button.grid(row=3, column=11, ipady=5)

    root.bind('<a>', a_btn)
    root.bind('<A>', a_btn)
    root.bind('<b>', b_btn)
    root.bind('<B>', b_btn)
    root.bind('<c>', c_btn)
    root.bind('<C>', c_btn)
    root.bind('<d>', d_btn)
    root.bind('<D>', d_btn)
    root.bind('<e>', e_btn)
    root.bind('<E>', e_btn)
    root.bind('<f>', f_btn)
    root.bind('<F>', f_btn)
    root.bind('<g>', g_btn)
    root.bind('<G>', g_btn)
    root.bind('<h>', h_btn)
    root.bind('<H>', h_btn)
    root.bind('<i>', i_btn)
    root.bind('<I>', i_btn)
    root.bind('<j>', j_btn)
    root.bind('<J>', j_btn)
    root.bind('<k>', k_btn)
    root.bind('<K>', k_btn)
    root.bind('<l>', l_btn)
    root.bind('<L>', l_btn)
    root.bind('<m>', m_btn)
    root.bind('<M>', m_btn)
    root.bind('<n>', n_btn)
    root.bind('<N>', n_btn)
    root.bind('<o>', o_btn)
    root.bind('<O>', o_btn)
    root.bind('<p>', p_btn)
    root.bind('<P>', p_btn)
    root.bind('<q>', q_btn)
    root.bind('<Q>', q_btn)
    root.bind('<r>', r_btn)
    root.bind('<R>', r_btn)
    root.bind('<s>', s_btn)
    root.bind('<S>', s_btn)
    root.bind('<t>', t_btn)
    root.bind('<T>', t_btn)
    root.bind('<u>', u_btn)
    root.bind('<U>', u_btn)
    root.bind('<v>', v_btn)
    root.bind('<V>', v_btn)
    root.bind('<w>', w_btn)
    root.bind('<W>', w_btn)
    root.bind('<x>', x_btn)
    root.bind('<X>', x_btn)
    root.bind('<y>', y_btn)
    root.bind('<Y>', y_btn)
    root.bind('<z>', z_btn)
    root.bind('<Z>', z_btn)



if __name__ == "__main__":
    root = Tk()
    root.title("hangman") 
    try:
        Image_icon = PhotoImage(file="hangman_visual/Hangman.png")
        root.iconphoto(False, Image_icon)
    except Exception as e:
        print(f"Error loading icon: {e}")
    root.config(bg="#F49DA2")
    root.resizable(0,0)

    button_variable_list = []

    main()
    root.mainloop()
