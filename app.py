from flask import Flask, render_template, request
import subprocess
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')


@app.route('/validate', methods=['POST'])
def submit():
  file = request.form['file']
  result = subprocess.run(['rstcheck', '-'], input=file, text=True, capture_output=True)
  if result.stderr:
      print('Errors found:')
      print(result.stderr)
      response = result.stderr.split('<stdin>:')
  else:
      print('No errors found.')
      response = 'No errors found.'
  return render_template('response.html', response=response)

if __name__ == "__main__":
  app.run(debug=True)
