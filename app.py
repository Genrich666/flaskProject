from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Временное хранилище отзывов
reviews = []

# Главная страница
@app.route('/')
def home():
    return render_template('index.html')  # Рендерим index.html из папки templates

# Получение отзывов
@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    return jsonify(reviews)

# Добавление отзыва
@app.route('/api/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    name = data.get('name')
    review = data.get('review')

    if name and review:
        reviews.append({'name': name, 'review': review})
        return jsonify({'message': 'Review added successfully!'}), 201
    return jsonify({'message': 'Invalid data'}), 400

if __name__ == '__main__':
    app.run(debug=True)
