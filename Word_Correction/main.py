"""
main.py

This is the main module for the Word Correction application using Streamlit.
It provides the user interface and integrates the Levenshtein distance
functionality to suggest corrections for misspelled words.

Functions:
    load_vocab(file_path): Load vocabulary from a file.
    main(): Run the Streamlit application.

This module depends on the levenshtein_distance module for word comparison functionality.
"""
import streamlit as st
from levenshtein_distance import find_nearest_word, compute_levenshtein_distance


def load_vocab(file_path):
    """
    Load vocabulary from a file.

    Args:
    file_path (str): Path to the vocabulary file.

    Returns:
    list: Sorted list of unique words from the vocabulary file.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return sorted(set([line.strip().lower() for line in f]))


def main():
    """
    Main function to run the Streamlit app for word correction.
    """
    st.title("Word Correction using Levenshtein Distance")

    # Load vocabulary
    vocabs = load_vocab('vocab.txt')

    # User input
    word = st.text_input('Word:')

    if st.button("Compute"):
        # Find the nearest word
        correct_word = find_nearest_word(word, vocabs)

        # Display the result
        st.write('Correct word:', correct_word)

        # Create two columns for display
        col1, col2 = st.columns(2)

        # Display vocabulary
        col1.write('Vocabulary:')
        col1.write(vocabs)

        # Calculate and display distances
        col2.write('Distances:')
        distances = {vocab: compute_levenshtein_distance(
            word, vocab) for vocab in vocabs}
        col2.write(dict(sorted(distances.items(), key=lambda item: item[1])))


if __name__ == "__main__":
    main()
