import requests

from tkinter import *
from tkinter import ttk




class weatherAPI:
  def __init__(self, url):
      self.api_url = url
      
  def __str__(self):
      return self.result

  def getWeather(self):
      try:
        
        result = requests.get(self.api_url).json()
        
        self.weather = result['current_weather']
        
        dailyStats = ['temperature_2m_max',
                     'temperature_2m_min', 'sunrise', 'sunset', 'precipitation_sum']

        
        for i in range(len(dailyStats)):
          self.weather[dailyStats[i]] = result['daily'][dailyStats[i]][0]

        weathercodes = {0 : "Clear Sky",
                        1 : "Mainly Clear",
                        2 : "Partly Cloudy",
                        3 : "Overcast",
                        45 : "Fog",
                        48 : "Depositing Rime Fog",
                        51 : "Light Drizzle",
                        53 : "Moderate Drizzle",
                        55 : "Dense Drizzle",
                        56 : "Freezing Light Drizzle",
                        57 : "Freezing Dense Drizzle",
                        61 : "Slight Rain",
                        63 : "Moderate Rain",
                        65 : "Heavy Rain",
                        66 : "Light Freezing Rain",
                        67 : "Heavy Freezing Rain",
                        71 : "Slight Snowfall",
                        73 : "Moderate Snowfall",
                        75 : "Heavy Snowfall",
                        77 : "Snow Grains",
                        80 : "Slight Rain Showers",
                        81 : "Moderate Rain Showers",
                        82 : "Violent Rain Showers",
                        85 : "Slight Snow Showers",
                        86 : "Heavy Snow Showers",
                        95: "Thunderstorm",
                        96: "Thunderstorm",
                        99: "Thunderstorm"
                       }
        self.weather['weathercode'] = weathercodes[self.weather['weathercode']]

        self.weather['sunrise'] = self.weather['sunrise'][len(self.weather['sunrise']) - 5:]
        self.weather['sunset'] = self.weather['sunset'][len(self.weather['sunset']) - 5:]
        self.weather['time'] = self.weather['time'].replace("T", " at ")

      except:
        print("404 ERROR NOT FOUND: Please check your internet connection and try again")
      
  
      

t = weatherAPI("https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,precipitation_sum&current_weather=true&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York")
t.getWeather()






WELCOMEFONT =("Verdana", 15)
DATAFONT = ("Verdana", 10)

class tkinterApp(Tk):
  
  # __init__ function for class tkinterApp
  def __init__(self, *args, **kwargs):
    
    # __init__ function for class Tk
    Tk.__init__(self, *args, **kwargs)
    # creating a container
    
    container = Frame(self)
    
    container.pack(side = "top", fill = "both", expand = True)

    container.grid_rowconfigure(0, weight = 1)
    container.grid_columnconfigure(0, weight = 1)

    # initializing frames to an empty array
    self.frames = {}

    # iterating through a tuple consisting
    # of the different page layouts
    for F in (StartPage, Data, Exit):

      frame = F(container, self)

      # initializing frame of that object from
      # startpage, data, Exit respectively with
      # for loop
      self.frames[F] = frame

      frame.grid(row = 0, column = 0, sticky ="nsew")

    self.show_frame(StartPage)

  # to display the current frame passed as
  # parameter
  def show_frame(self, cont):
    frame = self.frames[cont]
    frame.tkraise()

# first window frame startpage

class StartPage(Frame):
  def __init__(self, parent, controller):
    Frame.__init__(self, parent)
    
    # label of frame Layout 2
    label = ttk.Label(self, text ="Welcome To Weather View:\nA Comprehensive Easy To Use Weather Service ", font = WELCOMEFONT)
    
    # putting the grid in its place by using
    # grid
    label.grid(row = 0, column = 4, padx = 10, pady = 10)

    button1 = ttk.Button(self, text ="Data",
    command = lambda : controller.show_frame(Data))
  
    # putting the button in its place by
    # using grid
    button1.grid(row = 1, column = 1, padx = 10, pady = 10)

    ## button to show frame 2 with text layout2
    button2 = ttk.Button(self, text ="Exit",
    command = lambda : controller.show_frame(Exit))
  
    # putting the button in its place by
    # using grid
    button2.grid(row = 2, column = 1, padx = 10, pady = 10)

    


# second window frame data
class Data(Frame):
  
  def __init__(self, parent, controller):
    
    Frame.__init__(self, parent)
    temp_label = ttk.Label(self, text ="Current Temperature: " + str(t.weather["temperature"]) + "\u00B0 F", font = DATAFONT)
    temp_label.grid(row = 0, column = 4, padx = 10, pady = 5)

    max_temp_label = ttk.Label(self, text="Maximum Temperature: " + str(t.weather["temperature_2m_max"]) 
    +    "\u00B0 F", font = DATAFONT)
    max_temp_label.grid(row = 1, column = 4, padx = 10, pady = 0)

    min_temp_label = ttk.Label(self, text="Minimum Temperature: " + str(t.weather["temperature_2m_min"]) 
    +    "\u00B0 F", font = DATAFONT)
    min_temp_label.grid(row = 2, column = 4, padx = 10, pady = 0)

    sunrise_label = ttk.Label(self, text="Sunrise: " + str(t.weather["sunrise"]) 
    +    "", font = DATAFONT)
    sunrise_label.grid(row = 3, column = 4, padx = 10, pady = 10)
    sunset_label = ttk.Label(self, text="Sunset: " + str(t.weather["sunset"]) 
    +    "", font = DATAFONT)
    sunset_label.grid(row = 4, column = 4, padx = 10, pady = 0)

    precipitation_label = ttk.Label(self, text="Precipitation: " + str(t.weather["precipitation_sum"]) 
    +    " inches", font = DATAFONT)
    precipitation_label.grid(row = 0, column = 5, padx = 10, pady = 0)
    conditions_label = ttk.Label(self, text="Weather Conditions: " + str(t.weather["weathercode"]), font = DATAFONT)
    conditions_label.grid(row = 1, column = 5, padx = 10, pady = 0)
    windSpeed_label = ttk.Label(self, text="Windspeed: " + str(t.weather["windspeed"]) + " mph", font = DATAFONT)
    windSpeed_label.grid(row = 2, column = 5, padx = 10, pady = 0)
    
    windDirection_label = ttk.Label(self, text="Wind Direction: " + str(t.weather["winddirection"]) + "\u00B0", font = DATAFONT)
    windDirection_label.grid(row = 3, column = 5, padx = 10, pady = 0)

    time_label = ttk.Label(self, text="Most Recently Updated: " + str(t.weather["time"]), font = DATAFONT)
    time_label.grid(row = 4, column = 5, padx = 10, pady = 0)
    # button to show frame 2 with text
    # layout2
    button1 = ttk.Button(self, text ="Welcome Page",
              command = lambda : controller.show_frame(StartPage))
  
    # putting the button in its place
    # by using grid
    button1.grid(row = 1, column = 1, padx = 10, pady = 10)

    # button to show frame 2 with text
    # layout2
    button2 = ttk.Button(self, text ="Exit",
              command = lambda : controller.show_frame(Exit))
  
    # putting the button in its place by
    # using grid
    button2.grid(row = 2, column = 1, padx = 10, pady = 10)




# third window frame Exit
class Exit(Frame):
  def __init__(self, parent, controller):
    Frame.__init__(self, parent)
    label = ttk.Label(self, text ="Thank you for using WeatherView\nWeather Data From New York City, New York, USA\nCopyright 2022\n", font = WELCOMEFONT)
    label.grid(row = 0, column = 4, padx = 10, pady = 10)

    

# Driver Code
app = tkinterApp()
app.title('WeatherView')
app.mainloop()

