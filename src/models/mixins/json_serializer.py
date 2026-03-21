class JSONSerializer:
    def to_dict(self):
        return {c.name: getattr(self, c.name) 
                for c in self.__table__.columns
                if getattr(self, c.name) is not None}

    def to_json(self):
        return json.dumps(self.to_dict())
