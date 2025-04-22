import numpy as np
import matplotlib.pyplot as plt # type: ignore

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Initial interval must have f(a) and f(b) with opposite signs")

    history = np.zeros((max_iter, 6))
    
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        error = abs(b - a) / 2
        
        history[i] = [i, a, b, c, fc, error]
        
        if abs(fc) < tol or error < tol:
            history = history[:i+1]  
            break
            
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    
    return c, history

def plot_results(f, history, root):
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    x = np.linspace(history[0,1]-1, history[0,2]+1, 400)
    plt.plot(x, f(x), label='f(x)')
    plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
    plt.axvline(root, color='red', linestyle=':', label=f'Root ≈ {root:.6f}')
    
    plt.axvline(history[0,1], color='green', linestyle='--', alpha=0.5, label='Initial interval')
    plt.axvline(history[0,2], color='green', linestyle='--', alpha=0.5)
    plt.axvline(history[-1,1], color='blue', linestyle='--', alpha=0.5, label='Final interval')
    plt.axvline(history[-1,2], color='blue', linestyle='--', alpha=0.5)
    
    plt.title('Function and Root Finding')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    
    # Plot convergence
    # plt.subplot(1, 2, 2)
    # iterations = history[:,0]
    # errors = history[:,5]
    # plt.semilogy(iterations, errors, 'bo-')
    # plt.title('Convergence History')
    # plt.xlabel('Iteration')
    # plt.ylabel('Error (log scale)')
    # plt.grid(True)
    
    plt.tight_layout()
    plt.show()

def verify_root(f, root, tol=1e-6):
    """Verify that the found root is correct"""
    residual = abs(f(root))
    if residual > tol:
        print(f"Warning: Residual {residual:.2e} is larger than tolerance {tol:.1e}")
    else:
        print(f"Verified: Residual {residual:.2e} is within tolerance {tol:.1e}")
    return residual <= tol

f = lambda x: x**3 - 2*x**2 - 5*x + 6 
a, b = -3.0, 4.0

root, history = bisection_method(f, a, b)

print(f"Found root: {root:.8f}")
print(f"Number of iterations: {len(history)}")
print(f"Final error: {history[-1,5]:.2e}")
print(f"f(root) = {f(root):.2e}")

verify_root(f, root)
plot_results(f, history, root)