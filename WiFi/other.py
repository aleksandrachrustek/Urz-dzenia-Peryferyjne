import os
import time
import socket
import tqdm

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096


# os.system("wmic nic get name, index")
# os.system("wmic path win32_networkadapter where index=4 call disable")
# os.system("wmic path win32_networkadapter where index=4 call enable")
# os.system("netsh interface show interface")

def createNewConnection(name):
    config = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
<name>""" + name + """</name>
    <SSIDConfig>
        <SSID>
            <name>""" + name + """</name>
        </SSID>
    </SSIDConfig>
<connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>open</authentication>
                <encryption>none</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
        </security>

    </MSM>
</WLANProfile>"""
    command = "netsh wlan add profile filename=\"" + name + ".xml\"" + " interface=Wi-Fi"
    with open(name + ".xml", 'w') as file:
        file.write(config)
    os.system(command)


def deleteConnection(name):
    command = "netsh wlan delete profile " + name


def connect(name):
    command = "netsh wlan connect name=\"" + name + "\" ssid=\"" + name + "\" interface=Wi-Fi"
    os.system(command)


# function to display avavilabe Wifi networks
def displayAvailableNetworks():
    os.system("netsh wlan show networks interface=Wi-Fi")


def enableWiFiCard():
    os.system("netsh interface set interface Wi-Fi enable")
    print("Wlaczono karte sieciowa Wi-Fi")
    time.sleep(5)
    displayAvailableNetworks()


def disableWiFiCard():
    os.system("netsh interface set interface Wi-Fi disable")
    print("Wylaczono karte sieciowa Wi-Fi")


def main():
    enableWiFiCard()
    name_of_router = input('\n\nEnter Name of Wi-Fi network you want to connect to: ')
    deleteConnection(name_of_router)
    time.sleep(3)
    createNewConnection(name_of_router)
    connect(name_of_router)
    while (True):
        choose = input("Choose menu option: ")
        if (choose == "1"):
            print("File transfer")
            s = socket.socket()
            host = socket.gethostname

            # host = input("Where you want to put your files (ip)?")
            port = 55555
            s.bind((host, port))
            s.listen(5)
            while True:
                c, addr = s.accept()
            # s.connect(('192.168.1.100', port))
            # s.send("Hi")

        if (choose == "0"):
            disableWiFiCard()
            return


main()