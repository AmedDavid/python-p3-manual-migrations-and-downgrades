"""Rename email to email_address

Revision ID: a2bee8b566af
Revises: 791279dd0760
Create Date: 2025-05-18 16:13:25.539035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2bee8b566af'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None

def upgrade() -> None:
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.alter_column('email', new_column_name='email_address')

def downgrade() -> None:
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.alter_column('email_address', new_column_name='email')
