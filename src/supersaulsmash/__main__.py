from supersaulsmash.loginGUI import LoginGUI
from supersaulsmash.supersaulsmash import SuperSaulSmash

login_gui = LoginGUI()

# run login gui and get username and host ip
response = login_gui.run()

login_gui.window.close()

print("Finished login")

# if the user closes the window
if response == None:
    sys.exit()

username, ip = response

game = SuperSaulSmash(ip)

game.run()
