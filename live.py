from livereload.server import Server

# Create a new application
server = Server()
server.watcher.watch('/comeo_project/comeo_app/templates')
server.watcher.watch('/comeo_project/comeo_app/static')
server.watcher.watch('/comeo_project/registry/templates')
server.serve(host='0.0.0.0', port='35729', root='.')