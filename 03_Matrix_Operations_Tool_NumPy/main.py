import numpy as np

def inp_mat(prompt):
    """Input a matrix from the user."""
    print(prompt)
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        
        if rows <= 0 or cols <= 0:
            raise ValueError("Rows and columns must be positive integers.")
        
        print("Enter the matrix row by row (space-separated values):")
        matrix = []
        for i in range(rows):
            row = list(map(float, input(f"Row {i + 1}: ").strip().split()))
            if len(row) != cols:
                raise ValueError(f"Expected {cols} values but got {len(row)}.")
            matrix.append(row)
        return np.array(matrix)
    except ValueError as e:
        print(f"Input Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None

def display_mat(matrix, title="Matrix"):
    """Display a matrix with a title."""
    print(f"\n{title}:")
    print(matrix)
    print()

def add_matrices(mat1, mat2):
    """Add two matrices."""
    if mat1.shape != mat2.shape:
        raise ValueError(f"Matrices must have the same dimensions. Got {mat1.shape} and {mat2.shape}.")
    return mat1 + mat2

def subtract_matrices(mat1, mat2):
    """Subtract two matrices."""
    if mat1.shape != mat2.shape:
        raise ValueError(f"Matrices must have the same dimensions. Got {mat1.shape} and {mat2.shape}.")
    return mat1 - mat2

def multiply_matrices(mat1, mat2):
    """Multiply two matrices."""
    if mat1.shape[1] != mat2.shape[0]:
        raise ValueError(f"Number of columns of first matrix ({mat1.shape[1]}) must equal rows of second matrix ({mat2.shape[0]}).")
    return mat1 @ mat2

def transpose_matrix(mat):
    """Transpose a matrix."""
    return mat.T

def main():
    """Main function to run the matrix operations program."""
    print("=" * 50)
    print("MATRIX OPERATIONS CALCULATOR")
    print("=" * 50)
    
    while True:
        print("\nMatrix Operations Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose")
        print("5. Exit")
        
        choice = input("\nSelect an operation (1-5): ").strip()
        
        try:
            if choice == '1':
                print("\n--- MATRIX ADDITION ---")
                mat1 = inp_mat("Input first matrix:")
                if mat1 is None:
                    continue
                mat2 = inp_mat("\nInput second matrix:")
                if mat2 is None:
                    continue
                result = add_matrices(mat1, mat2)
                display_mat(mat1, "Matrix 1")
                display_mat(mat2, "Matrix 2")
                display_mat(result, "Result of Addition")
                
            elif choice == '2':
                print("\n--- MATRIX SUBTRACTION ---")
                mat1 = inp_mat("Input first matrix:")
                if mat1 is None:
                    continue
                mat2 = inp_mat("\nInput second matrix:")
                if mat2 is None:
                    continue
                result = subtract_matrices(mat1, mat2)
                display_mat(mat1, "Matrix 1")
                display_mat(mat2, "Matrix 2")
                display_mat(result, "Result of Subtraction")
                
            elif choice == '3':
                print("\n--- MATRIX MULTIPLICATION ---")
                mat1 = inp_mat("Input first matrix:")
                if mat1 is None:
                    continue
                mat2 = inp_mat("\nInput second matrix:")
                if mat2 is None:
                    continue
                result = multiply_matrices(mat1, mat2)
                display_mat(mat1, "Matrix 1")
                display_mat(mat2, "Matrix 2")
                display_mat(result, "Result of Multiplication")
                
            elif choice == '4':
                print("\n--- MATRIX TRANSPOSE ---")
                mat = inp_mat("Input matrix to transpose:")
                if mat is None:
                    continue
                result = transpose_matrix(mat)
                display_mat(mat, "Original Matrix")
                display_mat(result, "Transposed Matrix")
                
            elif choice == '5':
                print("\nThank you for using the Matrix Operations Calculator!")
                print("Exiting the program.")
                break
                
            else:
                print("\n⚠ Invalid choice. Please select a number between 1 and 5.")
                
        except ValueError as e:
            print(f"\n⚠ Operation Error: {e}")
        except Exception as e:
            print(f"\n⚠ Unexpected Error: {e}")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()