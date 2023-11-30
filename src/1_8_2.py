names = ["Cecilia", "Lise", "Marie"]
counts = [len(n) for n in names]

longest_name = None
max_count = 0

for i in range(len(names)):
    count = counts[i]
    
    if count > max_count:
        logest_name = names[i]
        max_count = count

print(longest_name)  # => Cecilia
