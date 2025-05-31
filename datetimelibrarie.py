import datetime

# Πέρνουμε την τρέχουσα ημερομηνία και ώρα
now = datetime.datetime.now()
print("Current date and time:", now)

# Μορφοποιηση ημερομηνίας σε string 
formatted = now.strftime("%d/%m/%Y %H:%M:%S")
print("Formatted date and time:", formatted)

# Δημιουργία κάποιας συγκεκριμένης ημερομηνίας
birthday = datetime.datetime(1990, 5, 15)
print("Birthday date:", birthday.strftime("%d/%m/%Y"))

# Υπολογισμός της διαφοράς μεταξύ  2 ημερομηνιών
difference = now - birthday
print("Age in days:", difference.days)

# Προσθεσε 7 μέρες απο σήμερα 
next_week = now + datetime.timedelta(days=7)
print("Date in 7 days:", next_week.strftime("%d/%m/%Y"))
