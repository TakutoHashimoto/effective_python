names = ["Cecilia", "Lise", "Marie"]
counts = [len(n) for n in names]

longest_name = None
max_count = 0

for i, name in enumerate(names):
    count = counts[i]

    if count > max_count:
        longest_name = names[i]
        max_count = count

print(longest_name)
