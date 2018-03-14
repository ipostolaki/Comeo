from livereload.server import Server

server = Server()
server.watcher.watch('/comeo_project/apps/base/templates')
server.watcher.watch('/comeo_project/apps/base/static')
server.watcher.watch('/comeo_project/apps/profiles/templates')
server.watcher.watch('/comeo_project/apps/profiles/static')
server.watcher.watch('/comeo_project/apps/registry/templates')
server.watcher.watch('/comeo_project/apps/crowdfunding/templates')
server.watcher.watch('/comeo_project/apps/comeo_debug/templates')
server.watcher.watch('/comeo_project/apps/events/templates')
server.serve(host='0.0.0.0', port='35729', root='.')
