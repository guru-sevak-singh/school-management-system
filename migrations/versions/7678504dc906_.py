"""empty message

Revision ID: 7678504dc906
Revises: d99e7d868e01
Create Date: 2024-05-14 16:16:25.754622

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7678504dc906'
down_revision = 'd99e7d868e01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('staff_attendence', schema=None) as batch_op:
        batch_op.drop_column('attendence_comment')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('staff_attendence', schema=None) as batch_op:
        batch_op.add_column(sa.Column('attendence_comment', sa.TEXT(), nullable=True))

    # ### end Alembic commands ###
