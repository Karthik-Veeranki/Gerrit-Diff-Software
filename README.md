# Gerrit-Diff-Software

## Steps to run the software in your local system:
```
git clone https://github.com/Karthik-Veeranki/Gerrit-Diff-Software
```
After cloning the repository, run the following commands:

Ensure you have python version >= 3.0
```
python -m pip install -r requirements.txt
```

```
python app.py
```
Website will be live on:

```
http://127.0.0.1:5000/
```

Upload the git log files of both the branches in the respective file upload sections.

Click on ```Submit```.

The list of gerrit commit IDs which are present in file1 and not present in file2 will be displayed.
