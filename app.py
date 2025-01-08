from flask import Flask, request, jsonify

app = Flask(__name__)

reviews = []  # Список для хранения отзывов (в реальной ситуации здесь будет база данных)

@app.route('/api/reviews', methods=['POST'])
def post_review():
    data = request.get_json()
    reviews.append(data)  # Сохраняем отзыв
    return jsonify({"message": "Отзыв отправлен!"}), 201

@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    return jsonify(reviews)

if __name__ == '__main__':
    app.run(debug=True)
