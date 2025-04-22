def solve_8_queens_all_solutions():
    def under_attack(col, queens):
        return col in queens or any(abs(col - x) == len(queens) - i for i, x in enumerate(queens))
    
    def solve(n):
        solutions = [[]]
        for row in range(n):
            solutions = [solution + [col] 
                         for solution in solutions
                         for col in range(n)
                         if not under_attack(col, solution)]
        return solutions
    
    solutions = solve(8)
    for i, solution in enumerate(solutions[:1]):
        print(f"Solution {i+1}:")
        for col in solution:
            print(' '.join('Q' if i == col else '.' for i in range(8)))
        print()

solve_8_queens_all_solutions()