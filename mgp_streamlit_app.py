import streamlit as st
import pandas as pd

TRAIN = "https://www.dropbox.com/scl/fi/5zy935lqpaqr9lat76ung/music_genre_train.csv?rlkey=ccovu9ml8pfi9whk1ba26zdda&dl=1"
TEST = "https://www.dropbox.com/scl/fi/o6mvsowpp9r3k2lejuegt/music_genre_test.csv?rlkey=ac14ydue0rzlh880jwj3ebum4&dl=1"


def main():
    train = pd.read_csv(TRAIN)
    test = pd.read_csv(TEST)

    st.header('Music Genre Prediction')

    st.write('Training dataset')
    st.dataframe(train)
    st.write('Test dataset')
    st.dataframe(test)


if __name__ == "__main__":
    main()