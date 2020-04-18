##Import docker client for python..

import docker
cli = docker.from_env()
#cli = docker.DockerClient(base_url='tcp://127.0.0.1:2375')

##Import Flask modules, to be able to show pretty things.. localhost:5000
from flask import Flask, render_template,request,redirect,url_for # For flask implementation

##Import BeatifulSoup module, with html.parsing capabilities..
import requests, re, os
from bs4 import BeautifulSoup

#Import database modules..
from pymongo import MongoClient # Database connector
from bson.objectid import ObjectId # For ObjectId to work
from bson.errors import InvalidId # For catching InvalidId exception for ObjectId


##
##Setup database information..
##
##

mongodb_host = os.environ.get('MONGO_HOST', 'localhost')
mongodb_port = int(os.environ.get('MONGO_PORT', '27017'))
client = MongoClient(mongodb_host, mongodb_port)    #Configure the connection to the database
db = client.camp2016    #Select the database
dockerdb = db.dockers #Select the collection


containers = cli.containers.list()


##
##Flask Main init section
##
app = Flask(__name__)
title = "Stocks shown by Flask, with python assistance"
heading = "Stock Getter"

def redirect_url():
    return request.args.get('next') or \
        request.referrer or \
        url_for('index')

##
##Static py app..

##
##FLASK section..Process stuff found above..
##

@app.route("/")
def mainindex ():
    return redirect("/docklist")

@app.route("/about")
def about():
    return render_template('credits.html',t=title,h=heading)

@app.route("/docklist")
def docklist():
    #Show Complete DB list.
    dblist = dockerdb.find()
    return render_template('index.html',stocks=dblist,t=title,h=heading)


@app.route("/update")
def update():
    #tmplist = client.containers.list(all=True)

    ##cont = tmplist[0]
    if len(containers)>0 :
#        print("We are moving on")
        for container in containers or []:
            #cont = containers[container]
            #name = cont.short_id
            name = ("{}".format(container.name))
            dockimage = ("{}".format(container.id))
            dockstatus = ("{}".format(container.status))
            dockerdb.insert({"symbol":name,"value":dockimage,"currency":dockstatus})

    return redirect("/docklist")

if __name__ == "__main__":
    #print("%02d:%02d:%02d" % (e // 3600, (e % 3600 // 60), (e % 60 // 1)))

    env = os.environ.get('APP_ENV', 'development')
    port = int(os.environ.get('PORT', 5100))
    debug = False if env == 'production' else True
    app.run(host='0.0.0.0', port=port, debug=debug)
    # Careful with the debug mode..
