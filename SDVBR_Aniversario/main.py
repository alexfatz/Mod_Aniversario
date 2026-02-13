from ModEntry import ModEntry
from StardewValley import Manifest

manifest=Manifest(
    Name="SDVBR_Aniversario",
    Author="Fatz",
    Version="1.0",
    Description="Stardew Valley Brasil",
    UniqueID="Fatz.SDVBR_Aniversario"
)
mod=ModEntry(manifest=manifest)

mod.write()
