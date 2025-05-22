import time

subset_sum_iterations = 0

def subset_sum_zero(nums):
    global subset_sum_iterations
    subset_sum_iterations = 0
    solutions = []

    def backtrack(start, path):
        global subset_sum_iterations
        if path and sum(path) == 0:
            solutions.append(path[:])
        for i in range(start, len(nums)):
            subset_sum_iterations += 1
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    start_time = time.time()
    backtrack(0, [])
    end_time = time.time()
    return solutions, subset_sum_iterations, (end_time - start_time) * 1000  # ms

def main():
    print("Subconjunto Soma Zero")
    conjuntos = [
        [1, -1, 2, -2],
        [3, 1, -4, 2, -2],
        [3, 34, 4, 12, 5, 2],
        [-7, -3, -2, 5, 8],
        [10, -10, 20, -5, -15]
    ]

    for c in conjuntos:
        solutions, iterations, elapsed = subset_sum_zero(c)
        print(f"Conjunto: {c} -> Iterações: {iterations} | Tempo: {elapsed:.2f} ms")
        for s in solutions:
            print(f"  - {s}")
        if not solutions:
            print("  - Nenhum subconjunto com soma zero encontrado.")

if __name__ == "__main__":
    main()
