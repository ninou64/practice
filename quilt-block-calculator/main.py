def calculate_blocks(width, height, block_size):
    return (width // block_size) * (height // block_size)


width = int(input("Enter the quilt width: "))
height = int(input("Enter the quilt height: "))
block_size = int(input("Enter the block size: "))

blocks = calculate_blocks(width, height, block_size)

print(f"You need {blocks} blocks.")