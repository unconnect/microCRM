from app import crm, db
from app.models import User, Customer


if __name__ == '__main__':
    crm.run(debug=True, use_reloader=True)

@crm.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Customer': Customer}