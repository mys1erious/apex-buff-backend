# API for Apex Legends

## API:
- [Live](https://apex-buff-development.herokuapp.com)

## Frontend made by [yurii-bel](https://github.com/yurii-bel):
- [Git](https://github.com/mys1erious/apex-buff-frontend/tree/master)
- [Live](https://apex-buff.herokuapp.com/)

## Stack:
- Backend: Django, DRF, Postgresql, Cloudinary, Heroku
- Frontend: React
### Weapon, Legends data is taken from:
- https://apexlegends.fandom.com/wiki/Weapon
- https://apexlegends.fandom.com/wiki/Legend
- [Scrapers](https://github.com/mys1erious/apex-buff-data)
### User Stats are taken from [apex.tracker.gg API](https://apex.tracker.gg/)

## Media:
### API:
https://user-images.githubusercontent.com/64038614/197342459-3e05ea8a-6413-4f50-98e9-102c6489dc17.mp4

### Frontend:
https://user-images.githubusercontent.com/64038614/197344750-0b99e0fe-1c28-47a7-8d53-9cd2956d585b.mp4

### Examples of response data:
### Legends:
```
--> https://apex-buff-development.herokuapp.com/api/v1/legends/valkyrie/

{
    "name": "Valkyrie",
    "icon_url": "http://res.cloudinary.com/hfiynpxd2/image/upload/e_bgremoval/v1657053192/legends/Valkyrie.png",
    "slug": "valkyrie",
    "role": "Winged Avenger",
    "real_name": "Kairi Imahara (今原カイリ)",
    "gender": "Female",
    "age": 30,
    "homeworld": "Angelia",
    "lore": "“ Bold, brash, fiery and fierce, Kairi Imahara isn’t above greasing palms and bending the law. When she was a child, she stole a Titan. It belonged to her dad: callsign Viper. She wanted to be just like him when she grew up. But the next day he left on a mission and never returned. In some ways, she still followed in his footsteps: it wasn't a Titan, but her ship offered a decent living. Her personal life, however, was anything but. During the day, she smuggled precious cargo, and at night, went shot for shot with the outlaws and mercs in the bars. But even though she had her ladies, her liquor, and her love of the sky, she was still obsessed with finding the man who’d put her father in harm’s way: his commander, Kuben Blisk.\nShe tracked Blisk down, prepared to kill him. But he spoke of her father with respect -- and challenged her to be better. She shot him anyway. But not to kill. Knowing she could get to him was enough. Well, that, and the Apex Games card she took from Blisk’s grasp.\nUsing the intact flight core from Viper’s Northstar, she built a sleek new jetpack that honored her father’s memory. And that was when Kairi could finally soar on her own… and in a version of her dad’s Titan, that ended up being hers after all.",
    "legend_type": {
        "name": "Recon",
        "slug": "recon",
        "icon_url": "https://res.cloudinary.com/hfiynpxd2/legends/types/Recon"
    },
    "abilities": [
        {
            "slug": "valkyrie-missile-swarm",
            "legend": "Valkyrie",
            "name": "Missile Swarm",
            "description": "Fire a swarm of mini-rockets that damage and disorient the enemy.",
            "info": "Launches 12 missiles in a 4x3 array, dealing damage and stunning enemies.\nIf a Legend gets hit, the first missile deals 25 damage and every subsequent missile deals 3.\nNeeds ample vertical clearance to use, meaning the player cannot use it on interior spaces with low ceilings.\nMinimum target distance (same elevation) is 12 meters; Maximum target distance is 100 meters horizontally, regardless of elevation difference between target and Valkyrie.\nWhen within valid range, the crosshair aligns with the closest row's middle rocket.",
            "icon_url": "http://res.cloudinary.com/hfiynpxd2/image/upload/e_trim/e_bgremoval/v1657053194/abilities/valkyrie_missile_swarm.png",
            "ability_type": "Tactical",
            "cooldown": 30
        },
        {
            "slug": "valkyrie-skyward-dive",
            "legend": "Valkyrie",
            "name": "Skyward Dive",
            "description": "Press once to prepare for launch. Teammates can interact with Valkyrie to join the launch. Press again to launch into the air and skydive.",
            "info": "Upon usage, Valkyrie enters a setup animation that charges up over 2 seconds, after which she can press Fire to launch ~180m into the air in about 7 seconds (1.5 seconds slow climbing and 5.5 seconds fast climbing) and enter a skydive, similar to using a Jump Tower. Squadmates can press Interact near Valkyrie to launch with her.\nSkyward Dive can be canceled during setup either by taking damage or manually by pressing the Ultimate button again. 75% of its charge is refunded when canceled.\nWhile in pre-launch, using ping will mark Valkyrie for her squad and display a \"Let's fly!\" notification in the kill feed.\nVertical clearance is required for flight.",
            "icon_url": "http://res.cloudinary.com/hfiynpxd2/image/upload/e_trim/e_bgremoval/v1657053196/abilities/valkyrie_skyward_dive.png",
            "ability_type": "Ultimate",
            "cooldown": 180
        },
        {
            "slug": "valkyrie-vtol-jets",
            "legend": "Valkyrie",
            "name": "Vtol Jets",
            "description": "Press the jump key while in the air to engage jetpack. You can switch between hold and toggle mode in the options menu.",
            "info": "VTOL Jets\nWhile in the air, press Jump again to engage VTOL Jets.\nUsing the Jets consumes fuel. The Fuel gauge is on the right side of the screen.\nActivating the VTOL Jets will consume about 12.5% of total fuel.\nMaximum duration is 7 seconds.\nFuel will begin to refill 8 seconds after the last Jets' usage.\nFully refueling from empty takes 10 seconds. (1 second will refill 10% of total fuel)\nWhile using the Jets, Valkyrie cannot use any weapons except for her Missile Swarm.\nOnce the Jets are released, there is a 1-second delay (a hand animation will be played) before she can use her weapons.\nNormal flight direction is upwards in the direction Valkyrie is facing.\nHold ADS to conduct level flight.\nJet-Fighter HUD\nActivates while skydiving or using her ultimate, Skyward Dive (in both launch and skydive).\nMarks any enemies within 250 meters with a direct and uninterrupted line of sight to Valkyrie. The champion will be marked with \"CH\" and the kill leader will be marked with \"KL\".\nEnemies are not notified by this scan, unlike Bloodhound and Crypto.\nSquadmates attached to Valkyrie also benefit from these target callouts.",
            "icon_url": "http://res.cloudinary.com/hfiynpxd2/image/upload/e_trim/e_bgremoval/v1657053195/abilities/valkyrie_vtol_jets.png",
            "ability_type": "Passive",
            "cooldown": null
        },
        {
            "slug": "valkyrie-recon",
            "legend": "Valkyrie",
            "name": "Recon",
            "description": "Scanning Survey Beacons reveals the next circle's location.",
            "info": "Allows the player to access the 12 survey beacons available on the map in any given match to determine the circle location after the currently marked circle.\nThe interaction with the survey beacon takes 7 seconds, during which the player is vulnerable.",
            "icon_url": "http://res.cloudinary.com/hfiynpxd2/image/upload/e_trim/e_bgremoval/v1657053197/abilities/valkyrie_recon.png",
            "ability_type": "Perk",
            "cooldown": null
        }
    ]
}
```
### Abilities:
```
--> https://apex-buff-development.herokuapp.com/api/v1/abilities/bangalore-smoke-launcher/

{
    "slug": "bangalore-smoke-launcher",
    "legend": "Bangalore",
    "name": "Smoke Launcher",
    "description": "Fire a high-velocity smoke canister that explodes into a smoke wall on impact.",
    "info": "Has two charges, allowing it to be used twice in a row.\nThe launcher allows Bangalore to fire canisters farther than grenades can be thrown.\nUpon landing, the canister splits into three, which land in a line perpendicular to where it was launched from. Takes 23 seconds to evaporate.\nThe canister's explosion deals 10 damage to enemies.\nMelee to cancel the launch.",
    "icon_url": "http://res.cloudinary.com/hfiynpxd2/image/upload/e_trim/e_bgremoval/v1657053086/abilities/bangalore_smoke_launcher.png",
    "ability_type": "Tactical",
    "cooldown": 33
}
```
### Weapons:
```
--> https://apex-buff-development.herokuapp.com/api/v1/weapons/sentinel/

{
    "slug": "sentinel",
    "name": "Sentinel",
    "icon_url": "http://res.cloudinary.com/hfiynpxd2/image/upload/e_trim/e_bgremoval/v1657631985/weapons/Sentinel.png",
    "weapon_type": "Sniper rifle",
    "attachments": [
        {
            "slug": "sniper-stock",
            "name": "Sniper Stock",
            "icon_url": "http://res.cloudinary.com/hfiynpxd2/image/upload/e_trim/e_bgremoval/v1657637910/weapons/attachments/Sniper_Stock.png"
        },
        {
            "slug": "deadeyes-tempo",
            "name": "Deadeye's Tempo",
            "icon_url": "http://res.cloudinary.com/hfiynpxd2/image/upload/e_trim/e_bgremoval/v1657637918/weapons/attachments/Deadeye_s_Tempo.png"
        },
        {
            "slug": "sniper-optics",
            "name": "Sniper optics",
            "icon_url": "http://res.cloudinary.com/hfiynpxd2/image/upload/e_trim/e_bgremoval/v1657637920/weapons/attachments/Sniper_optics.png"
        },
        {
            "slug": "extended-sniper-mag",
            "name": "Extended Sniper Mag",
            "icon_url": "http://res.cloudinary.com/hfiynpxd2/image/upload/e_trim/e_bgremoval/v1657637922/weapons/attachments/Extended_Sniper_Mag.png"
        }
    ],
    "ammo": [
        {
            "slug": "extended-heavy-mag",
            "name": "Extended Heavy Mag",
            "icon_url": "http://res.cloudinary.com/hfiynpxd2/image/upload/e_trim/e_bgremoval/v1657637898/weapons/attachments/Extended_Heavy_Mag.png"
        }
    ],
    "projectile_speed": 31000,
    "damage": [
        {
            "modificator": {
                "slug": "default",
                "name": "default",
                "icon_url": "http://res.cloudinary.com/hfiynpxd2/image/upload/e_trim/e_bgremoval/no_image"
            },
            "body": 70,
            "head": 140,
            "legs": 63
        },
        {
            "modificator": {
                "slug": "sniper-ammo-amped",
                "name": "sniper ammo amped",
                "icon_url": "http://res.cloudinary.com/hfiynpxd2/image/upload/e_trim/e_bgremoval/v1658255480/weapons/modificators/Sniper_Ammo_Amped.webp"
            },
            "body": 88,
            "head": 176,
            "legs": 79
        }
    ],
    "fire_modes": [
        {
            "fire_mode": {
                "slug": "single",
                "name": "Single",
                "icon_url": "http://res.cloudinary.com/hfiynpxd2/image/upload/e_trim/e_bgremoval/v1657469639/weapons/firemods/Single.png"
            },
            "stats": {
                "modificator": {
                    "slug": "sniper-ammo-amped",
                    "name": "sniper ammo amped",
                    "icon_url": "http://res.cloudinary.com/hfiynpxd2/image/upload/e_trim/e_bgremoval/v1658255480/weapons/modificators/Sniper_Ammo_Amped.webp"
                },
                "rpm": 31,
                "dps": 46,
                "ttk": 3.87
            }
        },
        {
            "fire_mode": {
                "slug": "single",
                "name": "Single",
                "icon_url": "http://res.cloudinary.com/hfiynpxd2/image/upload/e_trim/e_bgremoval/v1657469639/weapons/firemods/Single.png"
            },
            "stats": {
                "modificator": {
                    "slug": "default",
                    "name": "default",
                    "icon_url": "http://res.cloudinary.com/hfiynpxd2/image/upload/e_trim/e_bgremoval/no_image"
                },
                "rpm": 31,
                "dps": 36,
                "ttk": 3.87
            }
        }
    ]
}
```
### User Stats: 
Too much
