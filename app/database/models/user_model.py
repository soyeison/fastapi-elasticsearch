from typing import Optional
from elasticsearch_dsl import AsyncDocument, Text, Keyword, mapped_field, InnerDoc


class PhoneModel(InnerDoc):
    dial_code: str = mapped_field(Text(fields={"keyword": Keyword()}))
    number: str = mapped_field(Text(fields={"keyword": Keyword()}))
    imei: Optional[str] = mapped_field(Text())


class UserModel(AsyncDocument):
    first_name: str = mapped_field(Text(fields={"keyword": Keyword()}))
    last_name: str = mapped_field(Text(fields={"keyword": Keyword()}))
    phone: PhoneModel

    class Index:
        name = "user"
