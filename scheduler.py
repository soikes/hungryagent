from crontab import CronTab

class Scheduler:
    
    def __init__(self):
        self._cron = CronTab(user=True)
    
    def create_daily_schedule(self, id, cmd, time):
        self._generate_daily_cron_job(id, cmd, time)
        
    def edit_daily_schedule(self, id, cmd, time):
        job = self._get_cron_job(id)
        if cmd is not None:
            job.set_command(cmd)
        if time is not None:
            job.hour.on(time)
            
        job.enable()
        
        self._cron.write()
        
    def delete_schedule(self, id):
        job = self._get_cron_job(id)
        
        self._cron.remove(job)
        
        self._cron.write()
            
    def _generate_daily_cron_job(self, id, cmd, time):
        job = self._cron.new(command=cmd, comment=id)
        job.hour.on(time)
        job.day.every(1)
        
        job.enable()
        
        self._cron.write()
    
    def _get_cron_job(id):
        job = self._cron.find_comment(id)
        
        return job
