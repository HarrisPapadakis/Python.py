users = {
    "Uzumaki": {
        "first": "Naruto",
        "last": "Uzumaki",
        "Village": "Konoha",
    },
    "Uchiha": {
        "first": "Sasuke",
        "last": "Uchiha",
        "Village": "Konoha",
    },
    "Haruno": {
        "first": "Sakura",
        "last": "Haruno",
        "Village": "Konoha",
    },
    "Inuzuka": {
        "first": "Kiba",
        "last": "Inuzuka",
        "Village": "Konoha",
    },
    "Hyuuga": {
        "first": "Hinata",
        "last": "Hyuuga",
        "Village": "Konoha",
    },
    "Akimichi": {
        "first": "Choji",
        "last": "Akimichi",
        "Village": "Konoha",
    },
    "Nara": {
        "first": "Shikamaru",
        "last": "Nara",
        "Village": "Konoha",
    },
    "Yamanaka": {
        "first": "Ino",
        "last": "Yamanaka",
        "Village": "Konoha",
    },
    "Aburame": {
        "first": "Shino",
        "last": "Aburame",
        "Village": "Konoha",
    },
    "Rock": {
        "first": "Lee",
        "last": "Rock",
        "Village": "Konoha",
    },
    "Tenten": {
        "first": "Tenten",
        "last": "",
        "Village": "Konoha",
    },
    "Hyuga": {
        "first": "Neji",
        "last": "Hyuga",
        "Village": "Konoha",
    }
}

for username, user_info in users.items():
    print(f"\nUsername : {username}")
    full_name = f"{user_info['first']} {user_info['last']}".strip()
    location = user_info["Village"]

    print(f"\tFull name : {full_name.title()}")
    print(f"\tLocation : {location.title()}")
