import re
from datetime import datetime
from models import db, Log
from config import Config

log_pattern = re.compile(r'(\S+) (\S+) (\S+) \[(.*?)\] "(.*?)" (\d{3}) (\d+)')

def parse_log_line(line):
    match = log_pattern.match(line)
    if match:
        return match.groups()
    return None

def parse_logs():
    with open(Config.LOG_DIR + Config.LOG_EXT, 'r') as f:
        for line in f:
            parsed_log = parse_log_line(line)
            if parsed_log:
                timestamp = datetime.strptime(parsed_log[3], '%d/%b/%Y:%H:%M:%S %z')
                log_entry = Log(ip=parsed_log[0], identity=parsed_log[1], user=parsed_log[2], timestamp=timestamp,
                                request=parsed_log[4], status=int(parsed_log[5]), size=int(parsed_log[6]))
                db.session.add(log_entry)
        db.session.commit()
