
#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

import pandas as pd 

# DATA MUST HAVE COLUMNS ID, problem, status


class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def open_data(self, path):
        return pd.read_csv(path)

    def query_user_problem(self, opendata, userid, problem_no):
        try:
            status = opendata.query(f"ID == '{userid}' & problem == {problem_no}").status[0]
        except KeyError as e:
            raise e        
        return status

    def update_user_problem(self, opendata, user_id, problem_no, value):
        opendata = opendata.set_index(['ID', 'problem'])\
                           .set_value((user_id, problem_no), 'status', value)\
                           .reset_index()
        return opendata


    def do_POST(self):
        """Respond to a POST request."""

        # Extract and print the contents of the POST
        length = int(self.headers['Content-Length'])
        post_data = parse_qs(self.rfile.read(length).decode('utf-8'))

        user    = str(post_data['kuid'][0])
        problem = int(post_data['problem'][0])
        status  = bool(post_data['status'][0])

        data = self.open_data('testdata.csv') # shouldn't be hardcoded

#         curr_status = self.query_user_problem(data, user, problem)
#  #       This needs some fixing
#         if curr_status == True:
#             pass 
#         else:
#           self.update_user_problem(data, user, problem, status)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes(f"Updated status on problem {problem} to {str(status)}", "utf8"))
        return 
    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return
    


def run():
  print('starting server...')

  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()



if __name__ == '__main__':
    run()