import numpy as np

def format_numpy_array(arr, alignment='center'):
    # def format_string(arr):
        arr = str(arr)  
        if alignment == 'center':
            return arr.center(15, '_')
        elif alignment == 'left':
            return arr.ljust(15, '_')
        elif alignment == 'right':
            return arr.rjust(15, '_')
        else:
            raise ValueError("Alignment must be 'center', 'left', or 'right'.")
        
format_numpy_array_out = np.vectorize(format_numpy_array)

arr = np.array(['hello', 'numpy', 'world', 'python', 'ai'])

centered_arr = format_numpy_array_out(arr, alignment='center')
print("Centered:")
print(centered_arr)

left_arr = format_numpy_array_out(arr, alignment='left')
print("\nLeft-justified:")
print(left_arr)

right_arr = format_numpy_array_out(arr, alignment='right')
print("\nRight-justified:")
print(right_arr)