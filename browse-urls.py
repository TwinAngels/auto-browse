import webbrowser

with open("urls.txt") as f:
    for line in f:
        url = line.strip()
        webbrowser.open(url)
