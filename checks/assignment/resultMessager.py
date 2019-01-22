from requests import get, post
from time import sleep 


class ResultMessenger:

    def __init__(self, user, ip):
        self.user = user
        self.ip = ip

        self._check_connection()



    def _check_connection(self):
        """ Check that a connection can be made to the server
        """
        for _ in range(3):
            try:
                r =  get(f"http://{self.ip}/student/{self.user}")
                if r.ok:
                    break 
            except OSError as e:
                print(f"Connection error:\n{e}")
            sleep(2)
        else:
            raise ConnectionError(f"Can not connect to server with params ip: {self.ip}, user: {self.user}")



    def send_answer_to_db(self, problem, status):
        """ Submit an answer to the server
        """
        r = post(f"http://{self.ip}/student/{self.user}", data = {'ident': self.user, 'problem': problem, 'status': status})
        
        if not r.ok:
            raise ConnectionError(f"An error occured when pushing to the server. Is http://{self.ip}/student/{self.user} a valid URL?")


    def get_question_status(self, problem):
        r = self.get_full_status()
        return r[str(problem)]


    def get_full_status(self):  
        r = get(f"http://{self.ip}/student/{self.user}")

        if not r.ok:
            raise ValueError(f"Student ID {self.user} not in server database.")

        data = {int(k): bool(v) for k,v in dict( r.json() ).items()}
        return data