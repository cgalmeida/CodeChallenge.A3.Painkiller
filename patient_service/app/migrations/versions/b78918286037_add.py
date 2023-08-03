"""add

Revision ID: b78918286037
Revises: d94efd940ee3
Create Date: 2023-08-01 17:31:29.794413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b78918286037'
down_revision = 'd94efd940ee3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('measurements',
    sa.Column('measurement_id', sa.UUID(), nullable=False),
    sa.Column('temperature', sa.String(), nullable=False),
    sa.Column('blood_pressure_sys', sa.Integer(), nullable=True),
    sa.Column('blood_pressure_dias', sa.Integer(), nullable=True),
    sa.Column('BMI', sa.Float(), nullable=True),
    sa.Column('body_weight', sa.Float(), nullable=False),
    sa.Column('stroke', sa.Boolean(), nullable=True),
    sa.Column('diabetes', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('patient_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.patient_id'], ),
    sa.PrimaryKeyConstraint('measurement_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('measurements')
    # ### end Alembic commands ###
