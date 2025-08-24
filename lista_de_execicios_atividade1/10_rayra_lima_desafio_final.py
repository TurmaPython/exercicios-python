frutas = {
    "banana": 10,
    "maçã": 5,
    "laranja": 8
}

frutas["pera"] = 12

del frutas["banana"]

print("Itens em estoque:")
print(frutas.keys())

print("\nQuantidades em estoque:")
print(frutas.values())
