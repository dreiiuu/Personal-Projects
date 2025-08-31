import time

def lyrics():
    lines = [
        ("Early this morning", 0.06, 3.0),
        ("When you knocked upon my door", 0.055, 5.0),
        ("Early this morning", 0.055, 3.0),
        ("When you knocked upon my door", 0.055, 4.7),
        ("And I say, Hello Satan, I", 0.065, 2.2),
        ("I believe it is time to go", 0.06, 5.2),
        ("Me and the devil", 0.09, 3.2),
        ("walkin' side by side", 0.08, 4.6),
        ("Me and the devil", 0.08, 3.5),
        ("walkin' side by side", 0.065, 2.0), 
    ]

    for line, char_delay, pause in lines:
        for char in line:
            print(char, end="", flush=True)
            time.sleep(char_delay)
        print()
        time.sleep(pause)

if __name__ == "__main__": 
    lyrics()   
