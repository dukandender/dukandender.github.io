# Function to find the longest palindrome substring
def longest_pal_substr(s):
    n = len(s)
    if n == 0:
        return ""

    start = 0
    max_len = 1

    # Traverse the input string
    for i in range(n):
      
        # THIS RUNS TWO TIMES 
        # for both odd and even length
        # palindromes. j = 0 means odd
        # and j = 1 means even length
        for j in range(2):
            low = i
            hi = i + j

            # Expand substring while it is a palindrome
            # and in bounds
            while low >= 0 and hi < n and s[low] == s[hi]:
                curr_len = hi - low + 1
                if curr_len > max_len:
                    start = low
                    max_len = curr_len
                low -= 1
                hi += 1

    return s[start:start + max_len]

# Driver Code
if __name__ == "__main__":
    s = "deyerobbroyeed"
    print(longest_pal_substr(s))