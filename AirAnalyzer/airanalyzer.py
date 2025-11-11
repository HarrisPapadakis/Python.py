# Εισαγωγή  απαραίτητων βιβλιοθήκων
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Ανάγνωση καιτων δεδομένων
# Διάβασμα αρχείου CSV που περιέχει τα δεδομένα ποιότητας αέρα
air_quality_data = pd.read_csv("air_quality_data.csv")

# Μετατροπή στήλης 'date' σε μορφή ημερομηνίας (datetime)
air_quality_data['date'] = pd.to_datetime(air_quality_data['date'])

# Εξάγωγή μήνα και έτους από τη στήλη ημερομηνίας για ανάλυση ανά περίοδο
air_quality_data['month'] = air_quality_data['date'].dt.month
air_quality_data['year'] = air_quality_data['date'].dt.year

# Υπολογισμός μέσου όρου συγκέντρωσης PM2.5 ανά πόλη
# Ομαδοποιηση δεδομένων ανά πόλη και ορισμός μέσης ορου τιμής 'pm25'
avg_pm25 = air_quality_data.groupby('city')['pm25'].mean().reset_index()

# Εκτύπωση μέσου όρου PM2.5 για κάθε πόλη
print("Average PM2.5 Concentration:")
print(avg_pm25)

# Συνάρτηση υπολογισμού AQI (Δείκτη Ποιότητας Αέρα) με βάση το PM2.5


def calculate_aqi_pm25(pm25):
    """
    Υπολογίζει τον Δείκτη Ποιότητας Αέρα (AQI) για μια τιμή PM2.5.
    Οι τιμές βασίζονται στα πρότυπα του US EPA (απλοποιημένη εκδοχή).
    """
    if pm25 <= 12:
        aqi = (50 - 0) / (12 - 0) * (pm25 - 0) + 0          # Καλής ποιότητας αέρα
    elif pm25 <= 35.4:
        aqi = (100 - 51) / (35.4 - 12.1) * (pm25 - 12.1) + 51  # Μέτριας ποιότητας
    else:
        aqi = 101  # Ανώτερη τιμή (χαμηλότερη ακρίβεια)
    return aqi


# Εφαρμογή της συνάρτησης AQI στα δεδομένα
# Δημιουργία νέα στήλης 'aqi_pm25' με τις υπολογισμένες τιμές AQI
air_quality_data['aqi_pm25'] = air_quality_data['pm25'].apply(calculate_aqi_pm25)

# Υπολογισμός μηνιαίου AQI ανά πόλη
# Ομαδοποιήση ανά πόλη, έτος και μήνα με  υπολογίσμο μέσου AQI
monthly_aqi = air_quality_data.groupby(['city', 'year', 'month'])['aqi_pm25'].mean().reset_index()

# Εκτυπώση μηνιαίου AQI
print("Monthly Air Quality Index (AQI):")
print(monthly_aqi)

# Υπολογισμός συσχέτισης μεταξύ ρύπων

# Δημιουργια πίνακα συσχέτισης (correlation matrix) για τους ρύπους
pollutant_corr = air_quality_data[['pm25', 'no2', 'so2', 'co', 'o3']].corr()

#  Οπτικοποίηση της συσχέτισης με Heatmap
# ------------------------------------------------------------

plt.figure(figsize=(10, 8))  # Μέγεθος του γραφήματος
sns.heatmap(pollutant_corr, annot=True, cmap="coolwarm", linewidths=0.5)

# Προσθέτουμε τίτλο στο διάγραμμα
plt.title("Correlation Between Pollutants")

# Εμφάνιση του heatmap
plt.show()
