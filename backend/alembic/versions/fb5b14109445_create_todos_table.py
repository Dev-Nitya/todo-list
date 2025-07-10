"""Create todos table

Revision ID: fb5b14109445
Revises: 
Create Date: 2025-07-10 14:47:04.874465

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb5b14109445'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(""" 
     CREATE TABLE todos(
               id bigserial PRIMARY KEY,
               name TEXT,
               completed BOOLEAN NOT NULL DEFAULT FALSE
               )
""")


def downgrade() -> None:
    op.execute(""" 
     DROP TABLE todos
""")
