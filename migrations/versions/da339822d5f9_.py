"""empty message

Revision ID: da339822d5f9
Revises: d6d24625d2f2
Create Date: 2019-10-17 15:11:44.676409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da339822d5f9'
down_revision = 'd6d24625d2f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('email_list', sa.Column('country_code', sa.String(length=2), nullable=True))
    op.add_column('eth_contact', sa.Column('country_code', sa.String(length=2), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('eth_contact', 'country_code')
    op.drop_column('email_list', 'country_code')
    # ### end Alembic commands ###
