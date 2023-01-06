import base64
from io import BytesIO
from parse import *
from flask import Flask, render_template, request, redirect, url_for
from matplotlib.figure import Figure
import matplotlib
import matplotlib.pyplot as plt
from io import TextIOWrapper

matplotlib.use('Agg')

app = Flask(__name__)




@app.route("/")
def index():
    return render_template('index.html')

@app.route("/results", methods=['POST', 'GET'])
def results():
    if request.method == "POST":
        uploaded_file = request.files['file']
        select = request.form.get('data-type')
        if uploaded_file != '':
            uploaded_file =  TextIOWrapper(uploaded_file, encoding='utf-8')
    csv_list = dataPrep(uploaded_file)
    x, y, select = dataSel(csv_list, select)
    # Generate the figure **without using pyplot**.
    ax = plt
    ax.clf()
    ax.plot(x,y,linewidth=2.0)
    plt.gcf().autofmt_xdate()
    ax.matplotlib.pyplot.gcf().set_size_inches(18.5, 10.5)
    ax.xlabel('Time')
    ax.ylabel("Data for: {}".format(select))
    
    # Save it to a temporary buffer.
    buf = BytesIO()
    buf.flush()
    ax.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('results.html', plot_url=data)
    # f"<img src='data:image/png;base64,{data}'/>"

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=8000, debug=True)