from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///records.db'  
db = SQLAlchemy(app)

# schema model for record
class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    batch_id = db.Column(db.String(255))
    to_number = db.Column(db.String(255))
    from_number = db.Column(db.String(255))
    status = db.Column(db.Integer)
    status_text = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
with app.app_context():
    db.create_all()  

# api to search for specific record status
@app.route('/api/batch', methods=['GET'])
def get_batch_status():
    batch_id = request.args.get('batch_id')
    to = request.args.get('to')
    from_number = request.args.get('from')
    if from_number:
        record = Record.query.filter_by(batch_id=batch_id, to_number=to, from_number=from_number).first()
    else:
        record = Record.query.filter_by(batch_id=batch_id, to_number=to, from_number=from_number).first()

    if record:
        return jsonify({"batch_id":record.batch_id,"status": record.status,"to":record.to_number,"from":record.from_number,"status_text":record.status_text,"created_at":record.created_at})
    else:
        return jsonify({"status": "Not Found"}), 404

# api to store success sms
@app.route('/api/success', methods=['GET'])
def successful_batch():
    batch_id = request.args.get('batchId')
    to = request.args.get('to')
    from_number = request.args.get('from')
    status = 1
    status_text = request.args.get('statusText')
    print(batch_id,to,from_number,status_text)
    record = Record(batch_id=batch_id, to_number=to, from_number=from_number, status=status, status_text=status_text)
    db.session.add(record)
    db.session.commit()

    return jsonify({"status": status}), 200

# api to store failed sms
@app.route('/api/error', methods=['GET'])
def errored_batch():
    batch_id = request.args.get('batchId')
    to = request.args.get('to')
    from_number = request.args.get('from')
    status = 0
    status_text = request.args.get('statusText')

    record = Record(batch_id=batch_id, to_number=to, from_number=from_number, status=status, status_text=status_text)
    db.session.add(record)
    db.session.commit()
    return jsonify({"status": status}), 200

if __name__ == '__main__':
    app.run(debug=True)
