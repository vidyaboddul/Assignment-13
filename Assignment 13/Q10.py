import numpy as np

try:
    # Ask the user for the number of random numbers
    n = int(input("Enter how many random numbers you want to generate: "))

    if n <= 0:
        print("Please enter a positive number.")
    else:
        # Generate random numbers between 10 and 100
        arr = np.random.randint(10, 101, n)

        # Print the generated array
        print("\nGenerated Array:")
        print(arr)

        # Display statistics
        print("\nStatistics:")
        print("Mean:", np.mean(arr))
        print("Median:", np.median(arr))
        print("Standard Deviation:", np.std(arr))
        print("Minimum:", np.min(arr))
        print("Maximum:", np.max(arr))

        # Try to reshape into a 2D array
        print("\nReshaping into a 2D Array:")

        reshaped = False

        # Find suitable rows and columns automatically
        for rows in range(int(np.sqrt(n)), 1, -1):
            if n % rows == 0:
                cols = n // rows
                matrix = arr.reshape(rows, cols)
                print(matrix)

                # Row-wise sum
                print("\nRow-wise Sum:")
                print(np.sum(matrix, axis=1))

                reshaped = True
                break

        if not reshaped:
            print("Cannot reshape into a proper 2D matrix because", n, "has no suitable factors.")

except ValueError:
    print("Invalid input! Please enter an integer.")

except Exception as e:
    print("An error occurred:", e)

finally:
    print("\nProgram finished.")