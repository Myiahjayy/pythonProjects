from tkinter import *
import requests

def weather(canvas):
    zipcode = textField.get()
    api = "http://api.openweathermap.org/data/2.5/weather?zip=" + zipcode + "&units=imperial&appid=81e7f187b4f94b2f0871eecb8811b43f"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['description'].title()
    temp = int(json_data['main']['temp'])
    min_temp = int(json_data['main']['temp'])
    max_temp = int(json_data['main']['temp'])
    wind = json_data['wind']['speed']
    humidity = json_data['main']['humidity']

    final_info = condition + "\n" + str(temp) + "°F"
    final_temps = "\n" + "Max Temp: " + str(max_temp) + "°F" + "\n" + "Min temp: " + str(min_temp) + "°F"
    final_humidity_wind = "Humidity: " + str(humidity) + "\n" + "wind: " + str(wind)
    label1.config(text=final_info)
    label2.config(text=final_temps)
    label3.config(text=final_humidity_wind)

canvas = Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
canvas.configure(bg="light blue")

f = ("poppins", 15, "bold")
t = ("poppins", 35)
h = ("poppins", 20, "bold")

greeting = "Enter a zipcode: "
greeting_label = Label(canvas, font=t, text=greeting, bg="light blue")
greeting_label.pack()
textField = Entry(canvas, font=t, justify='center')
textField.pack(pady=20)
textField.focus()
textField.bind("<Return>", weather)

label1 = Label(canvas, font=t, bg="light blue")
label1.pack()
label2 = Label(canvas, font=f, bg="light blue")
label2.pack()
label3 = Label(canvas, font=f, bg="light blue")
label3.pack()
label4 = Label(canvas, font=t, bg="light blue")
label4.pack()

canvas.mainloop()
