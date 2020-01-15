import sys
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from pathlib import Path
import subprocess, shlex

# home directory
home = str(Path.home())
# full path to file to watch for changes
watch_file_path = Path(sys.argv[1])
# location of jekyll blog
jekyll_directory = Path(sys.argv[2])
# name of ngrok endpoint
hostname = "server.jeremy9959.net"
# port on local machine where blog is
port = 4000

# index file in blog
index_html = Path("{}/{}".format(jekyll_directory, "index.html"))

# top matter above the history
top_matter = """
<h1>Jupyter Notebook Relay</h1>
"""
# jupyter notebook to html
nbconvert_cmd = "jupyter nbconvert {} --to html --stdout".format(str(watch_file_path))
# start the jekyll blog
start_blog = "bundle exec --gemfile={} jekyll serve --source {} --destination {} --port {}".format(
    str(jekyll_directory / "Gemfile"),
    str(jekyll_directory),
    str(jekyll_directory / "_site"),
    port,
)
# start the ngrok relay
start_ngrok = home + "/ngrok http --hostname {} {}".format(hostname, port)


def startup():
    # put the topmatter (only) in the blog home
    with index_html.open("w") as f:
        f.write(top_matter)

    # start the jekyll blog
    blog_process = subprocess.Popen(shlex.split(start_blog))

    # start the ngrok relay
    ngrok_relay = subprocess.Popen(shlex.split(start_ngrok))
    return blog_process, ngrok_relay


def make_index_html():
    with index_html.open("w") as f:
        f.write(top_matter)

    print(nbconvert_cmd)
    print("--------------->", shlex.split(nbconvert_cmd))
    with index_html.open("a") as f:
        nbconvert_process = subprocess.Popen(shlex.split(nbconvert_cmd), stdout=f)
    return nbconvert_process


def on_created(event):
    print("{} has been created!".format(event.src_path))
    make_index_html()
    return


def on_deleted(event):
    print("{} has been deleted!".format(event.src_path))
    return


def on_modified(event):
    print(f"hey buddy, {event.src_path} has been modified")
    make_index_html()
    return


def on_moved(event):
    print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")
    make_index_html()
    return


if __name__ == "__main__":
    print(shlex.split(nbconvert_cmd))
    print(shlex.split(start_ngrok))
    print(shlex.split(start_blog))

    startup()
    pattern = ["str(watch_file_path)"]
    ignore_patterns = ""
    ignore_directories = True
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler()
    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified
    my_event_handler.on_moved = on_moved

    observer = Observer()
    observer.schedule(my_event_handler, str(watch_file_path.parents[0]), recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
