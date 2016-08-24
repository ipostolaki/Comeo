from livereload.server import Server

server = Server()
server.watcher.watch('/comeo_project/static')
server.watcher.watch('/comeo_project/apps/base/templates')
server.watcher.watch('/comeo_project/apps/profiles/templates')
server.watcher.watch('/comeo_project/apps/registry/templates')
server.watcher.watch('/comeo_project/comeo_app/templates')
server.serve(host='0.0.0.0', port='35729', root='.')