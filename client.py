import xmlrpclib

client = xmlrpclib.ServerProxy('http://127.0.0.1:9099')

print(client.is_cisco_visible())
