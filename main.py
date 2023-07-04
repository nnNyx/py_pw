import PySimpleGUI as sg
from dbQueries import *
import pyperclip, random
from password import get_password

sg.theme("Dark Teal 6")


def createGuiInput(searchQuery):
    layout = [
        [
            sg.Text(f"Enter the {searchQuery} you want to search for: "),
            sg.Input(key="_INsearch_"),
        ],
        [sg.Ok(), sg.Cancel()],
    ]
    window = sg.Window("Saved logins", layout, finalize=True)

    while True:
        event, values = window.read()
        userInput = values["_INsearch_"]
        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break
        if event == "Ok":
            if not userInput:
                window.close()
                sg.popup(f"{searchQuery} is required")
                return ""
            else:
                window.close()
                return userInput
    window.close()


def output(case):
    # isGuiInput = False
    if case == 1:
        data = [
            [idNum, user, email, site, pwd]
            for idNum, user, email, site, pwd in search_user(createGuiInput("username"))
        ]
        # isGuiInput = True
    elif case == 2:
        data = [
            [idNum, user, email, site, pwd]
            for idNum, user, email, site, pwd in search_email(createGuiInput("email"))
        ]
        # isGuiInput = True
    elif case == 3:
        data = [i for i in search_site(createGuiInput("website"))]
        # isGuiInput = True
    elif case == 4:
        data = [
            [idNum, username, email, site, pwd]
            for idNum, username, email, site, pwd in search_all()
        ]
        # isGuiInput = False

    layout = [
        [
            sg.Table(
                data,
                headings=["ID", "Username", "E-Mail", "Website", "Password"],
                justification="center",
                enable_events=True,
                key="-TABLE-",
                select_mode=sg.TABLE_SELECT_MODE_BROWSE,
            )
        ],
        [
            sg.Button(
                button_text="Copy password",
                key="_COPY_",
            )
        ],
        [sg.Button(button_text="Close", key="Cancel")],
    ]
    window = sg.Window("Saved logins", layout, finalize=True, element_justification="c")

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break
        if event == "_COPY_":
            table = values["-TABLE-"]
            a = table[0]
            print(data[table[0]][4])
            pyperclip.copy(data[a][4])
            sg.popup("Password copied!")
    window.close()


def creation():
    layout = [
        [
            sg.Text("Username:"),
            sg.Input(s=(40, 1), expand_x="true", expand_y="true", key="_username_"),
        ],
        [
            sg.Text("E-Mail: "),
            sg.Input(s=(40, 1), expand_x="true", expand_y="true", key="_email_"),
        ],
        [
            sg.Text("Website: "),
            sg.Input(s=(40, 1), expand_x="true", expand_y="true", key="_site_"),
        ],
        [
            sg.Text("Password length: "),
            sg.Slider(
                range=(8, 100),
                default_value=20,
                orientation="horizontal",
                key="_length_",
            ),
        ],
        [sg.Ok(), sg.Cancel()],
    ]
    window = sg.Window("User/Pwd Gen", layout, finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break
        elif event == "Ok":
            username, email, site, passLen = (
                values["_username_"],
                values["_email_"],
                values["_site_"],
                values["_length_"],
            )
            if not username:
                sg.popup("A username is required")
            elif not email:
                sg.popup("An email is required")
            elif not site:
                sg.popup("A website is required")
            else:
                create_user(username, email, site, int(passLen))
                break
    window.close()


def generatePassword(amount):
    password = ""

    for i in range(amount):
        x = random.randint(33, 126)
        password += chr(x)
    return password


def create_user(username, email, site, passLen):
    password = generatePassword(passLen)
    pyperclip.copy(password)

    make_user(username, email, site, password)
    print(f"Created user {username} & copied password to clipboard!")


def logicHandler(x):
    if x == 1:
        creation()
    elif 1 < x < 6:
        output(x - 1)


def genMenu():
    layout = [
        [sg.Text("Create new account"), sg.Button(button_text="Create", key="_Btn1_")],
        [sg.Text("Search by username"), sg.Button(button_text="Search", key="_Btn2_")],
        [sg.Text("Search by email"), sg.Button(button_text="Search", key="_Btn3_")],
        [sg.Text("Search by website"), sg.Button(button_text="Search", key="_Btn4_")],
        [sg.Text("Show all accounts"), sg.Button(button_text="Show", key="_Btn5_")],
    ]
    window = sg.Window("Menu", layout, finalize=True, element_justification="c")

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == "_Btn1_":
            logicHandler(1)
        if event == "_Btn2_":
            logicHandler(2)
        if event == "_Btn3_":
            logicHandler(3)
        if event == "_Btn4_":
            logicHandler(4)
        if event == "_Btn5_":
            logicHandler(5)

    window.close()


def main():
    layout = [[sg.Text("Password:"), sg.Input(key="_pwd_")], [sg.Ok(), sg.Cancel()]]
    window = sg.Window("Menu", layout, finalize=True, element_justification="c")

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break
        if event == "Ok":
            if values["_pwd_"] == get_password():
                window.close()
                genMenu()
            else:
                sg.Popup("Incorrect password")
                window.close()
    window.close()


if __name__ == "__main__":
    main()
