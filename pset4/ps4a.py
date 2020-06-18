# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) <= 1:
        #print([sequence])
        return [sequence]
    else:
        permutations = []
        first_char = sequence[0]
        next_chars = sequence[1:]
        permutations_of_subsequence = get_permutations(next_chars)
        for seq in permutations_of_subsequence:
            for index in range(len(seq) + 1):
                new_seq = seq[0:index] + first_char + seq[index:len(seq)+1]
                permutations.append(new_seq)
           
        #print(permutations)
        return permutations

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    print("Input:", 'red')
    print("Expected output:", ['red', 'erd', 'edr', 'rde', 'dre', 'der'])
    print('Actual output:', get_permutations('red'))
    
    print("Input:", 'try')
    print("Expected output:", ['try', 'rty', 'ryt', 'tyr', 'ytr', 'yrt'])
    print('Actual output:', get_permutations('try'))
    
    print("Input:", 'ply')
    print("Expected output:", ['ply', 'lpy', 'lyp', 'pyl', 'ypl', 'ylp'])
    print('Actual output:', get_permutations('ply'))
     
     
     
     
     
     