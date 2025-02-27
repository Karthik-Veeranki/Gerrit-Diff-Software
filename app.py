from flask import Flask, request, render_template, send_file
import logic
import html_table

app = Flask(__name__)


@app.route('/')
def index():
    logic.delete_file()
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def upload_files():
    # Step 1: take the files input
    file1 = request.files['file1']
    file2 = request.files['file2']

    content1 = file1.read().decode('utf-8')
    content2 = file2.read().decode('utf-8')

    # Step 2: Clean and fetch the data for commit_id
    commits1 = logic.compute(content1, True)
    commits2 = logic.compute(content2, False)

    # Step 3: feed the commits of both files as input 
    # to find the commits present only in file 1 and not in file 2
    sorted_result = logic.findDifference(commits1, commits2)

    # Step 4: Save the result in a file "output.txt"
    logic.saveContents(sorted_result, file1, file2)

    # Step 5: Create the result html page dynamically
    html_table.html_call(sorted_result)
    
    return render_template('result.html')


@app.route('/download')
def download_file():
    output_file_path = 'output.txt'
    return send_file(output_file_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
