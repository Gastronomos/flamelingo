"""add other cruds

Revision ID: 006f0933d8c1
Revises: d175ce7d7857
Create Date: 2025-01-21 12:48:30.630627

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '006f0933d8c1'
down_revision: Union[str, None] = 'd175ce7d7857'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('topics',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=320), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_topics_name'), 'topics', ['name'], unique=False)
    op.create_table('levels',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('stages', sa.Integer(), nullable=False),
    sa.Column('topic_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['topic_id'], ['topics.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('phrases',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('ru', sa.Text(), nullable=False),
    sa.Column('en', sa.Text(), nullable=False),
    sa.Column('level', sa.Integer(), nullable=False),
    sa.Column('topic_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['topic_id'], ['topics.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_phrases_en'), 'phrases', ['en'], unique=False)
    op.create_index(op.f('ix_phrases_ru'), 'phrases', ['ru'], unique=False)
    op.create_table('rules',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=320), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('topic_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['topic_id'], ['topics.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_rules_name'), 'rules', ['name'], unique=False)
    op.create_table('words',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('ru', sa.String(length=80), nullable=False),
    sa.Column('en', sa.String(length=80), nullable=False),
    sa.Column('level', sa.Integer(), nullable=False),
    sa.Column('topic_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['topic_id'], ['topics.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_words_en'), 'words', ['en'], unique=False)
    op.create_index(op.f('ix_words_ru'), 'words', ['ru'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_words_ru'), table_name='words')
    op.drop_index(op.f('ix_words_en'), table_name='words')
    op.drop_table('words')
    op.drop_index(op.f('ix_rules_name'), table_name='rules')
    op.drop_table('rules')
    op.drop_index(op.f('ix_phrases_ru'), table_name='phrases')
    op.drop_index(op.f('ix_phrases_en'), table_name='phrases')
    op.drop_table('phrases')
    op.drop_table('levels')
    op.drop_index(op.f('ix_topics_name'), table_name='topics')
    op.drop_table('topics')
    # ### end Alembic commands ###
