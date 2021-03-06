"""new fields in user model

Revision ID: 06b2c60f7d12
Revises: 2553b36ff963
Create Date: 2020-08-30 17:17:55.964668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06b2c60f7d12'
down_revision = '2553b36ff963'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('birthday', sa.Date(), nullable=True))
    op.add_column('user', sa.Column('entry_date', sa.Date(), nullable=True))
    op.add_column('user', sa.Column('last_login', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('title', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'title')
    op.drop_column('user', 'last_login')
    op.drop_column('user', 'entry_date')
    op.drop_column('user', 'birthday')
    # ### end Alembic commands ###
