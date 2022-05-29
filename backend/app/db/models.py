from sys import maxsize
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy_utils import URLType
import uuid

from .session import Base
from .custom_types import ChoiceField
from ..core.utils import get_default_archive_methods
from sqlalchemy.orm import relationship


EXTRACTORS = get_default_archive_methods()
STATUS_CHOICES = [
    "pending",
    "running",
    "succeeded",
    "failed",
    "skipped",
]


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)


class ArchiveResult(Base):
    __tablename__ = "archive_result"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4)
    snapshot_id = Column(ForeignKey('snapshot.id'))
    snapshot = relationship('Snapshot', back_populates='archive_results')
    extractor = Column(ChoiceField(EXTRACTORS))
    output = Column(String)
    start_ts = Column(DateTime, index=True)
    end_ts = Column(DateTime)
    status = Column(ChoiceField(STATUS_CHOICES), index=True)


class Snapshot(Base):
    __tablename__ = "snapshot"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    url = Column(URLType, unique=True, index=True)
    timestamp = Column(String, unique=True, index=True)
    added = Column(DateTime, index=True)
    updated = Column(DateTime, index=True)
    archive_results = relationship('ArchiveResult', back_populates='snapshot')
