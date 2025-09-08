# Name Justin Jimenez
# CIS 3330
# CODE 1 - Weather Assistant
# Conversion formula: (Temperature in °F - 32) * .5556
# Note that the message to user should be the following
# "What is the temperature outside: "

def main():
    pass
temp_F = input("What is the temperature outside:")
temp_C = (int(temp_F)-32)*.5556

if temp_C > 20:
      print('\nWear a hat')

elif temp_C < 20 and temp_C > 10:
      print('\nWear a light jacket')

elif temp_C < 10:
      print('\nWear a heavy jacket')
if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
