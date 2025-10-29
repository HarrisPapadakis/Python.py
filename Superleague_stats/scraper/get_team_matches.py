import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

def get_team_matches(team_id: int, team_name: str, year: int):
    """
    Παίρνει όλους τους αγώνες μιας ομάδας για τη σεζόν (π.χ. 2010/11)
    και αποθηκεύει τα δεδομένα σε CSV.
    """
    os.makedirs("data", exist_ok=True)

    # URL με τα παιχνίδια της ομάδας για τη σεζόν
    url = f"https://www.transfermarkt.gr/-/spielplan/verein/{team_id}/saison_id/{year}"
    headers = {"User-Agent": "Mozilla/5.0"}

    print(f"📥 Λήψη αγώνων για {team_name} ({year}/{year+1}) ...")
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print(f"❌ Σφάλμα ({r.status_code}) για {team_name}")
        return None

    soup = BeautifulSoup(r.text, "html.parser")

    matches = []
    rows = soup.select("table.items tr")

    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 5:
            continue

        # Ημερομηνία
        date = cols[1].text.strip()

        # Αντίπαλος
        opponent_tag = cols[3].find("a")
        opponent = opponent_tag.text.strip() if opponent_tag else ""

        # Σκορ και link αγώνα
        score_tag = cols[4].find("a")
        score = score_tag.text.strip() if score_tag else ""
        match_url = score_tag["href"] if score_tag and "href" in score_tag.attrs else ""

        # Εντός/εκτός (αν περιέχει "vs" είναι εντός)
        home_away = "H" if "vs" in cols[3].text else "A"

        if date and opponent and score:
            matches.append({
                "year": year,
                "team_id": team_id,
                "team_name": team_name,
                "date": date,
                "opponent": opponent,
                "home_away": home_away,
                "score": score,
                "match_url": match_url
            })

    if not matches:
        print(f"⚠️ Δεν βρέθηκαν αγώνες για {team_name}")
        return None

    df = pd.DataFrame(matches)

    # Δημιουργία ασφαλούς ονόματος αρχείου
    safe_team = team_name.lower().replace(" ", "_").replace("ά", "a").replace("ό", "o").replace("ί", "i")
    output_path = f"data/matches_{safe_team}_{year}.csv"

    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    print(f"✅ Αποθηκεύτηκαν {len(df)} αγώνες για {team_name} → {output_path}")
    return df


# ---------------------------------------------
# Εκτέλεση για δοκιμή (π.χ. Ολυμπιακός Πειραιώς)
# ---------------------------------------------
if __name__ == "__main__":
    df = get_team_matches(683, "Ολυμπιακός Πειραιώς", 2010)
    if df is not None:
        print(df.head())
    else:
        print("⚠️ Δεν υπάρχουν δεδομένα για αυτή τη σεζόν.")
    time.sleep(2)
