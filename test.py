from flask import Flask

app = Flask('__name__')

@app.route('/')
def main():
    return '안녕하세요'

@app.route('/hello')
def betray():
    return '나가주세요'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=False)