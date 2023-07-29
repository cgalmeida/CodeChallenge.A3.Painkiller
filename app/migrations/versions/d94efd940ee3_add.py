"""add

Revision ID: d94efd940ee3
Revises: 
Create Date: 2023-07-29 20:07:19.228048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd94efd940ee3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patients',
    sa.Column('patient_id', sa.UUID(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('condition', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('patient_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('patients')
    # ### end Alembic commands ###
