from livereload.server import Server

# Create a new application
server = Server()
server.watcher.watch('/Users/ipostolaki/envs/comeo_sync/comeo_project/comeo_app/templates')
server.watcher.watch('/Users/ipostolaki/envs/comeo_sync/comeo_project/comeo_app/static')
server.serve(host='127.0.0.1', port='35729', root='.')