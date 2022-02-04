'''
Created on Jan 26, 2022
@summary: Head Function
@author: git:buildergin
Update on Feb 03, 2022
'''

# #############################################
# Own Files Import
# #############################################
from windows.splash import splashScreen
from windows.menu import main_root

# HERE UNDER START THE FUNCTIONALITIES
def splash_window():
    # SPLASH SCREEN
    splys = splashScreen()

    spl_screen_width = splys.root.winfo_screenwidth()
    spl_screen_height = splys.root.winfo_screenheight()
    spl_window_width = int(spl_screen_width / 3.5)  
    spl_window_height = int(spl_screen_height / 3)

    # Coordinates of the upper left corner of the window to make the window appear in the center
    spl_x_cordinate = int((spl_screen_width/2) - (spl_window_width/2))
    spl_y_cordinate = int((spl_screen_height/2) - (spl_window_height/2))

    splys.root.geometry(("%dx%d+%d+%d" % (spl_window_width,spl_window_height, spl_x_cordinate, spl_y_cordinate)))

    # Wait 4 seconds and destroy splash window
    splys.root.after(4000, lambda: splys.root.destroy())
    splys.root.mainloop()

    main_root()



def main():
    START_SPLASH_WINDOW = splash_window()


if __name__ == '__main__':
    main()


