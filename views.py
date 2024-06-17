from flask import Blueprint, request, jsonify
from models import Log
from datetime import datetime

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/logs', methods=['GET'])
def get_logs():
    ip = request.args.get('ip')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    query = Log.query
    
    if ip:
        query = query.filter_by(ip=ip)
    if start_date and end_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        query = query.filter(Log.timestamp.between(start_date, end_date))
    
    logs = query.all()
    return jsonify([log.as_dict() for log in logs])

@main_blueprint.route('/logs/<int:log_id>', methods=['GET'])
def get_log(log_id):
    log = Log.query.get_or_404(log_id)
    return jsonify(log.as_dict())

class Log(db.Model):
    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
