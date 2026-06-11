#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json_file():
    """Read products from JSON file"""
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv_file():
    """Read products from CSV file"""
    products = []

    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)

    return products


def read_sqlite_db():
    """Read products from SQLite database"""
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')

    products = [dict(row) for row in cursor.fetchall()]

    conn.close()
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    try:
        if source == 'json':
            products = read_json_file()

        elif source == 'csv':
            products = read_csv_file()

        elif source == 'sql':
            products = read_sqlite_db()

        else:
            return render_template(
                'product_display.html',
                error='Wrong source'
            )

    except Exception:
        return render_template(
            'product_display.html',
            error='Database error'
        )

    if product_id:
        product = next(
            (p for p in products if str(p['id']) == product_id),
            None
        )

        if product is None:
            return render_template(
                'product_display.html',
                error='Product not found'
            )

        products = [product]

    return render_template(
        'product_display.html',
        products=products
    )


if __name__ == '__main__':
    app.run(debug=True)