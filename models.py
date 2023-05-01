class Photo():
    def __init__(self, data, scheme="Rembrandt", config="Iso:200 Tiempo_obturación:5/2000 Diafragma_F/5.6", type_photo="Retrato") -> None:
        self.data = data
        self.scheme = scheme
        self.config = config
        self.type = type_photo

    def show(self):
        print(self.data, self.scheme, self.config, self.type)
