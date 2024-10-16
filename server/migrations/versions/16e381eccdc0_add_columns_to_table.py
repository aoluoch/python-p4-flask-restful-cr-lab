"""add columns to table

Revision ID: 16e381eccdc0
Revises: 67f5d67aea55
Create Date: 2024-10-11 15:13:25.208055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16e381eccdc0'
down_revision = '67f5d67aea55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plants')
    # ### end Alembic commands ###
