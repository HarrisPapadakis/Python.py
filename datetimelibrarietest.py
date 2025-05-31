import datetime

# Δημιουργία συγκεκριμένης ημερομηνίας 
x = datetime.datetime(2023, 1, 1)

print(x.strftime("%A"))   # Full weekday name -> "Saturday"
print(x.strftime("%Y"))   # Year -> "2021"
print(x.strftime("%d/%m/%Y"))  # Formatted date -> "25/12/2021"
