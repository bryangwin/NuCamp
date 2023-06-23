"""date of birth set null

Revision ID: 55e51541ebc5
Revises: 990f75cf7c1b
Create Date: 2023-05-30 14:22:00.775423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55e51541ebc5'
down_revision = '990f75cf7c1b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
    """
    ALTER TABLE customers
    ALTER COLUMN date_of_birth SET NOT NULL;
    """
    )


def downgrade() -> None:
    op.execute(
    """ALTER TABLE customers
    ALTER COLUMN date_of_birth DROP NOT NULL;
    """
    )
