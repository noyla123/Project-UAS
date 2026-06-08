from flask import Flask, render_template, request
import hashlib

application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def index():

if request.method == 'POST':
    file = request.files['sertifikat']
    if file:
        isi_file = file.read()
        hash_sha256 = hashlib.sha256(isi_file).hexdigest()
        return render_template(
            'response.html',
            hash=hash_sha256
        )
return render_template('form.html')

if __name__ == '__main__':
application.run(debug=True)
