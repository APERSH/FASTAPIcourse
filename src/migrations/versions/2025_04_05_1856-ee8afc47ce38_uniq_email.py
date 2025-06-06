"""uniq email

Revision ID: ee8afc47ce38
Revises: d9deff036f6d
Create Date: 2025-04-05 18:56:19.258381

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ee8afc47ce38"
down_revision: Union[str, None] = "d9deff036f6d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint(None, "users", ["email"])


def downgrade() -> None:
    op.drop_constraint(None, "users", type_="unique")

