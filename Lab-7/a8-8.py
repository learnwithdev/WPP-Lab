def decode_message(encoded):
    num_to_letter = {str(i): chr(64 + i) for i in range(1, 27)}
    
    results = []
    
    def backtrack(remaining, current_decoding):
        if not remaining:
            results.append("".join(current_decoding))
            return
        
        # Try 1-digit group
        if remaining[0] != "0" and int(remaining[0]) <= 26:
            backtrack(remaining[1:], current_decoding + [num_to_letter[remaining[0]]])
        
        # Try 2-digit group if at least 2 digits remain
        if len(remaining) >= 2:
            two_digits = remaining[:2]
            if two_digits[0] != "0" and int(two_digits) <= 26:
                backtrack(remaining[2:], current_decoding + [num_to_letter[two_digits]])
    
    backtrack(encoded, [])
    return results

test_cases = ["11106", "12", "123"]
for test in test_cases:
    print(f"Encoded: {test}")
    decodings = decode_message(test)
    print(f"Possible decodings: {decodings}")
    print()