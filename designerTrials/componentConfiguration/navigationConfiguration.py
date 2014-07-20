## configuration for navigation bar
import sys,os

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


imageFileFolder = "imageFiles\\"

navBarBackgroundColor = '#A8ACAF'

## icons for area 1
navigationBackStandardTheme1 = resource_path(imageFileFolder+"navigationImages/Text Box_BACKWARDBT_ABC.svg")
navigationBackHoverTheme1 = resource_path(imageFileFolder+"navigationImages/Text Box_BACKWARDBT_A_CURSORSTAND.svg")

navigationFowardStandardTheme1 = resource_path(imageFileFolder+"navigationImages/Text Box_FORWARDBT_ABC.svg")
navigationFowardHoverTheme1 = resource_path(imageFileFolder+"navigationImages/Text Box_FORWARDBT_A_CURSORSTAND.svg")

## icons for area 2

navigationBackStandardTheme2 = resource_path(imageFileFolder+"navigationImages/Text Box_BACKWARDBT_ABC.svg")
navigationBackHoverTheme2 = resource_path(imageFileFolder+"navigationImages/Text Box_BACKWARDBT_B_CURSORSTAND.svg")

navigationFowardStandardTheme2 = resource_path(imageFileFolder+"navigationImages/Text Box_FORWARDBT_ABC.svg")
navigationFowardHoverTheme2 = resource_path(imageFileFolder+"navigationImages/Text Box_FORWARDBT_B_CURSORSTAND.svg")

## icons for area 3
navigationBackStandardTheme3 = resource_path(imageFileFolder+"navigationImages/Text Box_BACKWARDBT_ABC.svg")
navigationBackHoverTheme3 = resource_path(imageFileFolder+"navigationImages/Text Box_BACKWARDBT_C_CURSORSTAND.svg")

navigationFowardStandardTheme3 = resource_path(imageFileFolder+"navigationImages/Text Box_FORWARDBT_ABC.svg")
navigationFowardHoverTheme3 = resource_path(imageFileFolder+"navigationImages/Text Box_FORWARDBT_C_CURSORSTAND.svg")