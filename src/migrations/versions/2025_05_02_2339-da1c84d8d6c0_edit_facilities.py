"""edit facilities

Revision ID: da1c84d8d6c0
Revises: 38ed5f95fb15
Create Date: 2025-05-02 23:39:33.222181

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "da1c84d8d6c0"
down_revision: Union[str, None] = "38ed5f95fb15"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.add_column(
        "rooms_facilities", sa.Column("facilities_id", sa.Integer(), nullable=False)
    )
    op.drop_constraint(
        "rooms_facilities_facility_id_fkey", "rooms_facilities", type_="foreignkey"
    )
    op.create_foreign_key(
        None, "rooms_facilities", "facilities", ["facilities_id"], ["id"]
    )
    op.drop_column("rooms_facilities", "facility_id")



def downgrade() -> None:

    op.add_column(
        "rooms_facilities",
        sa.Column("facility_id", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.drop_constraint(None, "rooms_facilities", type_="foreignkey")
    op.create_foreign_key(
        "rooms_facilities_facility_id_fkey",
        "rooms_facilities",
        "facilities",
        ["facility_id"],
        ["id"],
    )
    op.drop_column("rooms_facilities", "facilities_id")

