def is_cisco_visible():
    return False if exists("1447059938811.png", 2) is None else True  # this api is so bad

from SimpleXMLRPCServer import SimpleXMLRPCServer as Server

server = Server(('127.0.0.1', 9099))

server.register_function(is_cisco_visible)
server.serve_forever()