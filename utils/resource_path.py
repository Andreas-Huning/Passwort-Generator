import sys
import os

def get_resource_path(relative_path):
    """
    Liefert den absoluten Pfad zu einer Ressource, 
    sowohl im Entwicklungsmodus als auch im PyInstaller-Bundle.
    """
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS  # temporäres Verzeichnis von PyInstaller
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
