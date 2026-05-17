#!/usr/bin/env python3
"""Aktualisiert den Klassenfortschritt-Zaehler in README.md."""

import re
import sys


def berechne_balken(n: int, ziel: int, breite: int = 30) -> tuple[str, int]:
    prozent = min(n * 100 // ziel, 100) if ziel > 0 else 0
    gefuellt = prozent * breite // 100
    balken = "█" * gefuellt + "░" * (breite - gefuellt)
    return balken, prozent


def main() -> None:
    if len(sys.argv) < 2:
        print("Verwendung: update_fortschritt.py <anzahl>")
        sys.exit(1)

    n = int(sys.argv[1])
    ziel = 100
    balken, prozent = berechne_balken(n, ziel)

    with open("README.md", encoding="utf-8") as f:
        text = f.read()

    text = re.sub(
        r"Aktuell:\s+\d+\s*/\s*\d+",
        f"Aktuell:       {n} / {ziel}",
        text,
    )
    text = re.sub(
        r"\[[░█]+\]\s+\d+\s*%",
        f"[{balken}]  {prozent} %",
        text,
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(text)

    print(f"OK Klassenfortschritt aktualisiert: {n} / {ziel} ({prozent} %)")


if __name__ == "__main__":
    main()
