from flask import Flask, render_template, request
import sys
import io
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_belajar.html')

@app.route('/materi/sintaks')
def materi_sintaks():
    return render_template('materi_sintaks.html')

@app.route('/latihan/sintaks', methods=['GET', 'POST'])
def latihan_sintaks():
    output = ''
    error = ''
    code = ''
    if request.method == 'POST':
        code = request.form.get('code', '')
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        try:
            exec(code, {'__builtins__': {'print': print, 'range': range, 'len': len, 'str': str, 'int': int, 'float': float, 'bool': bool, 'list': list, 'dict': dict, 'tuple': tuple}})
            output = redirected_output.getvalue()
        except Exception as e:
            error = str(e)
        finally:
            sys.stdout = old_stdout
    return render_template('latihan_sintaks.html', output=output, error=error, code=code)

if __name__ == '__main__':
    app.run(debug=True)
