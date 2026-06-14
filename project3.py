import numpy as np

def input_matrix(name):
    rows = int(input(f"\nEnter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))

    print(f"\nEnter elements for {name} row by row:")
    elements = []

    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        elements.append(row)

    return np.array(elements)


def show_matrix(name, matrix):
    print(f"\n{name}:")
    print(matrix)


def add_matrices(a, b):
    return a + b


def subtract_matrices(a, b):
    return a - b


def multiply_matrices(a, b):
    return np.dot(a, b)


def transpose_matrix(a):
    return np.transpose(a)


def determinant_matrix(a):
    return np.linalg.det(a)


def menu():
    print("\n====== MATRIX OPERATIONS TOOL ======")
    print("1. Add Matrices")
    print("2. Subtract Matrices")
    print("3. Multiply Matrices")
    print("4. Transpose Matrix")
    print("5. Determinant of Matrix")
    print("6. Exit")


def main():
    while True:
        menu()
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            result = add_matrices(A, B)
            show_matrix("Result (A + B)", result)

        elif choice == 2:
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            result = subtract_matrices(A, B)
            show_matrix("Result (A - B)", result)

        elif choice == 3:
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            result = multiply_matrices(A, B)
            show_matrix("Result (A x B)", result)

        elif choice == 4:
            A = input_matrix("Matrix")
            result = transpose_matrix(A)
            show_matrix("Transpose", result)

        elif choice == 5:
            A = input_matrix("Matrix")
            if A.shape[0] == A.shape[1]:
                result = determinant_matrix(A)
                print("\nDeterminant:", result)
            else:
                print("\nError: Determinant only works for square matrices.")

        elif choice == 6:
            print("\nExiting program... Goodbye!")
            break

        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()