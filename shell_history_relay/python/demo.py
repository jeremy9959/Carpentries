import sys
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from pathlib import Path
import subprocess
import shlex
import requests
from requests.exceptions import ConnectionError

# home directory
home = str(Path.home())

# full path to file to watch for changes
watch_file_path = Path(sys.argv[1]).absolute()

# jekyll directory
jekyll_directory = Path(sys.argv[2])

# port on local machine where jekyll material is served
port = 4000

# index file in blog
index_html = Path("{}/{}".format(jekyll_directory, "index.html"))

# top matter added above the notebook
top_matter = """
<h1>Jupyter Notebook Relay</h1>
"""

# command to convert jupyter notebook to html
nbconvert_cmd = "jupyter nbconvert {} --to html --stdout".format(str(watch_file_path))

# command to start the jekyll blog
start_blog = "bundle exec --gemfile={} jekyll serve --source {} --destination {} --port {}".format(
    str(jekyll_directory / "Gemfile"),
    str(jekyll_directory),
    str(jekyll_directory / "_site"),
    port,
)


def startup():

    # put the topmatter (only) in the blog home
    with index_html.open("w") as f:
        f.write(top_matter)

    # start the ngrok relay
    try:
        _ = requests.get("http://localhost:4040/api")
    except ConnectionError:
        print(
            "ngrok is not available, please run\n~/ngrok start --none\nand then restart this script"
        )
        exit(1)

    ngrok_tunnel = {"name": "relay_tunnel", "addr": port, "proto": "http"}
    setup_tunnel = requests.post("http://localhost:4040/api/tunnels", json=ngrok_tunnel)
    tunnel = setup_tunnel.json()
    print("Relay will be available at:\n {}".format(tunnel["public_url"]))

    # start the jekyll blog
    _ = subprocess.Popen(shlex.split(start_blog), stdout=subprocess.DEVNULL)


def make_index_html():
    with index_html.open("w") as f:
        f.write(top_matter)

    with index_html.open("a") as f:
        nbconvert_process = subprocess.Popen(shlex.split(nbconvert_cmd), stdout=f)
    return nbconvert_process


def on_created(event):
    print("created!")
    make_index_html()
    return


def on_deleted(event):
    print("deleted!")
    with index_html.open("w") as f:
        f.write(top_matter)
    return


def on_modified(event):
    print("modified")
    make_index_html()
    return


def on_moved(event):
    print("moved!")
    on_deleted(event)
    return


if __name__ == "__main__":

    startup()
    pattern = [str(watch_file_path)]
    ignore_patterns = ""
    ignore_directories = True
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns=pattern)
    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified
    my_event_handler.on_moved = on_moved

    observer = Observer()
    observer.schedule(my_event_handler, str(watch_file_path.parents[0]), recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(20)
    except KeyboardInterrupt:
        observer.stop()
        try:
            tunnel_stop = requests.delete(
                "http://localhost:4040/api/tunnels/relay_tunnel (http)"
            )
            print("http: {}".format(tunnel_stop.status_code))
        except ConnectionError:
            print("Warning: Failed to close the http tunnel")

        try:
            tunnel_stop = requests.delete(
                "http://localhost:4040/api/tunnels/relay_tunnel"
            )
        except ConnectionError:
            print("Warning: Failed to close the https tunnel")

    observer.join()
