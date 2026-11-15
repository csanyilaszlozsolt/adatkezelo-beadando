from data.basic.generator import generate_all

teams, drivers, results = generate_all(3)

print("Csapatok:")
for t in teams:
    print(t)

print("\nPilotak:")
for d in drivers:
    print(d)

print("\nEredmenyek (elso 5):")
for r in results[:5]:
    print(r)
