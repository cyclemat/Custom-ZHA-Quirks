"""ZHA custom quirk: Livarno Lux Smart Home LED-Stimmungslicht Zigbee 14156506L (TS0505B / _TZ3210_r0xgkft5).

Basiert auf dem offiziellen Lidl-RGB+CCT-Quirk und den Werten aus Zigbee2MQTT:
- Lampe meldet color_capabilities nicht korrekt -> fest auf CT + XY + HS
- Kein Enhanced Hue
- Farbtemperaturbereich 153-500 Mired
"""

from zigpy.quirks import CustomCluster
from zigpy.quirks.v2 import QuirkBuilder
from zigpy.zcl.clusters.lighting import Color


class LidlMoodLightColorCluster(CustomCluster, Color):
    """Color-Cluster mit festen Werten, die die Lampe selbst falsch/nicht meldet."""

    _CONSTANT_ATTRIBUTES = {
        Color.AttributeDefs.color_capabilities.id: 0b11001,  # HS, XY, Farbtemperatur
        Color.AttributeDefs.color_temp_physical_min.id: 153,
        Color.AttributeDefs.color_temp_physical_max.id: 500,
    }


(
    QuirkBuilder("_TZ3210_r0xgkft5", "TS0505B")
    .replaces(LidlMoodLightColorCluster, endpoint_id=1)
    .add_to_registry()
)
