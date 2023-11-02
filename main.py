from enum import Enum
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

app = FastAPI()


class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Dog(BaseModel):
    name: str
    pk: int
    kind: DogType


class Timestamp(BaseModel):
    id: int
    timestamp: int


dogs_db = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}

post_db = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]


@app.get('/')
def root():
    return {"message": "Successful Response"}


@app.post('/post')
def post(timestamp: Timestamp):
    current_time = int(datetime.now().timestamp())
    if timestamp.timestamp > current_time:
        raise HTTPException(status_code=400, detail="Timestamp is in the future")

    if any(post_item.id == timestamp.id for post_item in post_db):
        raise HTTPException(status_code=400, detail="Post ID already exists")

    post_db.append(timestamp)
    return timestamp


@app.get('/dog')
def get_dog(kind: Optional[DogType] = None):
    if kind is None:
        return list(dogs_db.values())
    else:
        filtered_dogs = [dog for dog in dogs_db.values() if dog.kind == kind]
        return filtered_dogs


@app.post('/dog')
def create_dog(dog: Dog):
    if dog.pk in dogs_db:
        raise HTTPException(status_code=400, detail="Dog with this Primary Key already exists")
    dogs_db[dog.pk] = dog
    return dog


@app.get('/dog/{pk}')
def get_dog_primary_key(pk: int):
    if pk not in dogs_db:
        raise HTTPException(status_code=404, detail="Dog not found")
    return dogs_db[pk]


@app.patch('/dog/{pk}')
def update_dog_primary_key(pk: int, dog: Dog):
    if pk not in dogs_db:
        raise HTTPException(status_code=404, detail="Dog not found")
    dogs_db[pk] = dog
    return dog