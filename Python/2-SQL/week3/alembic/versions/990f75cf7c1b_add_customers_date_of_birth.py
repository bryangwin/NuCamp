"""add customers date_of_birth

Revision ID: 990f75cf7c1b
Revises: 0b360682ad9d
Create Date: 2023-05-29 12:50:41.689218

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '990f75cf7c1b'
down_revision = '0b360682ad9d'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ADD COLUMN date_of_birth TIMESTAMP;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        DROP COLUMN date_of_birth;
        """
    )