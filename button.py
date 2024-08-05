from flask import Flask, render_template_string

app = Flask(__name__)

# HTML 템플릿을 문자열로 직접 포함
html_template = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Button Press with Space Key</title>
    <script>
        document.addEventListener('DOMContentLoaded', (event) => {
            document.addEventListener('keydown', (e) => {
                if (e.code === 'Space') {
                    e.preventDefault(); // Space 키의 기본 동작 방지 (스크롤)
                    document.getElementById('myButton').click(); // 버튼 클릭
                }
            });
        });
    </script>
</head>
<body>
    <h1>Press Space to Click the Button</h1>
    <button id="myButton" onclick="alert('Button Clicked!')">Click Me</button>
</body>
</html>
'''

@app.route("/")
def index():
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=8080)