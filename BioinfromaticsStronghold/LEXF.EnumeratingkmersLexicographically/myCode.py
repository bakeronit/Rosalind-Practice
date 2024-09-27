from itertools import product

def generate_lexicographic_strings(alphabet, n):
    all_strings = [''.join(p) for p in product(alphabet, repeat=n)] 
    all_strings.sort()
    # Print each string in a new line
    for string in all_strings:
        print(string)

# Example usage
alphabet = ['A', 'C', 'G', 'T']
n = 2
generate_lexicographic_strings(alphabet, n)
