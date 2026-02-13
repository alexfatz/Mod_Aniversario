from StardewValley import Helper, EditMap, Position, Include
from StardewValley.contentpatcher import MapTiles


class CarregarMaps:
    def __init__(self, mod: Helper, mapa: str):
        self.mod = mod
        self.mapa = mapa
        self.contents()


    def contents(self):
        light_tiles = {
            "Town": "24 50 4 33 53 4 24 58 4 21 64 4 17 86 4 27 86 4 38 65 4 30 72 4 27 72 4 41 69 4 71 67 4 52 98 4 56 98 4 92 79 4 12 48 4 13 48 4 14 48 4 15 48 4 12 49 4 13 49 4 14 49 4 15 49 4 13 50 4 14 50 4 15 50 4 34 58 1 39 58 1 44 58 1 34 61 1 39 61 1 44 61 1 24 65 1 23 69 1 33 73 1 35 71 1 36 66 1 34 62 1 26 58 1 27 58 1 26 59 1 27 59 1 29 58 1 30 58 1 29 59 1 30 59 1 30 65 6 33 70 4 84 44 4 85 44 4 86 44 4 87 44 4 84 45 4 85 45 4 86 45 4 87 45 4 84 46 4 85 46 4 86 46 4 87 46 4 2 50 1",
            "Beach": "44 31 4 90 35 4 44 32 6 90 36 6 29 1 4 30 1 4 31 1 4 32 1 4 29 2 4 30 2 4 31 2 4 32 2 4 29 3 4 30 3 4 31 3 4 32 3 4",
            "BusStop": "26 15 4 27 15 4 28 15 4 29 15 4 26 16 4 27 16 4 28 16 4 29 16 4 26 17 4 27 17 4 28 17 4 29 17 4",
            "Desert": "6 50 4 14 19 4 15 19 4 16 19 4 17 19 4 14 20 4 15 20 4 16 20 4 17 20 4 14 21 4 15 21 4 16 21 4 17 21 4",
            "Farm": "59 13 4 60 13 4 61 13 4 62 13 4 59 14 4 60 14 4 61 14 4 62 14 4 59 15 4 60 15 4 61 15 4 62 15 4",
            "Forest": "71 7 4 72 7 4 73 7 4 74 7 4 71 8 4 72 8 4 73 8 4 74 8 4 71 9 4 72 9 4 73 9 4 74 9 4",
            "Island_S": "23 8 4 24 8 4 25 8 4 26 8 4 23 9 4 24 9 4 25 9 4 26 9 4 23 10 4 24 10 4 25 10 4 26 10 4",
            "Mountain": "12 24 4 55 4 4 77 6 4 24 16 4 25 16 4 26 16 4 27 16 4 24 17 4 25 17 4 26 17 4 27 17 4 24 18 4 25 18 4 26 18 4 27 18 4",
            "Railroad": "25 43 4 26 43 4 27 43 4 28 43 4 25 44 4 26 44 4 27 44 4 28 44 4 25 45 4 26 45 4 27 45 4 28 45 4",
        }

        bolo_tiles = (Position(X=27, Y=68), Position(X=28, Y=68), Position(X=29, Y=68), Position(X=30, Y=68) , Position(X=31, Y=68), Position(X=32, Y=68), Position(X=33, Y=68), Position(X=27, Y=69), Position(X=33, Y=69), Position(X=32, Y=69), Position(X=27, Y=70), Position(X=28, Y=70), Position(X=32, Y=70), Position(X=28, Y=70), Position(X=31, Y=70), Position(X=29, Y=71), Position(X=30, Y=71), Position(X=31, Y=71))

        self.mod.content.registryContentData(
            Include(
                FromFile=self.mapa
            )
        )

        self.mod.content.registryContentData(
            EditMap(
                LogName=f"Edit_{self.mapa}Map",
                Target=f"Maps/{self.mapa}",
                FromFile=f"assets/Maps/{self.mapa}.tmx"
            ) if self.mapa == "Saloon" else

            EditMap(
                LogName=f"Edit_{self.mapa}Map",
                Target=f"Maps/{self.mapa}",
                FromFile=f"assets/Maps/{self.mapa}.tmx",
                MapProperties={
                    "Light": light_tiles[self.mapa]
                }
            ) if self.mapa != "Town" else

            EditMap(
                LogName=f"Edit_{self.mapa}Map",
                Target=f"Maps/{self.mapa}",
                FromFile=f"assets/Maps/{self.mapa}.tmx",
                MapProperties={
                    "Light": light_tiles[self.mapa]
                },
                MapTiles=[
                    MapTiles(
                        Layer="Buildings",
                        Position=position,
                        SetProperties={"Action": "HappyBirthday"}
                    ) for position in bolo_tiles
                ] + [
                    MapTiles(
                        Layer="Buildings",
                        Position=Position(X=23, Y=63),
                        SetProperties={"Action": "Parabens"}
                    ),
                    MapTiles(
                        Layer="Buildings",
                        Position=Position(X=17, Y=53),
                        SetProperties={"Action": "Message \"nota_aniversario\""}
                    ),
                    MapTiles(
                        Layer="Buildings",
                        Position=Position(X=18, Y=53),
                        SetProperties={"Action": "Presente"}
                    ),
                    MapTiles(
                        Layer="Buildings",
                        Position=Position(X=19, Y=53),
                        SetProperties={"Action": "MessageSpeech \"nota_npc_aniversario\""}
                    )
                ] + [
                    MapTiles(
                        Layer="Buildings",
                        Position=Position(X=x, Y=y),
                        SetProperties={"Action": "Comida"}
                    ) for x, y in ((26, 58), (27, 58), (26, 59), (27, 59), (26, 60), (27, 60), (29, 58), (30, 58), (29, 59), (30, 59), (29, 60), (30, 60))
                ] + [
                    MapTiles(
                        Layer="Front",
                        Position=Position(X=x, Y=y),
                        SetProperties={"Action": "Presente"}
                    ) for x, y in ((26, 57), (27, 57), (29, 57), (30, 57))
                ]
            ),

            contentFile=self.mapa
        )
