from locust import HttpLocust, TaskSet

def index(l):
    l.client.get("/")

def filme(l):
    l.client.get("/filme/comedy")

def top(l):
    l.client.get("/top_100")


class UserBehavior(TaskSet):
    tasks = {index:4, filme:2, top:1}


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait=5000
    max_wait=9000
    host='http://www.magic-preview.de'

    def __init__(self, *args, **kwargs):
        super(WebsiteUser, self).__init__(*args, **kwargs)
        self.client.auth = ("< you-know-who>", "<you-know-what>")