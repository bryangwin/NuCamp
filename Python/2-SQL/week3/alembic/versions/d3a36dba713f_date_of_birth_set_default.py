"""date of birth set default

Revision ID: d3a36dba713f
Revises: 55e51541ebc5
Create Date: 2023-05-30 14:28:18.421042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3a36dba713f'
down_revision = '55e51541ebc5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
    """
    ALTER TABLE customers
    ALTER COLUMN date_of_birth SET DEFAULT now();
    """
    )


def downgrade() -> None:
    op.execute(
    """
    ALTER TABLE customers
    ALTER COLUMN date_of_birth DROP DEFAULT;
    """
    )
