from config import *
from flask import Flask, render_template, redirect
from flask_caching import Cache
import os
import random

def page_not_found(e):
    return render_template('404.html'), 404

app = Flask(__name__)
app, cache = Flask(__name__), Cache(config={'CACHE_TYPE': 'SimpleCache'})
app.register_error_handler(404, page_not_found)
app.config["SECRET_KEY"] = clientsecret

@app.route("/")
def home():
    try:
        movielist, deadlist, movielist2, moviecount = os.listdir("J:/static/movies"), [], [], 0
        for item in movielist:
            if (str(item)[-4:] == ".mkv") or (str(item)[-4:] == ".m4v") or (str(item)[-4:] == ".avi"):
                do = "nothing"
            else:
                movielist2.append(item)
                moviecount += 1
        return render_template("Home.html", item2="nothing", movielist=sorted(movielist2), episodelist=sorted(deadlist), seasonlist=sorted(deadlist), badlist=sorted(deadlist), tvlist=sorted(deadlist), moviecount=moviecount, word2="Streamable", genre="Movies")
    except FileNotFoundError:
        return redirect("/404")

@app.route("/broken")
def brokenmovies():
    try:
        movielist, deadlist, badmovies, badcount = os.listdir("J:/static/movies"), [], [], 0
        for item in movielist:
            if (str(item)[-4:] == ".mkv") or (str(item)[-4:] == ".m4v") or (str(item)[-4:] == ".avi"):
                badmovies.append(item)
                badcount += 1
        return render_template("Home.html", item2="nothing", movielist=sorted(deadlist), episodelist=sorted(deadlist), seasonlist=sorted(deadlist), badlist=sorted(badmovies), tvlist=sorted(deadlist), moviecount=badcount, word2="UnStreamable", genre="Movies")
    except FileNotFoundError:
        return redirect("/404")

@app.route("/tv")
def tvshows():
    try:
        files, deadlist, tvlist, tvcount = os.listdir("J:/static/tv"), [], [], 0
        for item in files:
            tvlist.append(item)
            tvcount += 1
        return render_template("Home.html", item2="nothing", movielist=sorted(deadlist), episodelist=sorted(deadlist), seasonlist=sorted(deadlist), tvlist=sorted(tvlist), badlist=sorted(deadlist), moviecount=tvcount, word2="Streamable", genre="Tv Shows")
    except FileNotFoundError:
        return redirect("/404")

@app.route("/tv/<tvshow>")
def tvshowseason(tvshow):
    try:
        files, deadlist, seasonlist, seasoncount = os.listdir("J:/static/tv/"+tvshow), [], [], 0
        for item in files:
            seasonlist.append(item)
            seasoncount += 1
        return render_template("Home.html", item2=tvshow, movielist=sorted(deadlist), episodelist=sorted(deadlist), seasonlist=sorted(seasonlist), tvlist=sorted(deadlist), badlist=sorted(deadlist), moviecount=seasoncount, word2="Streamable", genre="Seasons")
    except FileNotFoundError:
        return redirect("/404")

@app.route("/tv/<tvshow>/<season>")
def tvshowepisode(tvshow, season):
    try:
        files, deadlist, episodelist, episodecount, badmovies, badcount = os.listdir("J:/static/tv/"+tvshow+"/"+season), [], [], 0, [], 0
        for item in files:
            if (str(item)[-4:] == ".mkv") or (str(item)[-4:] == ".m4v") or (str(item)[-4:] == ".avi"):
                do = "nothing"
            else:
                episodelist.append(item)
                episodecount += 1
        return render_template("Home.html", item2=tvshow, item3=season, movielist=sorted(deadlist), episodelist=sorted(episodelist), seasonlist=sorted(deadlist), tvlist=sorted(deadlist), badlist=sorted(deadlist), moviecount=episodecount, word2="Streamable", genre="Episodes")
    except FileNotFoundError:
        return redirect("/404")

@app.route("/watch/<moviename>")
def moviepage(moviename):
    try:
        return render_template("Movie-Page.html", movietitle=str(moviename).replace("-", " ").replace(".mp4", ""), vidsrc=str(str("https://flarecasino.ca/static/movies/"+moviename).replace(" ", "-")))
    except FileNotFoundError:
        return redirect("/404")

@app.route("/tv/watch/<show>/<season>/<episode>")
def showpage(show, season, episode):
    try:
        return render_template("Movie-Page.html", movietitle=str(episode).replace("-", " ").replace(".mp4", ""), vidsrc=str(str("https://flarecasino.ca/static/tv/"+show+"/"+season+"/"+episode).replace(" ", "-")))
    except FileNotFoundError:
        return redirect("/404")
    
@app.route("/",subdomain="dev")
def devhome():
    try:
        movielist, deadlist, movielist2, moviecount = os.listdir("J:/static/movies"), [], [], 0
        for item in movielist:
            if (str(item)[-4:] == ".mkv") or (str(item)[-4:] == ".m4v") or (str(item)[-4:] == ".avi"):
                do = "nothing"
            else:
                movielist2.append(item)
                moviecount += 1
        return render_template("devHome.html", item2="nothing", movielist=sorted(movielist2), episodelist=sorted(deadlist), seasonlist=sorted(deadlist), badlist=sorted(deadlist), tvlist=sorted(deadlist), moviecount=moviecount, word2="Streamable", genre="Movies")
    except FileNotFoundError:
        return redirect("/404")

@app.route("/broken",subdomain="dev")
def devbrokenmovies():
    try:
        movielist, deadlist, badmovies, badcount = os.listdir("J:/static/movies"), [], [], 0
        for item in movielist:
            if (str(item)[-4:] == ".mkv") or (str(item)[-4:] == ".m4v") or (str(item)[-4:] == ".avi"):
                badmovies.append(item)
                badcount += 1
        return render_template("devHome.html", item2="nothing", movielist=sorted(deadlist), episodelist=sorted(deadlist), seasonlist=sorted(deadlist), badlist=sorted(badmovies), tvlist=sorted(deadlist), moviecount=badcount, word2="UnStreamable", genre="Movies")
    except FileNotFoundError:
        return redirect("/404")

@app.route("/tv",subdomain="dev")
def devtvshows():
    try:
        files, deadlist, tvlist, tvcount = os.listdir("J:/static/tv"), [], [], 0
        for item in files:
            tvlist.append(item)
            tvcount += 1
        return render_template("devHome.html", item2="nothing", movielist=sorted(deadlist), episodelist=sorted(deadlist), seasonlist=sorted(deadlist), tvlist=sorted(tvlist), badlist=sorted(deadlist), moviecount=tvcount, word2="Streamable", genre="Tv Shows")
    except FileNotFoundError:
        return redirect("/404")

@app.route("/tv/<tvshow>",subdomain="dev")
def devtvshowseason(tvshow):
    try:
        files, deadlist, seasonlist, seasoncount = os.listdir("J:/static/tv/"+tvshow), [], [], 0
        for item in files:
            seasonlist.append(item)
            seasoncount += 1
        return render_template("devHome.html", item2=tvshow, movielist=sorted(deadlist), episodelist=sorted(deadlist), seasonlist=sorted(seasonlist), tvlist=sorted(deadlist), badlist=sorted(deadlist), moviecount=seasoncount, word2="Streamable", genre="Seasons")
    except FileNotFoundError:
        return redirect("/404")

@app.route("/tv/<tvshow>/<season>",subdomain="dev")
def devtvshowepisode(tvshow, season):
    try:
        files, deadlist, episodelist, episodecount, badmovies, badcount = os.listdir("J:/static/tv/"+tvshow+"/"+season), [], [], 0, [], 0
        for item in files:
            if (str(item)[-4:] == ".mkv") or (str(item)[-4:] == ".m4v") or (str(item)[-4:] == ".avi"):
                do = "nothing"
            else:
                episodelist.append(item)
                episodecount += 1
        return render_template("devHome.html", item2=tvshow, item3=season, movielist=sorted(deadlist), episodelist=sorted(episodelist), seasonlist=sorted(deadlist), tvlist=sorted(deadlist), badlist=sorted(deadlist), moviecount=episodecount, word2="Streamable", genre="Episodes")
    except FileNotFoundError:
        return redirect("/404")

@app.route("/watch/<moviename>",subdomain="dev")
def devmoviepage(moviename):
    try:
        return render_template("devMovie-Page.html", movietitle=str(moviename).replace("-", " "), link=str(str(moviename).replace(" ", "-")))
    except FileNotFoundError:
        return redirect("/404")

if __name__ == '__main__':
    #from waitress import serve
    #import logging
    #logger = logging.getLogger('waitress')
    #logger.setLevel(logging.DEBUG)
    #serve(app, host="0.0.0.0", port=80, threads=8)
    app.config['SERVER_NAME'] = servername
    cache.init_app(app)
    app.run(debug=True, host="0.0.0.0", port=80)
