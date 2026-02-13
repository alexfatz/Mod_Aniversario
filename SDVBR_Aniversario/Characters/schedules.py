from StardewValley import EditData, Helper


class SchedulesAniversario:
    def __init__(self, mod: Helper):
        self.mod = mod
        self.contents()

    def contents(self):
        schedules_setup = {
            "Abigail": "900 Town 24 76 2/2500 SeedShop 1 9 3 abigail_sleep", 
            "Alex": "900 Town 37 76 3/2500 JoshHouse 21 4 1 alex_sleep", 
            "Caroline": "900 Town 35 60 2/2500 SeedShop 25 4 1 caroline_sleep", 
            "Clint": "900 Town 28 60 2/2500 Blacksmith 10 4 1 clint_sleep",
            "Demetrius": "900 Town 33 59 2/2500 ScienceHouse 15 4 0 demetrius_sleep",
            "Elliott": "900 Town 31 58 3/2500 ElliottHouse 13 4 1 elliott_sleep",
            "Emily": "900 Town 27 62 2/2500 HaleyHouse 21 4 1 emily_sleep",
            "Evelyn": "900 Town 31 61 2/2500 JoshHouse 4 17 0",
            "George": "900 Town 31 62 2/2500 JoshHouse 3 5 0 george_sleep",
            "Gus": "900 Town 26 62 2/2500 Saloon 23 4 1 gus_sleep",
            "Haley": "900 Town 36 76 1/2500 HaleyHouse 1 5 3 haley_sleep",
            "Harvey": "900 Town 22 61 2/2500 Hospital 4 4 0 harvey_sleep",
            "Jas": "900 Town 19 64 1/2500 AnimalShop 1 7 3 jas_sleep",
            "Jodi": "900 Town 29 62 2/2500 SamHouse 22 5 1 jodi_sleep",
            "Kent": "900 Town 30 62 2/2500 SamHouse 21 5 3 kent_sleep",
            "Leah": "900 Town 31 59 3/2500 LeahHouse 2 4 3 leah_sleep",
            "Lewis": "900 Town 35 70 3/2500 ManorHouse 22 4 1 lewis_sleep",
            "Linus": "900 Town 32 56 2/2500 Tent 4 4 2 linus_sleep",
            "Marnie": "900 Town 35 69 3/2500 AnimalShop 12 5 3 marnie_sleep",
            "Maru": "900 Town 23 61 2/2500 ScienceHouse 2 4 3 maru_sleep",
            "Pam": "900 Town 25 58 1/2500 Trailer 15 4 2 pam_sleep",
            "Penny": "900 Town 20 62 2/2500 Trailer 4 9 1 penny_sleep",
            "Pierre": "900 Town 33 60 2/2500 SeedShop 24 4 3 pierre_sleep", 
            "Robin": "900 Town 34 59 2/2500 ScienceHouse 21 4 1 robin_sleep",
            "Sam": "900 Town 23 77 1/2500 SamHouse 6 13 0 sam_sleep",
            "Sebastian": "900 Town 25 77 3/2500 SebastianRoom 11 9 1 sebastian_sleep",
            "Shane": "900 Town 25 59 1/2500 AnimalShop 27 4 1 shane_sleep",
            "Vincent": "900 Town 20 64 3/2500 SamHouse 8 22 3 vincent_sleep",
            "Willy": "900 Town 38 69 3/2500 FishShop 5 4 2",
        }

        for name, schedule in schedules_setup.items():
            self.mod.content.registryContentData(
                EditData(
                    LogName=f"schedules_{name}",
                    Target=f"Characters/schedules/{name}",
                    Entries={"summer_19": schedule},
                )
            )
