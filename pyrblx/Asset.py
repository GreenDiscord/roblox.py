from .utis import send_request
import aiohttp
import datetime
import time
import asyncio
from .ex import AssetNotFound
from asyncinit import asyncinit


class AssetInfo:
    def __init__(self,assetID:int,json):
        self.ID = assetID
        self.link = json

    @property
    def product_type(self):
        return self.link["ProductType"]

    @property
    def name(self):
        return self.link["Name"]

    @property
    def id(self):
        return self.link["TargetId"]


    def __repr__(self):
        return self.name

    @property
    def description(self):
        return self.link["Description"]

    @property
    def creator(self):
        return self.link["Creator"]["Name"]

    @property
    def creator_type(self):
        return self.link["Creator"]["CreatorType"]

    @property
    def price_in_robux(self):
        return self.link["PriceInRobux"] if not None else 0

    @property
    def created_at(self):
        return self.link["Created"]

    @property
    def created_age(self):
        date_time_str = self.link["Created"]
        noob = date_time_str[:10]
        strp = datetime.datetime.strptime(noob, '%Y-%m-%d')
        now = datetime.datetime.utcnow()
        diff = now - strp
        days = diff.days
        months, days = divmod(days, 30)
        yrs, months = divmod(months, 12)
        return dict(years=yrs, months=months, days=days)

    @property
    def updated_at(self):
        return self.link["Updated"]

    @property
    def update_age(self):
        date_time_str = self.link["Updated"]
        noob = date_time_str[:10]
        strp = datetime.datetime.strptime(noob, '%Y-%m-%d')
        now = datetime.datetime.utcnow()
        diff = now - strp
        days = diff.days
        months, days = divmod(days, 30)
        yrs, months = divmod(months, 12)
        return dict(years=yrs, months=months, days=days)

    @property
    def sales(self):
        return self.link["Sales"]

    @property
    def buyable(self):
        return self.link["IsForSale"]

    @property
    def isLimited(self):
        return self.link["IsLimited"]

    @property
    def isLimitedUnique(self):
        return self.link["IsLimitedUnique"]

    @property
    def remaining(self):
        return self.link["Remaining"]

    @property
    async def icon(self):
        _ok = await send_request(f"https://www.roblox.com/item-thumbnails?params=%5B%7BassetId:{self.ID}%7D%5D")
        return _ok[0]["thumbnailUrl"]

    @property
    def thumbnail(self):
        return f"https://assetgame.roblox.com/Game/Tools/ThumbnailAsset.ashx?aid={self.ID}&fmt=png&wd=420&ht=420"

    @property
    def direct_url(self):
        return f"https://www.roblox.com/games/{self.ID}/{self.name}"