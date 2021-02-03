import asyncio
import asyncpg

from dataclasses import dataclass
from aiohttp import ClientSession

from models_db import JsonPlaceholderUser, JsonPlaceholderPost, Session


@dataclass
class Service:
    name: str
    url: str


SERVICES = [
    Service("jsonplaceholder_users", "https://jsonplaceholder.typicode.com/users"),
    Service("jsonplaceholder_posts", "https://jsonplaceholder.typicode.com/posts"),
]


async def fetch(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def fetch_list_users(service: Service) -> str:
    async with ClientSession() as session:
        result = await fetch(session, service.url)

        to_db_users = []

        for i in result:
            id_num = i["id"]
            name = i["name"]
            email = i["email"]

            to_db_users.append(id_num)
            to_db_users.append(name)
            to_db_users.append(email)

            group_users = [tuple(to_db_users[k:k + 3]) for k in range(0, len(to_db_users), 3)]

    conn = await asyncpg.connect(
        "postgresql://pavel.giro:password@localhost/postgres"
    )

    for d in group_users:
        session = Session()
        u = JsonPlaceholderUser(id=d[0], username=d[1], email=d[2])
        session.add(u)
        session.commit()

    await conn.close()


async def fetch_list_posts(service: Service) -> str:
    async with ClientSession() as session:
        result = await fetch(session, service.url)

        to_db_posts = []

        for i in result:
            id_num = i["id"]
            title = i["title"]
            body = i["body"]

            to_db_posts.append(id_num)
            to_db_posts.append(title)
            to_db_posts.append(body)

            group_posts = [tuple(to_db_posts[k:k + 3]) for k in range(0, len(to_db_posts), 3)]


    conn = await asyncpg.connect(
        "postgresql://pavel.giro:password@localhost/postgres"
    )

    for d in group_posts:
        session = Session()
        p = JsonPlaceholderPost(id=d[0], title=d[1], body=d[2])
        session.add(p)
        session.commit()

    await conn.close()


async def get_list():
    coros = [fetch_list_users(SERVICES[0]),
             fetch_list_posts(SERVICES[1]),
             ]

    await asyncio.wait(
        coros,
        timeout=0.5,
        return_when=asyncio.ALL_COMPLETED,
    )


def run_main():
    asyncio.run(get_list())
