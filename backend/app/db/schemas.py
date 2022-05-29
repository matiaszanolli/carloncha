from datetime import datetime
from tokenize import Number

from pydantic import BaseModel
import typing as t
import uuid


class UserBase(BaseModel):
    email: str
    is_active: bool = True
    is_superuser: bool = False
    first_name: str = None
    last_name: str = None


class UserOut(UserBase):
    pass


class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True


class UserEdit(UserBase):
    password: t.Optional[str] = None

    class Config:
        orm_mode = True


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str = None
    permissions: str = "user"


class SnapshotBase(BaseModel):
    url: str
    timestamp: datetime = datetime.now
    added: datetime = datetime.now
    updated: t.Optional[datetime] = None


class Snapshot(SnapshotBase):
    id: uuid.uuid4

    class Config:
        orm_mode = True

class SnapshotCreate(SnapshotBase):
    pass

    class Config:
        orm_mode = True


class ArchiveResultBase(BaseModel):
    uuid: uuid.uuid4 = uuid.uuid4
    url: str
    snapshot_id: int
    extractor: str
    output: str = ''
    start_ts: datetime = datetime.now
    end_ts: t.Optional[datetime] = None


class ArchiveResult(ArchiveResultBase):
    id: int

    class Config:
        orm_mode = True


class SnapshotCreate(SnapshotBase):
    status: str = 'pending'

    class Config:
        orm_mode = True
