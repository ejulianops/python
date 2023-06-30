from datetime import datetime

day = int(input('Day of birth: '))
month = int(input('Month of birth: '))
year = int(input('Year of birth: '))

date_of_birth = datetime(year, month, day)
millenium = datetime(1999, 12, 31)
how_old_on_millenium = millenium - date_of_birth
stringify_and_split = f"{how_old_on_millenium}".split(" ")
days = int(stringify_and_split[0])

if days > 0:
    print(f"You were {days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")
