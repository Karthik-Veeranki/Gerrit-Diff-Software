def html_call(sorted_result):
    
    # Generate the HTML content
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Result</title>

    <link rel="stylesheet" href="{{ url_for('static', filename='styles/styleResult.css') }}">
</head>


<body style="background-color: #E6E6FA">

    <header>
        <h1>Gerrit Difference Automation Software</h1>
    </header>

    <br>
    <h3>Commit difference result</h3>
        

<table>
    <tr>
        <th>Commit_id</th>
        <th>Date</th>
    </tr>
    """

    for key,values in sorted_result.items():
        html_content += f"""
        <tr>
            <td>{key}</td>
            <td>{values}</td>
        </tr>
        """

    # Close the table and the rest of the HTML tags
    html_content += """
</table>

<br><br>
    <a href="/download" class="button">Download Result as Text File</a>
    <br><br><br>
    <a href="/" class="button">Home</a>

    <footer>
        &copy; 2025. All rights reserved.
    </footer>
</body>
</html>
    """

    # Write the HTML content to a file
    with open("templates/result.html", "w") as file:
        file.write(html_content)

