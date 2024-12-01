from multiprocessing import Pool

# Define the original matrix
original_matrix = [
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4],
]

# Function to process each row
def process_row(row):
    return [cell * 2 for cell in row]

def main():
    # Create a pool of workers
    with Pool(processes=2) as pool:
        # Distribute work across rows
        new_matrix = pool.map(process_row, original_matrix)

    print("Original matrix:")
    for row in original_matrix:
        print(row)

    print("\nNew matrix:")
    for row in new_matrix:
        print(row)

if __name__ == '__main__':
    main()
