"""Initial migration.

Revision ID: c84637f200d2
Revises: 
Create Date: 2024-06-30 21:25:22.803399

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c84637f200d2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('service')
    op.drop_table('invoice')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('invoice',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('project', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('client', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('address', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('invoice_date', sa.DATE(), nullable=False),
    sa.Column('due_date', sa.DATE(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('service',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('invoice_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('description', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('amount', mysql.FLOAT(), nullable=False),
    sa.ForeignKeyConstraint(['invoice_id'], ['invoice.id'], name='service_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
