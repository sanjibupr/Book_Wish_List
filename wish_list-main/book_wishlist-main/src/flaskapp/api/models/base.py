from flaskapp.extensions import db


class Base(db.Model):
    """
    Base class
    """

    __abstract__ = True

    def __str__(self):
        return f"{self.__class__.__qualname__}: {self.user_id if hasattr(self, 'user_id') else self.isbn}"

    def __repr__(self):
        return f"<{self.__class__.__qualname__} object name={self.user_id if hasattr(self, 'user_id') else self.isbn}>"

    def to_dict(self):
        data = {}
        dict_keys = self.__dict__.keys()
        for k in dict_keys:
            if k == "_sa_instance_state":
                continue
            value = getattr(self, k)
            data[k] = value
        return data
