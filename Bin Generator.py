import PySimpleGUI as sg
from threading import Thread
import rstr
import requests
from concurrent.futures import ThreadPoolExecutor
import datetime

x = datetime.datetime.now()

generated_Bins = []


class gen_Bin:
    def Mastercard(self):
        generated_Bins.append(rstr.xeger(str(5) + "\d{5}"))

    def Visa(self):
        generated_Bins.append(rstr.xeger(str(4) + "\d{5}"))

    def Amex(self):
        generated_Bins.append(rstr.xeger(str(3) + "\d{5}"))

    def Discover(self):
        generated_Bins.append(rstr.xeger(str(6) + "\d{5}"))


def check_Bin(Bin):
    url = f"https://binlist.io/lookup/{Bin}"
    datas = requests.get(url).json()

    if datas['success'] == True:
        window['bins'].print(f"Bin      :  {Bin}\n"
                             f"Scheme   :  {datas['scheme']}\n"
                             f"Country  :  {datas['country']['name']}\n"
                             f"Type     :  {datas['type']}\n"
                             f"Category :  {datas['category']}\n"
                             f"Bank     :  {datas['bank']['name']}\n________________________")


def run1():
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(check_Bin, Bin) for Bin in generated_Bins]
        executor.shutdown(wait=True)


def genetator(no, type):
    if type == "Mastercard":

        for i in range(no):
            gen_Bin().Mastercard()
        Thread(target=run1).start()

    elif type == "Visa":

        for i in range(no):
            gen_Bin().Visa()
        Thread(target=run1).start()

    elif type == "Amex":

        for i in range(no):
            gen_Bin().Amex()
        Thread(target=run1).start()

    elif type == "Discover":

        for i in range(no):
            gen_Bin().Discover()
        Thread(target=run1).start()


Layout = [
    [sg.Text("Valid Credit Card Bin Generator", font=("", 25))],
    [sg.Text("Developed By Henry Richard J", font=("", 13))],
    [sg.Multiline(size=(55, 22), disabled=True, key="bins")],
    [sg.Text("Number of Bins to generate:")],
    [sg.Slider(range=(1, 5000), default_value=5, size=(15, 20), font=("", 10), key="Number_OF_Bins",
               tooltip="Use The Slider To Choose Number Of Bins To Be Generated", orientation="horizontal")],
    [sg.Button("Generate Mastercard", size=(20, 2), font=("", 15), key="Generate_Mastercard"),
     sg.Button("Generate Visa", size=(20, 2), font=("", 15), key="Generate_Visa")],
    [sg.Button("Generate Amex", size=(20, 2), font=("", 15), key="Generate_Amex"),
     sg.Button("Generate Discover", size=(20, 2), font=("", 15), key="Generate_Discover")],
    [sg.Button("Save", size=(20, 2), font=("", 15), key="Save_Bin")]
]

window = sg.Window('Valid Credit Card Bin Generator', Layout, element_justification='center')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "Generate_Mastercard":
        generated_Bins.clear()
        no_of_bins = int(values["Number_OF_Bins"])
        Thread(target=genetator(no_of_bins, "Mastercard")).start()

    if event == "Generate_Visa":
        generated_Bins.clear()
        no_of_bins = int(values["Number_OF_Bins"])
        Thread(target=genetator(no_of_bins, "Visa")).start()

    if event == "Generate_Amex":
        generated_Bins.clear()
        no_of_bins = int(values["Number_OF_Bins"])
        Thread(target=genetator(no_of_bins, "Amex")).start()

    if event == "Generate_Discover":
        generated_Bins.clear()
        no_of_bins = int(values["Number_OF_Bins"])
        Thread(target=genetator(no_of_bins, "Discover")).start()

    if event == 'Save_Bin':
        open(f"Results\\[Valid Bins] {x.strftime('%d-%m-%y %I-%M-%S-%p')}.txt", "a").write(values["bins"])
        sg.popup("Bins Saved in Results folder!")
