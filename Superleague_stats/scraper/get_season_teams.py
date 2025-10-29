import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_season_teams(year: int):
    """
    Συλλέγει όλες τις ομάδες της Super League Ελλάδας για μια συγκεκριμένη σεζόν (π.χ. 2010)
    και τις αποθηκεύει σε αρχείο CSV.
    """
    
    base_url = f"https://www.transfermarkt.gr/super-league-1/startseite/wettbewerb/GR1/saison_id/{year}"
    headers = {"User-Agent": "Mozilla/5.0"}

    print(f"🔍 Ανάκτηση δεδομένων για τη σεζόν {year}/{year+1}...")
    r = requests.get(base_url, headers=headers)
    if r.status_code != 200:
        print(f"❌ Σφάλμα κατά τη φόρτωση ({r.status_code})")
        return None

    soup = BeautifulSoup(r.text, "html.parser")

    teams_data = []
    teams = soup.select("table.items td.hauptlink a")
    for team in teams:
        name = team.text.strip()
        href = team["href"]
        # Παράδειγμα href: /olympiakos-pireus/startseite/verein/683
        if "/verein/" in href:
            team_id = href.split("/verein/")[-1].split("/")[0]
            teams_data.append({"year": year, "team_name": name, "team_id": team_id})

    if not teams_data:
        print("⚠️ Δεν βρέθηκαν ομάδες — άλλαξε πιθανόν η δομή του site.")
        return None

    df = pd.DataFrame(teams_data)
    output_file = f"data/teams_{year}.csv"
    df.to_csv(output_file, index=False, encoding="utf-8-sig")

    print(f"✅ Αποθηκεύτηκαν {len(df)} ομάδες στο αρχείο {output_file}")
    return df


# Εκτέλεση μόνο αν τρέχει το αρχείο απευθείας
if __name__ == "__main__":
    df_2010 = get_season_teams(2010)
    print(df_2010)
    time.sleep(2)
