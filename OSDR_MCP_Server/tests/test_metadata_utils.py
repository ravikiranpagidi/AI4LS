import sys
import unittest
from pathlib import Path


SERVER_DIR = Path(__file__).parents[1] / "src" / "mcp_server_osdr"
sys.path.insert(0, str(SERVER_DIR))

from metadata_utils import format_mission_name


class FormatMissionNameTests(unittest.TestCase):
    def test_preserves_scalar_name(self):
        self.assertEqual(format_mission_name("SpaceX-3"), "SpaceX-3")

    def test_joins_multiple_names(self):
        self.assertEqual(
            format_mission_name(["SpaceX-3", "SpaceX-4"]),
            "SpaceX-3, SpaceX-4",
        )

    def test_missing_name_uses_na(self):
        self.assertEqual(format_mission_name(None), "N/A")


if __name__ == "__main__":
    unittest.main()
