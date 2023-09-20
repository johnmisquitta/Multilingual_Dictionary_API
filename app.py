import random
from flask import Flask, jsonify
import pandas as pd
import csv

app = Flask(__name__)

dictionary = {}

def get_random_name():
    with open('word.csv', 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)

        for row in csv_reader:
            word = row[1]
            #print(word)

            birthday_dict = {word: data_row for (index, data_row) in enumerate(row)}
            #print(birthday_dict)

            if word not in dictionary:
                dictionary[word] = {
                    'english': {'word': row[1], 'meaning': row[2]},
                    'hindi': {'word': row[3], 'meaning': row[4]},
                    'marathi': {'word': row[5], 'meaning': row[6]}
                }

        random_key = random.choice(list(dictionary))
        return dictionary[random_key]

@app.route('/random-name', methods=['GET'])
def random_name():
    name = get_random_name()
    print(name)
    result = {'word': name}
    #return jsonify(result)
    return jsonify(name)


if __name__ == '__main__':
    app.run()
