from subprocess import check_output
from bottle import Bottle, request, route, run
from scheduler import Scheduler
import json
import http.client
# import servo

class HungryAgent:
    
    def __init__(self, agent_id, host, port):
        self._server_url = "http://hungrycats.herokuapp.com"
        self._heartbeat_interval = 120
        self._ip = self._get_ip()
        
        print('ip: ' + self._ip)
        
        self._id = agent_id #TODO persist this, maybe just in a text file
        
        self._host = host
        self._port = port
        
        self._app = Bottle()
        self._scheduler = Scheduler()
        self._setup_routes()
        
        self._create_checkin(self._server_url)
        
    def _setup_routes(self):
        self._app.route('/', method='GET', callback=self._hello)
        self._app.route('/schedules/<id:int>', method='POST', callback=self._create_schedule)
        self._app.route('/schedules/<id:int>', method='PATCH', callback=self._edit_schedule)
        self._app.route('/schedules/<id:int>', method='DELETE', callback=self._delete_schedule)
        self._app.route('/feed/', method='POST', callback=self._feed)
                
    def _hello(self):
        return "hungrycats agent online v0.0.1"
        
    def _create_schedule(self, id):
        
        return "schedule created"
        
    def _edit_schedule(self, id):
        
        return "schedule edited"
        
    def _delete_schedule(self, id):
        
        return "schedule deleted"
        
    def _feed(self):
    #    rotation_time = amount / 1000
    #     
    #     servo.rotate(rotation_time)
        return "cats fed"
    
    def start(self):
        self._app.run(host=self._host, port=self._port)

    def _create_checkin(self, server_url):
        ip = self._get_ip()
        
        #TODO use http.client to do this instead
        curl_command = '''curl -H "Content-Type: application/json" -X POST -d '{{"ip":"{0}"}}' {1}/api/checkin/{2}'''
        
        cmd = curl_command.format(ip, server_url, self._id)
        print('check-in command: ' + cmd)
        
        if self._scheduler.get_cron_job("checkin") is None:
            self._scheduler.create_cron_job("checkin", cmd, "*/5 * * * *")
        
        return 0
        
    def check_in(self):
        self.ip = self.get_ip()
        
        # then use the web
        return 0
        
    def _get_ip(self):
        ip_command = "dig +short myip.opendns.com @resolver1.opendns.com"
        ip = check_output(ip_command, shell=True).decode('utf-8').rstrip()
        return ip
    
