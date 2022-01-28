"""create user_info table

Revision ID: 4e3ba5f233a8
Revises: 
Create Date: 2022-01-25 15:25:57.547666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e3ba5f233a8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user_info',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(225), unique=True),
        sa.Column('password', sa.Unicode(255)),
    )


def downgrade():
    pass
