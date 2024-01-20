from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)
water_folder = 'workers/water'

@app.route('/')
def show_all_diffs():
    diff_texts = []
    print('======= here =======')
    print(water_folder)
    for filename in os.listdir(water_folder):
        print(filename)
        if filename.endswith('_diff.txt'):
            diff_file_path = os.path.join(water_folder, filename)
            with open(diff_file_path, 'r') as file:
                diff_content = file.read()
                diff_texts.append(diff_content)
                print(diff_texts)
    return render_template('all_diffs.html', diff_texts=diff_texts)

@app.route('/workers/water/')
def water_files(filename):
    return send_from_directory(water_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)
