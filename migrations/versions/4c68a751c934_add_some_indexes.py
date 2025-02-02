"""Add some indexes

Revision ID: 4c68a751c934
Revises: 006f0933d8c1
Create Date: 2025-01-21 21:18:48.772096

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c68a751c934'
down_revision: Union[str, None] = '006f0933d8c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_phrases_level'), 'phrases', ['level'], unique=False)
    op.create_index(op.f('ix_phrases_topic_id'), 'phrases', ['topic_id'], unique=False)
    op.add_column('words', sa.Column('part_of_speech', sa.String(length=80), nullable=False))
    op.create_index(op.f('ix_words_level'), 'words', ['level'], unique=False)
    op.create_index(op.f('ix_words_part_of_speech'), 'words', ['part_of_speech'], unique=False)
    op.create_index(op.f('ix_words_topic_id'), 'words', ['topic_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_words_topic_id'), table_name='words')
    op.drop_index(op.f('ix_words_part_of_speech'), table_name='words')
    op.drop_index(op.f('ix_words_level'), table_name='words')
    op.drop_column('words', 'part_of_speech')
    op.drop_index(op.f('ix_phrases_topic_id'), table_name='phrases')
    op.drop_index(op.f('ix_phrases_level'), table_name='phrases')
    # ### end Alembic commands ###
