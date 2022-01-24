# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

def music(artist, **titles):
    print(f"Artist: {artist}")
    for titles, name in titles.items():
        print(f"{titles}: {name}")


if __name__ == "__main__":
    music(
        "Prodigy",
        Track_1="Breathe",
        Track_2="Smack My Bitch Up",
        Track_3="Firestarter"
    )
