from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/user-datas', methods=['POST'])
def user_datas():
    form_datas = request.get_json()
    email_field = form_datas.get('email')
    name_field = form_datas.get('name')
    category_field = form_datas.get('category')
    first_book_field = form_datas.get('firstBook')
    second_book_field = form_datas.get('secondBook')
    print(f'DADOS ENVIADOS PELO FRONTEND\n\nEmail: {email_field}\nNome: {name_field}\nCategoria: {category_field}\nPrimeiro livro lido: {first_book_field}\nSegundo livro lido: {second_book_field}')
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(port=5000)
