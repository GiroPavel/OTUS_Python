import asyncio

from dataclasses import dataclass
from aiohttp import ClientSession

import asyncpg

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://pavel.giro:password@localhost:5432/postgres")
Base = declarative_base(bind=engine)


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)


@dataclass
class Service:
    name: str
    url: str


SERVICES = [
    Service("jsonplaceholder", "https://jsonplaceholder.typicode.com/users")
]


async def fetch(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def fetch_list_users(service: Service) -> str:
    async with ClientSession() as session:
        result = await fetch(session, service.url)

        to_db = []

        for i in result:
            id_num = i["id"]
            name = i["name"]
            email = i["email"]

            to_db.append(id_num)
            to_db.append(name)
            to_db.append(email)

            to_db_group = [tuple(to_db[k:k + 3]) for k in range(0, len(to_db), 3)]

    conn = await asyncpg.connect(
        "postgresql://pavel.giro:password@localhost/postgres"
    )

    for d in to_db_group:
        await conn.execute(
            "INSERT INTO users VALUES ($1, $2, $3)", int(d[0]), str(d[1]), str(d[2])
        )

    await conn.close()


async def get_list_users():
    coros = [fetch_list_users(s) for s in SERVICES]

    await asyncio.wait(
        coros,
        timeout=0.5,
        return_when=asyncio.ALL_COMPLETED,
    )


def run_main():
    asyncio.run(get_list_users())


if __name__ == "__main__":
    run_main()
    Base.metadata.create_all()
