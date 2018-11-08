import base64
import io

# https://palletsprojects.com/p/flask/
from flask import Flask
from flask import render_template

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')


app = Flask(__name__)
app.debug = False


@app.route("/")
def plot_flowers():
    flowers = pd.read_csv('http://danielykim.me/data/iris.csv')

    colormap = {
        'setosa'     : '#4C72B0', 
        'versicolor' : '#DD8452', 
        'virginica'  : '#55A868'
        }
    colors = [ colormap[x] for x in flowers['species'] ]

    x_label, y_label = 'petal_length', 'petal_width'

    plt.scatter(
        flowers[x_label], 
        flowers[y_label], 
        c = colors,
        alpha = 0.33
        )

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    b_io = io.BytesIO()

    plt.savefig(b_io)

    img_buf = b_io.getbuffer()

    img_b64 = base64.b64encode(img_buf)

    base64_image = img_b64.decode('utf-8')

    return render_template('temp.html', base64_image=base64_image)



if __name__ == "__main__":
    # https://gist.github.com/ianschenck/977379a91154fe264897
    reactor_args = {}
    
    def run_twisted_wsgi():
        from twisted.internet import reactor
        from twisted.web.server import Site
        from twisted.web.wsgi import WSGIResource

        resource = WSGIResource(reactor, reactor.getThreadPool(), app)
        site = Site(resource)
        reactor.listenTCP(5000, site)
        reactor.run(**reactor_args)
        
    if app.debug:
        # Disable twisted signal handlers in development only.
        reactor_args['installSignalHandlers'] = 0
        # Turn on auto reload.
        import werkzeug.serving
        run_twisted_wsgi = werkzeug.serving.run_with_reloader(run_twisted_wsgi)

    run_twisted_wsgi()
