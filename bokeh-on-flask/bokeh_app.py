# https://palletsprojects.com/p/flask/
from flask import Flask
from flask import render_template

import pandas as pd

from bokeh.plotting import figure
from bokeh.embed import components


app = Flask(__name__)
app.debug = False


@app.route("/")
def plot_flowers():
    flowers = pd.read_csv('http://danielykim.me/data/iris.csv')

    colormap = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
    colors = [colormap[x] for x in flowers['species']]

    p = figure(title = "Iris Morphology")
    p.xaxis.axis_label = 'Petal Length'
    p.yaxis.axis_label = 'Petal Width'

    p.circle(flowers["petal_length"], flowers["petal_width"],
             color=colors, fill_alpha=0.2, size=10)

    script, div = components(p)

    return render_template('iris.html', bokeh_script=script, bokeh_div=div)



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
