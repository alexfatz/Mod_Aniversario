from StardewValley import (
    Manifest,
    Helper,
    ContentPatcher,
    EditData
)
from Characters.schedules import SchedulesAniversario
from Maps.CarregarMaps import CarregarMaps
from pathlib import Path
from StardewValley.Data import AudioChangesData
from StardewValley.Data.GameData import AudioCategory


class ModEntry(Helper):
    def __init__(self, manifest: Manifest):
        super().__init__(
            manifest=manifest, modFramework=ContentPatcher(manifest=manifest)
        )
        self.contents()


    def contents(self):
        maps_files = Path("assets/Maps")
        self.assetsFileIgnore = [
            f"Maps/{i.stem}.png"
            for i in maps_files.glob("*.png")
            if i.stem
            not in ("SDVBR_Bandeira", "SDVBR_Bandeira2", "bexigas", "bolo", "chama")
        ]

        self.content.registryContentData(
            EditData(
                LogName="adicionando_falas",
                Target="Strings/StringsFromMaps",
                Entries={
                    "nota_aniversario": "O encontro entre os pelicanos está marcado para 18 do verão.",
                    "nota_npc_aniversario": "Obrigado por participar! Parabéns Stardew Valley Brasil!"
                }
            )
        )

        for m in maps_files.glob("*.tmx"):
            if m.stem == "chama":
                continue
            CarregarMaps(self, m.stem)

        self.content.registryContentData(
            EditData(
                LogName="adicionando_musica",
                Target="Data/AudioChanges",
                Entries={
                    f"musica_parabens": AudioChangesData(
                        key="musica_parabens",
                        ID="musica_parabens",
                        FilePaths=["{{AbsoluteFilePath: assets/musica_parabens.ogg}}"],
                        Category=AudioCategory.Music,
                        StreamVorbis = True,
                        Looped = False,
                        UseReverb = False
                    ).getJson()
                }
            )
        )

        SchedulesAniversario(self)
