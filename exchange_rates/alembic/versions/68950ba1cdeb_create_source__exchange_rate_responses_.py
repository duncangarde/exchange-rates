"""Create source__exchange_rate_responses table

Revision ID: 68950ba1cdeb
Revises:
Create Date: 2023-03-11 22:02:03.703247

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '68950ba1cdeb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'source__exchange_rate_responses',
        sa.Column('timestamp', sa.BigInteger, primary_key=True),
        sa.Column('base', sa.String(50), nullable=False),
        sa.Column('date', sa.Date, nullable=False),
        sa.Column('rates', sa.JSON, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('source__exchange_rate_responses')
