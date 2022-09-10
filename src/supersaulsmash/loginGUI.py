import PySimpleGUIWx as gui

class LoginGUI:
    def __init__(self):

        gui.theme("System Default 1")

        self.layout = [
            [gui.Text("")],
            [gui.Text("Username")],
            [gui.Input(key = "-USERNAME-", size = (120,30))],
            [gui.Text("")],
            [gui.Text("IP Address")],
            [gui.Input(key = "-IP_ADDRESS-", size = (120,30))],
            [gui.Text("")],
            [gui.Button("Join", key = "-JOIN-"), gui.Button("Create", key = "-CREATE-")],
        ]

        self.window = gui.Window("Live Chat", self.layout)

    def run(self):
        # update the gui based on user inputs

        while True:

            event, values = self.window.read()

            print(event)

            username, ip = (values["-USERNAME-"], values["-IP_ADDRESS-"])

            if event == None:
                self.window.close()

                return

            elif event == "-JOIN-":
                # join server
                return (username, ip)

            elif event == "-CREATE-":
                # create server
                pass
