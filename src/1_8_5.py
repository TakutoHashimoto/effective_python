names = ["Cecilia", "Lise", "Marie"]
counts = [len(n) for n in names]

longest_name = None
max_count = 0

names.append("Rosalind")

for name, count in zip(names, counts):
    print(name)
