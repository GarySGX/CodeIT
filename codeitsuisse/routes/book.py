import logging
import json
from flask import request, jsonify
from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/olympiad-of-babylon', methods=['POST'])
def olympiad():
    result = {'optimalNumberOfBooks':0}
    input1 = request.get_json()
    books = input1['books']
    days = input1['days']
    def Number(books,days):
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
        return counter
    result['optimalNumberOfBooks']= Number(books,days)
    return dumps(result)
