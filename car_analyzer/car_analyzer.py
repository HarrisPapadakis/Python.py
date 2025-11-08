#Εισάγουμε τις βιβλιοθήκες Pandas, NumPy, και Matplotlib για
#διαχείριση δεδομένων, αριθμητικές πράξεις και οπτικοποιήσεις

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Φορτώνουμε το dataset από ένα URL. Καθώς τα δεδομένα είναι χωρισμένα με κενά
#χρησιμοποιούμε το `delim_whitespace=True` και ορίζουμε τα ονόματα των στηλών

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
column_names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
df = pd.read_csv(url, names=column_names, delim_whitespace=True)

# Αντικαθιστούμε τα ερωτηματικά '?' στη στήλη 'horsepower' 
# με NaN (Not a Number), μετατρέπουμε τη στήλη σε αριθμητικό τύπο (float) 
# και αφαιρούμε τις γραμμές με ελλιπείς τιμές
df['horsepower'] = df['horsepower'].replace('?', np.nan)
df['horsepower'] = df['horsepower'].astype(float)
df.dropna(inplace=True)

# Εμφανίζουμε βασικές στατιστικές λεπτομέρειες όπως μέσο όρο, τυπική απόκλιση, κλπ.,
# για τις αριθμητικές στήλες του DataFrame
print(df.describe())

# Υπολογίζουμε και εμφανίζουμε τον πίνακα συσχέτισης για να εξετάσουμε τις σχέσεις 
# μεταξύ των αριθμητικών μεταβλητών. Εξαιρούμε τις μη-αριθμητικές στήλες
numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
print(df[numeric_columns].corr())

# Δημιουργούμε ένα διάγραμμα διασποράς για να οπτικοποιήσουμε τη σχέση μεταξύ του
# βάρους ('weight') και της κατανάλωσης ('mpg') των αυτοκινήτων
plt.scatter(df['weight'], df['mpg'])
plt.xlabel('Weight')
plt.ylabel('Miles Per Gallon')
plt.title('Weight vs. MPG')

plt.show()
