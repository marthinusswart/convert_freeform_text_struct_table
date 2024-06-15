import pandas as pd
from pandas import DataFrame
import sys
import argparse


def get_max_lengths(df: DataFrame) -> int:
    column_names = list(df.columns)
    max_lengths = []

    for i in column_names:
        max_lengths.append(0)

    for index, row in df.iterrows():
        col_num: int = 0
        for value in row:
            if max_lengths[col_num] < len(value):
                max_lengths[col_num] = len(value)
            col_num = col_num + 1

    return max_lengths


def fill_line(text_length, max_length, fill_char: str) -> str:
    result: str = ""
    for i in range(text_length, max_length):
        result = result + fill_char

    return result


def create_text_row(fields, max_lengths, fill_char: str) -> str:
    index = 0
    text_row: str = ""

    for text in fields:
        formatted_text = (
            text + fill_line(len(text), max_lengths[index], fill_char) + "|"
        )
        text_row = text_row + formatted_text
        index = index + 1

    return text_row


def print_as_text(df: DataFrame) -> None:
    column_names = list(df.columns)
    max_lengths = get_max_lengths(df)
    text_line = create_text_row(column_names, max_lengths, " ")
    print(text_line)
    empty_fields = ["" for _ in range(len(column_names))]
    text_line = create_text_row(empty_fields, max_lengths, "-")
    print(text_line)

    for index, row in df.iterrows():
        text_line = create_text_row(row, max_lengths, " ")
        print(text_line)

    text_line = create_text_row(empty_fields, max_lengths, "-")
    print(text_line)


def read_csv(csv_filename) -> DataFrame:
    # Read CSV file into a DataFrame
    df = pd.read_csv(csv_filename)
    return df


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert CSV to TXT")
    parser.add_argument("-csv_file", "--csv_filename")
    args = parser.parse_args()
    df = read_csv(args.csv_filename)
    print_as_text(df)


if __name__ == "__main__":
    main()
