"""
levenshtein_distance.py

This module provides functions to calculate the Levenshtein distance
between words and find the nearest word in a vocabulary.

Functions:
    levenshtein_distance(token1, token2): Calculate Levenshtein distance between two words.
    find_nearest_word(word, vocabs): Find the nearest word in a vocabulary.

This module is part of the Word Correction project using Streamlit.
"""


def compute_levenshtein_distance(token1, token2):
    """
    Calculate the Levenshtein distance between two strings.

    Args:
        token1 (str): The first string.
        token2 (str): The second string.

    Returns:
        int: The Levenshtein distance between the two strings.
    """
    # Initialize the matrix of distances
    m, n = len(token1), len(token2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Calculate the Levenshtein distance using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if token1[i - 1] == token2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]


def find_nearest_word(word, vocabs):
    """
    Find the nearest word in the vocabulary to the given word.

    Args:
    word (str): The input word to find a correction for.
    vocabs (list): A list of words in the vocabulary.

    Returns:
    str: The word from the vocabulary with the smallest Levenshtein distance to the input word.
    """
    # Calculate Levenshtein distance for each word in the vocabulary
    leven_distances = {vocab: compute_levenshtein_distance(
        word, vocab) for vocab in vocabs}
    # Return the word with the smallest distance
    return min(leven_distances, key=leven_distances.get)
