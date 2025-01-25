from livereload import Server, shell
import os, json

static_dir = './build/'

def reload_static():
    print("Files have changed. Reloading...")

server = Server()

build_config = json.load(open("../buildConfig.json"))

server.watch(os.path.join("../" + build_config["contentTemplatesPath"], '*'), shell('python3 build.py'))

server.watch(os.path.join(static_dir, '*.html'))
server.watch(os.path.join(static_dir, '*.css'))
server.watch(os.path.join(static_dir, '*.js'))
server.watch(os.path.join(static_dir, '*.json'))

server.serve(root=static_dir, host='0.0.0.0', port=5500)
