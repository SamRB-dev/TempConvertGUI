#!/usr/bin/python3
import PySimpleGUI as psg

# UI Components / CONSTANTS
THEME = 'DarkBlue2'
FONT_TEXT = ("Monospace 14")
FONT_SPIN = ("Monospace 10")
LAYOUT = [
	[
		psg.Text("Temperature in",font=FONT_TEXT),
		psg.Spin(['Kelvin','Fahrenheit','Celsius'],key='-intype-',font=FONT_SPIN)
	],
	[
		psg.Text("Convert to",font=FONT_TEXT),
		psg.Spin(['All','Kelvin','Fahrenheit','Celsius'],key='-convertto-',font=FONT_SPIN)
	],
	[psg.Text("Temperature",font=FONT_TEXT)],
	[psg.Input(key="-temp-",font=FONT_TEXT)],
	[psg.Button("Convert",key="-exec-")],
	[psg.Text("-----------------------------------Output--------------------------------------")],
	[psg.Text("",key='-output-',font=FONT_TEXT)]
]

# Converter Functions
def K2F(temp:float) -> float:
	return (temp - 273.15) * 1.8 + 32
def K2C(temp:float) -> float:
	return (temp - 273.15)
def C2K(temp:float) -> float:
	return (temp + 273.15)
def C2F(temp:float) -> float:
	return (temp * 1.8) + 32
def F2C(temp:float) -> float:
	return (temp - 32) * (5/9)
def F2K(temp:float) -> float:
	return (temp - 32) * (5/9) + 273.15

# Main Function
def main():
	try:
		psg.theme(THEME)
		root = psg.Window("TempConvert",LAYOUT,size=(350,295))
		while (1):
			event,values = root.read()
			if (event == psg.WIN_CLOSED):
				break
			elif (event == '-exec-'):
				intype = values['-intype-']
				converto = values['-convertto-']
				output = None
				temp = float(values['-temp-'])
				if (intype == 'Kelvin'):
					if (converto == 'Kelvin'):
						output = f"{temp}°K"
					elif (converto == 'Fahrenheit'):
						result = K2F(temp)
						output = f"{round(result,2)}°F"
					elif (converto == 'Celsius'):
						result = K2C(temp)
						output = f"{round(result,2)}°C"
					else:
						output = f"Kelvin: {temp}°K\nFahrenheit: {round(K2F(temp),2)}°F\nCelsius: {round(K2C(temp),2)}°C"
				elif (intype == 'Celsius'):
					if (converto == 'Kelvin'):
						result = C2K(temp)
						output = f"{round(result,2)}°K"
					elif (converto == 'Celsius'):
						output = f"{temp}°C"
					elif (converto == 'Fahrenheit'):
						result = C2F(temp)
						output = f"{round(result,2)}°F"
					else:
						output = f"Kelvin: {round(C2K(temp),2)}°K\nFahrenheit: {round(C2F(temp),2)}°F\nCelsius:{temp}°C"
				elif (intype == 'Fahrenheit'):
					if (converto == 'Kelvin'):
						result = F2K(temp)
						output = f"{round(result,2)}°K"
					elif (converto == 'Celsius'):
						result = F2C(temp)
						output = f"{round(result,2)}°C"
					elif (converto == 'Fahrenheit'):
						output = f"{temp}°F"
					else:
						output = f"Kelvin: {round(F2K(temp),2)}°K\nFahrenheit: {temp}°F\nCelsius: {round(F2C(temp),2)}°C"
				root['-output-'].update(output)			
		root.close()
		
	except Exception as error:
		print("Error")
		print(error)

if __name__ == '__main__':
	main()
