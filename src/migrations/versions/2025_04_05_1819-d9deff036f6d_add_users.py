"""add users

Revision ID: d9deff036f6d
Revises: 6dde99f90beb
Create Date: 2025-04-05 18:19:39.893617

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d9deff036f6d"
down_revision: Union[str, None] = "6dde99f90beb"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=100), nullable=False),
        sa.Column("hashed_password", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    


def downgrade() -> None:
    
    op.drop_table("users")
    
