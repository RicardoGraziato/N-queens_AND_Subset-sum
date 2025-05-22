import time

def is_safe(position, row, col):
    for r in range(row):
        c = position[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def solve_n_queens_util(n, row, position, solutions, counter):
    if row == n:
        solutions.append(position[:])
        return

    for col in range(n):
        counter[0] += 1
        if is_safe(position, row, col):
            position[row] = col
            solve_n_queens_util(n, row + 1, position, solutions, counter)

def print_board(solution):
    n = len(solution)
    board = []
    for row in range(n):
        line = ['.'] * n
        line[solution[row]] = 'Q'
        board.append(''.join(line))
    return "\n".join(board)

def solve_n_queens(n):
    start = time.time()
    solutions = []
    counter = [0]
    position = [-1] * n
    solve_n_queens_util(n, 0, position, solutions, counter)
    end = time.time()
    elapsed = (end - start) * 1000 
    return solutions, counter[0], elapsed

def main():
    print("N-Rainhas")
    for n in [4, 8, 7, 10]:
        solutions, iterations, elapsed = solve_n_queens(n)
        print(f"\nn = {n} -> Iterações: {iterations} | Tempo: {elapsed:.2f} ms")
        print(f"Total de soluções: {len(solutions)}")
        for i, sol in enumerate(solutions[:3], 1):  
            print(f"\nSolução {i}:\n{print_board(sol)}")

if __name__ == "__main__":
    main()
