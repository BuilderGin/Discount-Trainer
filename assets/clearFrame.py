'''
Created on Feb 02, 2022
@summary: Clear the Window Frame
@author: git:buildergin
Update on Feb 02, 2022
'''

# #############################################
# Clearing all child frames
# #############################################


def clearAll(self):
    # Destroy Everything in Home
    child = clear(self)
    home_btn = destroy_home_btn(self)
    self.header_frame.destroy()
    self.container_frame.destroy()
    self.footer_frame.destroy()


def clear(self):
    # Destroy each child label or frame
    for child in self.header_frame.winfo_children():
        child.destroy()

    for child in self.container_frame.winfo_children():
        child.destroy() 
    
    for child in self.footer_frame.winfo_children():
        child.destroy()


def clear_capture(self):
    self.cap_frame.destroy() 
    self.camera_frame.destroy() 


def destroy_home_btn(self):
    self.home_button_frame.destroy() 
    self.home_squats.destroy() 
    self.home_biceps.destroy() 
    self.home_template3.destroy() 

def destroy_about_btn(self):
    self.about_back_to_menu.destroy() 
    self.about_gitlink.destroy() 