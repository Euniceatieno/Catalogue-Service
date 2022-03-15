"""baseline

Revision ID: 11044df43f82
Revises: 
Create Date: 2022-03-15 10:42:39.573020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11044df43f82'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
      op.create_table(
        'user_data',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String()),
        sa.Column('password', sa.String())
        )



def downgrade():
        op.drop_table('user_data')

