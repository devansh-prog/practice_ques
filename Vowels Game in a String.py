
def play_game(s):
    s = list(s)
    turn = 1
    vowels = set("aeiou")

    while len(s) != 0:
        n = int(input(f"User {turn}, enter n: "))

        if n > len(s):
            continue

        removed = s[:n]
        vowel_count = sum(1 for ch in removed if ch in vowels)

        if turn == 1 and vowel_count % 2 == 0:
            continue
        if turn == 2 and vowel_count % 2 != 0:
            continue

        s = s[n:]
        turn = 2 if turn == 1 else 1

        
        if len(s) == 0:
            return turn == 2

result = play_game("leetcoder")
print(result)


