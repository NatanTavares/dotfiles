#!/usr/bin/env python3

import subprocess
import time
import sys

GLYPHS = {
    "paused": "",
    "playing": "",
    "stopped": ""
}
SCROLL_TEXT_LENGTH = 40
REFRESH_INTERVAL = 0.3
PLAYERCTL = "/usr/bin/playerctl"

def get_status():
    try:
        result = subprocess.run([PLAYERCTL, "status"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0 or "No players found" in result.stderr.decode():
            return "stopped"
        return result.stdout.decode().strip().lower()
    except:
        return "stopped"

def get_title():
    try:
        result = subprocess.run([PLAYERCTL, "metadata", "title"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0 or "No players found" in result.stderr.decode():
            return None
        return result.stdout.decode().strip()
    except:
        return None

def get_player():
    try:
        result = subprocess.run([PLAYERCTL, "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        players = result.stdout.decode().strip().splitlines()
        return players[0] if players else None
    except:
        return "unknown"

def scroll_generator(text, width, delay_cycles=10):
    padded = text + "   "  # Add space for separation between loops
    full = padded + padded[:width]  # Ensure a smooth loop

    i = 0
    while True:
        if i == 0:
            # Pause at the "start" of scroll
            for _ in range(delay_cycles):
                yield text[:width].ljust(width)
        yield full[i:i+width]
        i = (i + 1) % len(padded)


if __name__ == "__main__":
    scroll = None
    last_title = ""

    while True:
        status = get_status()
        player = (get_player() or "unknown").split('.')[0]
        title = get_title()

        glyph = GLYPHS.get(status, "")

        if not title and player == "unknown" and status == "stopped":
            print("", flush=True)
            scroll = None
        elif not title or status == "stopped" :
            print(f"{glyph} {player} (stopped)", flush=True)
            scroll = None
        else:
            if title != last_title or scroll is None:
                scroll = scroll_generator(title, SCROLL_TEXT_LENGTH)
                last_title = title
            print(f"{glyph}  {player}: {next(scroll)}", flush=True)

        time.sleep(REFRESH_INTERVAL)

