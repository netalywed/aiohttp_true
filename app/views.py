from aiohttp import web
from models import Session, UserModel


class UserView(web.View):

    async def get(self):
        art_id = int(self.request.match_info['art_id'])
        session = self.request['session']
        article = await session.get(UserModel, art_id)
        if article is None:
            pass

        return web.json_response({
            'art_id': article.art_id,
            'headline': article.headline,
            'description': article.description,
            'creation_date': article.creation_date.isoformat(),     # время преобразуем в стандарт iso
            'owner': article.owner,
        })

    async def post(self):
        article_data = await self.request.json()  #получаем от клиента, на его основе создаем нового пользователя
        session = self.request['session']
        new_article = UserModel(**article_data)
        session.add(new_article)
        await session.commit()
        return web.json_response({
            'art_id': new_article.art_id,
            'headline': new_article.headline,
            'owner': new_article.owner,
        })

    async def patch(self):
        art_id = int(self.request.match_info['art_id'])
        article_data = await self.request.json()
        session = self.request['session']
        article = await session.get(UserModel, art_id)
        for field, value in article_data.items():
            setattr(article, field, value)
        session.add(article)
        await session.commit()
        return web.json_response({
            'art_id': article.art_id,
            'headline': article.headline,
            'owner': article.owner})

    async def delete(self):
        art_id = int(self.request.match_info['art_id'])
        session = self.request['session']
        article = await session.get(UserModel, art_id)
        session.delete(article)
        session.commit()
        return web.json_response({'status': 'deleted'})