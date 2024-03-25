"""Renaming students to scholars

Revision ID: f8b894de4877
Revises: 
Create Date: 2023-12-09 18:31:23.455293

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8b894de4877'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('students', 'scholars')


def downgrade():
    op.rename_table('scholars', 'students')
