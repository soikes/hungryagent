from subprocess import check_output
from bottle import Bottle, request, route, run
from scheduler import Scheduler
import json
# import servo

class HungryAgent:

    def __init__(self, agent_id, host, port):
        self._heartbeat_interval = 120
        self._ip = self._get_ip()
        
        self._id = agent_id #TODO persist this, maybe just in a text file
        
        self._host = host
        self._port = port
        
        self._app = Bottle()
        self._scheduler = Scheduler()
        self._setup_routes()
        
        self._create_checkin()
        
    def _setup_routes(self):
        self._app.route('/', method='GET', callback=self._hello)
        self._app.route('/schedules/<id:int>', method='POST', callback=self._create_schedule)
        self._app.route('/schedules/<id:int>', method='PATCH', callback=self._edit_schedule)
        self._app.route('/schedules/<id:int>', method='DELETE', callback=self._delete_schedule)
        self._app.route('/feed/<amount:int>', method='POST', callback=self._feed)
                
    def _hello(self):
        return "Hungrycats agent online v0.0.1"
        
    def _create_schedule(self, id):
        
        return 0
        
    def _edit_schedule(self, id):
        
        return 0
        
    def _delete_schedule(self, id):
        
        return 0
        
    def _feed(self, amount):
        rotation_time = amount / 1000
    #     
    #     servo.rotate(rotation_time)
    #     return 0
    
    def start(self):
        self._app.run(host=self._host, port=self._port)

    def _create_checkin(self):
        ip_command   = "dig +short myip.opendns.com @resolver1.opendns.com"
        curl_command = '''ip=$({0}); curl -H "Content-Type: application/json" -X POST -d '{{"ip":"$ip"}}' http://hungrycats.herokuapp.com/api/checkin/{1}'''
        
        cmd = curl_command.format(ip_command, self._id)
        return 0
        
    def check_in(self):
        self.ip = self.get_ip()
        
        # then use the web
        return 0
        
    def _get_ip(self):
        ip_command = "dig +short myip.opendns.com @resolver1.opendns.com"
        ip = check_output(ip_command, shell=True).decode('utf-8').rstrip()
        return ip
    
