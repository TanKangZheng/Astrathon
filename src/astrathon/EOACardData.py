from dataclasses import dataclass, fields
import re

@dataclass
class EOACardData:
    # Card ID
    cardId: str
    # Set ID # DEPRECATED FIELD #
    # setId: str
    # Card Name
    cardName: str
    # Card Affinity
    cardAffinity: str
    # Card Type
    cardType : str
    # Card Subtypes
    cardSubTypes: list[str] | None
    # Renowned
    renowned: bool
    # Supply Cost
    statSupplyCost: int | None
    # Influence
    statInfluence: int | None
    # Attack
    statAttack : int | None
    # Health
    statHealth: int | None
    # Ability Text
    abilityText: str | None
    # Formatted Ability Text
    abilityTextFormatted: str | None
    # Flavor Text
    flavorText: str | None
    # Artist Name
    artistName: str
    # Card Image
    cardImageUrl: str
    # Card Image Large
    cardImageLargeUrl: str
    # Rarity
    rarity: str
    # Print Number
    printNumber: str
    # Finish
    finish: str
    # Variant
    variant: str | None
    # Expansion Code
    expansionCode: str

    # Init
    def __init__(self, data: dict):

        # Helper function to catch non-used values
        def sentinelToNone(value, sentinel=-1000):
            return None if value == sentinel else value
        # Helper function to decode ability text
        def decode_text(text):
            if text is None:
                return None
            return re.sub(r"u([0-9A-F]{4})", r"\\u\1", text).encode().decode("unicode_escape")

        self.cardId = data.get("cardId")
        self.cardName = data.get("cardName")
        self.cardAffinity = data.get("cardAffinity")
        self.cardType = data.get("cardType")
        # Empty sub type lists are automatically converted to None
        self.cardSubTypes = data.get("cardSubTypes") or None
        self.renowned = data.get("renowned")
        self.statSupplyCost = data.get("statSupplyCost")
        # Influence, Attack and Health are set to -1000 if the card does not support that value
        self.statInfluence = sentinelToNone(data.get("statInfluence"))
        self.statAttack = sentinelToNone(data.get("statAttack"))
        self.statHealth = sentinelToNone(data.get("statHealth"))
        # Ability Text is the raw encoded version
        # Ability Text Formatted is the human-readable version
        self.abilityText = data.get("abilityText") or None
        self.abilityTextFormatted = decode_text(self.abilityText)
        self.flavorText = data.get("flavorText") or None
        self.artistName = data.get("artistName")
        self.cardImageUrl = data.get("cardImageUrl")
        self.cardImageLargeUrl = data.get("cardImageLargeUrl")
        self.rarity = data.get("rarity")
        self.printNumber = data.get("printNumber")
        self.finish = data.get("finish")
        self.variant = sentinelToNone(data.get("variant"), sentinel=0)
        self.expansionCode = data.get("expansionCode")

    ## Print
    def __str__(self) -> str:
        width = max(len(f.name) for f in fields(self))
        return "\n".join(
            f"{f.name:<{width}} : {(getattr(self, f.name))}" for f in fields(self)
        )