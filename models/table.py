from config import db


class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_number = db.Column(db.Integer, nullable=False, unique=True)
    position = db.Column(db.String(2), nullable=False, unique=True)
    in_use = db.Column(db.Boolean, default=False)

    def __init__(self, table_num, position):
        self.table_number = table_num
        self.position = position


def check_table(table_id):
    table = Table.query.filter_by(id=table_id).first()
    return table.in_use


def change_table_status(table_id):
    table = Table.query.filter_by(id=table_id).first()
    if table.in_use:
        table.in_use = False
    else:
        table.in_use = True
    db.session.commit()
    return f'status: 200'

