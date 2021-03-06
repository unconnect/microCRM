"""users table

Revision ID: 2553b36ff963
Revises: aa41238b3fee
Create Date: 2020-08-30 09:57:26.150132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2553b36ff963'
down_revision = 'aa41238b3fee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'first_name', new_column_name='firstname')
    op.alter_column('user', 'last_name', new_column_name='lastname')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'firstname', new_column_name='first_name')
    op.alter_column('user', 'lastname', new_column_name='last_name')
    # ### end Alembic commands ###
