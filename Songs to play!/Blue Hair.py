import time

def lyrics():
    lines = [
        ("Last I heard she was living", 0.08, 2.6),
        ("With a boy who acts his age", 0.07, 0.8),
        ("bum bum bum", 0.09, 2.4),
        ("bum bum bum", 0.09, 1.5),
        ("And I guess I'll just miss her", 0.09, 1.9),
        ("Even though she isn't even really gone", 0.08, 0.9),
        ("But things are just different", 0.08, 1.3),
        ("Ever since she cut her blue hair off", 0.08, 0.4),      
        ("bum bum bum", 0.09, 0.2),
        ("bum bum bum", 0.09, 0.6),
        ("bum bum bum", 0.09, 0.6),
        ("bum bum bum", 0.09, 0.9),
    ]

    for line, char_delay, pause in lines:
        for char in line:
            print(char, end="", flush=True)
            time.sleep( char_delay)
        print()
        time.sleep(pause)

if __name__ == "__main__":
    lyrics()
