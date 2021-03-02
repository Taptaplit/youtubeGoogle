import sys
sys.path.append('C:\\Users\\home\\OneDrive\\Coding\\Python\\Automations\\youtubeGoogle')
import backend
sys.path.append('C:\\Users\\home\\OneDrive\\Coding\\Python\\Automations\\youtubeGoogle\\website')



bkd = backend.Backend('TimeOutWithTim')





def get_data(input=None):
    d = {}
    if input:
        video, total = bkd.query(input)
        index = -1
        for item in video:
            index = index + 1
            if index % 2:
                url = video[int(index - 1)]
                title = video[int(index)]
                d[str(title)] = {}
                d[str(title)]['title'] = str(title)
                d[str(title)]['url'] = str(url) 
    if d == {}:
        d['No Results'] = {}
        d['No Results']['title'] = '404 No Results Found!'
        d['No Results']['url'] = '/'
    return d



from flask import Flask, request, render_template, url_for, redirect 

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template('index.html')

@app.route('/post/handler/redirect/handler', methods=['GET', 'POST'])
def post():
    if request.method == "POST": 
        query = request.form.get("Sq") 
        return redirect(url_for('display', q=query))
    else:
        return redirect(url_for('main'))

@app.route('/query=?=<q>', methods=["GET", "POST"]) 
def display(q):
    vid = get_data(input=q)
    data = bkd.get_data()
    for video in data:
        text = data[str(video)]['text']
        if len(text) > 800:
            textA = text[:800] + '...'
            data[str(video)]['text'] = textA
    try:
        return render_template("query.html", videos=vid, data=data)
    except:
        data = {}
        data['No Results'] = {}
        data['No Results']['text'] = f'No Results found for {q}! Please try searching something else.'
        data['No Results']['url']  = 'https://192.168.15.111:3000/'

        d = {}
        d['No Results'] = {}
        d['No Results']['title'] = '404 No Results Found!'
        d['No Results']['url'] = 'https://192.168.15.111:3000/'
        
        return render_template("query.html", videos=d, data=data) 
    
    

