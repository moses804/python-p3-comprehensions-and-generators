# lib/list_comprehension.py

def return_evens(seq):
    """
    Returns a list of even numbers from the input sequence using a list comprehension.
    """
    return [num for num in seq if num % 2 == 0]


def make_exclamation(sentences):
    """
    Returns a list of sentences with an exclamation mark added at the end of each sentence using a list comprehension.
    """
    return [sentence + "!" for sentence in sentences]
