import logging
import json
from flask import request, jsonify
from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/olympiad-of-babylon', methods=['POST'])
def Number(books,days):
    result = {'optimalNumberOfBooks':counter}
    books = request.get_json();
    books.sort()
    days.sort(reverse=True)
    bookI=0
    bookJ=len(books)-1
    counter=0
    for i in days:
        while i>books[bookJ]:
            i-=books[bookJ]
            bookJ-=1
            counter+=1
        while i>books[bookI]:
            i=books[bookI]
            bookI+=1
            counter+=1
    return json.dumps(result)