from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

reviews = []

@app.route('/')
def home():
    return render_template('index.html')  # Путь к вашему HTML файлу

@app.route('/api/reviews', methods=['POST'])
def post_review():
    try:
        data = request.get_json()
        if 'name' not in data or 'review' not in data or 'ownership' not in data:
            return jsonify({'error': 'Недостаточно данных'}), 400
        reviews.append(data)
        return jsonify({"message": "Отзыв отправлен!"}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    return jsonify(reviews)

if __name__ == '__main__':
    app.run(debug=True)