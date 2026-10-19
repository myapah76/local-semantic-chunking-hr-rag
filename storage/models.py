import uuid
import datetime
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import declarative_base, relationship

try:
    from pgvector.sqlalchemy import Vector
    HAS_PGVECTOR = True
except ImportError:
    HAS_PGVECTOR = False
    # Fallback to Text or custom type if pgvector package isn't installed locally
    from sqlalchemy.types import UserDefinedType
    class Vector(UserDefinedType):
        def __init__(self, dim):
            self.dim = dim
        def get_col_spec(self, **kw):
            return f"vector({self.dim})"

Base = declarative_base()

class DocumentChunk(Base):
    """
    Table storing raw text chunks and metadata.
    """
    __tablename__ = "document_chunks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    document_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    chunk_index = Column(Integer, nullable=False)
    content = Column(Text, nullable=False)
    token_count = Column(Integer, nullable=True)
    metadata_ = Column("metadata", JSONB, default=dict)
    strategy = Column(String(100), default="LocalSemantic")
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    embedding = relationship("ChunkEmbedding", back_populates="chunk", uselist=False, cascade="all, delete-orphan")

class ChunkEmbedding(Base):
    """
    Table storing 1024-dimensional dense vectors with pgvector.
    """
    __tablename__ = "chunk_embeddings"

    chunk_id = Column(UUID(as_uuid=True), ForeignKey("document_chunks.id", ondelete="CASCADE"), primary_key=True)
    embedding = Column(Vector(1024), nullable=False)
    model_name = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    chunk = relationship("DocumentChunk", back_populates="embedding")
