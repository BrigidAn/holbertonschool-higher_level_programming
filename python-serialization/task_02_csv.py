#!/usr/bin/env python3
"""Convert CSV data to JSON"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Convert CSV file data to JSON format and save it to data.json.

    Args:
        filename (str): Name of the CSV file.

    Returns:
        bool: True if conversion succeeds, False otherwise.
    """
    try:
        with open(filename, "r", encoding="utf-8") as csv_file:
            data = list(csv.DictReader(csv_file))

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True

    except Exception:
        return False