width = int(input("Quilt width: "))
height = int(input("Quilt height: "))
block_size = int(input("Block size: "))

blocks = (width // block_size) * (height // block_size)

print(f"You need {blocks} blocks.")