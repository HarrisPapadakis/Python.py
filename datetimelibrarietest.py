import datetime

# Δημιουργία συγκεκριμένης ημερομηνίας 
x = datetime.datetime(2023, 1, 1)

print(x.strftime("%A"))   # Εκτυπώνουμε το όνομα της ημέρας
print(x.strftime("%Y"))   # Εκτυπώνουμε μόνο το έτος
print(x.strftime("%d/%m/%Y"))  # Εκτυπώνουμε την ημερομηνία σε μορφή: Ημέρα/Μήνας/Έτος
