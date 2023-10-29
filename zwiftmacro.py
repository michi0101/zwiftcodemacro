import pyautogui
import time

codes = ["Goalienware",
    "ATOC2015",
    "GOAMGENTOC",
    "GOBATTENKILL",
    "BICYCLINGMAG",
    "BIKERADAR",
    "BIKEANDBEER",
    "CANBERRACCKIT",
    "GOCIS",
    "CRCANYC",
    "GOCYCLEOPS",
    "GOELITE",
    "GOFREESPEED",
    "GoGCN",
    "GEARPATROL",
    "GEELONGCCKIT",
    "GOLDCOAST",
    "GOLONGRIDERS",
    "GOVISION",
    "GOINGAMBA",
    "Hikkit32616",
    "JENSIE",
    "LAFUGA.CC",
    "LAVA",
    "MDCCKit",
    "MTSKIT",
    "MGCCKit",
    "NCCMAKIT",
    "PCGKIT32516",
    "GOPEARSON",
    "RIDEPOWERTAP",
    "RIDEQUARQ",
    "RADAVIST",
    "RIDEAUSTRALIA",
    "ROAD.CC",
    "GOSKRYE",
    "SIGMASPORT",
    "SLOWTWITCH",
    "SOIGNEURDK",
    "STKILDA2015KIT",
    "SYDNEYCCKIT",
    "GOTACX",
    "TDP2015",
    "GOTRAINSHARP",
    "TRIATHLETEMAG",
    "TSBIKES",
    "GOUSMES",
    "VCGHKIT",
    "WAHOOFITNESS",
    "GOWBR",
    "GOWSR",
    "ZTHKIT"]

def enterCode(word):
    time.sleep(0.5)
    pyautogui.typewrite("p")
    time.sleep(0.5)
    pyautogui.typewrite(word)

time.sleep(1)

for word in codes:
    enterCode(word)