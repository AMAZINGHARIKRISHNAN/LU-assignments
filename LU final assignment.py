#Question 1
#Hey you are a chemist from India and you work with degree celsius in yourday to day life but due to a project your company had collaborated with a MNC company,
#where the chemists use degree frainite for their purposes, and to maintain collaboration consistent we want to have a easy degree conversion,
#Please develop a python based degree converter which takes °C value and give you output of °F 
temp = input("Input the  temperature(like 9c)")
degree = int(temp[:-1])
convention = temp[-1]

if convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  convention_t = "Fahrenheit"
print("The temperature in", convention_t, "is", result, "degrees.")
