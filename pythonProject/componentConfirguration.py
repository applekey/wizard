import os,sys

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


imageFileFolder = "imageFiles\\"


### configuration items for awsomePlayer
configPlaySVGLocation= resource_path(imageFileFolder+"volumeSliderImages\VideoBar_B_2_PLAY.svg")
configureStopSVGLocation = resource_path(imageFileFolder+"volumeSliderImages\VideoBar_C_1_SLIDEBUTTON.svg")
configFullScreenSVGLocation = resource_path(imageFileFolder+"volumeSliderImages\VideoBar_B_2_FULLSCREEN.svg")
volumeSliderIcon = resource_path(imageFileFolder+"volumeSliderImages\VideoBar_A_2_SOUND.svg")
volumeSliderMuteIcon=resource_path(imageFileFolder+"volumeSliderImages\VideoBar_C_1_SOUND.svg")

print configPlaySVGLocation
print configureStopSVGLocation
print configFullScreenSVGLocation

#videoScrollNubScanning = os.getcwd()+"\\volumeSliderImages\\nub.svg"
videoScrollNubScanning = ":general/nub.svg"


qSliderStyle=" \
QSlider::groove:horizontal {\
border: 1.5px solid #A8ACAF;\
background: white;\
height: 18px;\
border-radius: 10px;\
}\
QSlider::handle:horizontal {\
image: url("+ videoScrollNubScanning+");\
}\
"
print qSliderStyle

### configuration items for banner

activeColors = ['#1ABC9C','#F1C40F','#E74C3B']
inactiveColors = ['#A8ACAF','#99A3A3','#879191']
activeIcons =[resource_path(imageFileFolder+"bannerImages/0__A_1_ICON80.svg"),resource_path(imageFileFolder+"bannerImages/0__B_1_ICON80.svg"),resource_path(imageFileFolder+"bannerImages/0__C_1_ICON80.svg")]
inactiveIcons =[resource_path(imageFileFolder+"bannerImages/0__A_2_ICON80.svg"),resource_path(imageFileFolder+"bannerImages/0__B_2_ICON80.svg"),resource_path(imageFileFolder+"bannerImages/0__C_2_ICON80.svg")]
bannerText = ['Scanning','Modeling','Printing']
bannerIconWidth = 60

#fonts
fontFile = resource_path("resources/OpenSans-Bold.ttf")
fontName  = "Open Sans"
fontSize = 20




## configuration for awsomeText
awsomeTextBackGroundColor = '#A8ACAF'

## configuration for awsomedialogue
awsomeDialogStyle = "\
background: #ecf0f1;\
border-width: 2px;\
border-color: #1ABC9C;\
}"


## banner constants
firstButtonWidthPercentage = 0.65
bannerHeightPixelsPercentage = 0.05  # this is the relationship between the height of the width of the bar and the height, height = bannerHeightPixelsPercentage*width
iconWidth = 100
bannerHeightAbsolute = 80
bannerCurvaturePercentage = 0.5

## videoPlayer constants
videoPlayerBackgroundColor = "#ecf0f1"

## textFrame constantts
textFrameBackgroundColor =  "#95a5a6"

##awsome Slider constatns
awsomeSliderNumberDisplayStyle = "\
background:transparent;\
border-style: outset;\
border-radius: 10px;\
border-width: 2px;\
border-color: #FFFFFF\
"

awsomeSliderStyle=" \
QSlider::groove:horizontal {\
border: 1.3px solid #FFFFFF;\
background: transparent;\
height: 18px;\
border-radius: 10px;\
}\
QSlider::handle:horizontal {\
image: url("+ videoScrollNubScanning+");\
}\
"

## textedit scrollbar config
scrollBarStyle = "\
QScrollBar:verticle  {\
    border: 2px solid grey;\
    background: transparent;\
	border-radius: 30px;\
}\
QScrollBar::handle:verticle  {\
    background: white;\
    min-height: 80px;\
    border: 1px solid grey;\
	border-radius: 7px;\
}\
"






