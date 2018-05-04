from serverHelper import *
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from time import time



L, R = 1, 100000

start_time = time()

queue = []
distributeQuery(queue, L, R, 4)
final_answer = 0
parts = len(queue)

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(("0.0.0.0", 8000),
                        requestHandler=RequestHandler, allow_none=True) as server:
    server.register_introspection_functions()

    # Register a function under a different name
    def query():
        if len(queue) == 0:
            return (-1, -1)
        res = queue[-1]
        queue.pop()
        return res
    server.register_function(query, 'query')
    # Register a function under a different name
    
    def compile_result(res):
        global final_answer
        global parts
        final_answer += res 
        parts -= 1

        if parts == 0:
            end_time = time()
            print("=====================================")
            time_taken = end_time-start_time
            print("Final Answer: " + str(final_answer))# + " in", end_time-start_time, "s ")
            print("The computation took %d seconds" %(time_taken))
            print("=====================================")
        return 1

    server.register_function(compile_result, 'compile_result')

    # Run the server's main loop
    server.serve_forever()