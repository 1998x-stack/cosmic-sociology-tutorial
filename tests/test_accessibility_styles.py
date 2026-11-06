"""Static regression checks for the dependency-free course index."""
from pathlib import Path
import re
import unittest

INDEX = (Path(__file__).resolve().parents[1] / "index.html").read_text(encoding="utf-8")


class AccessibilityStylesTest(unittest.TestCase):
    def test_keyboard_focus_is_visible(self):
        self.assertRegex(INDEX, r"\.card-footer a:focus-visible\s*\{[^}]*outline:\s*3px solid")

    def test_reduced_motion_disables_transitions(self):
        block = INDEX.split("@media (prefers-reduced-motion: reduce)", 1)[1]
        self.assertRegex(block, r"\.card,\s*\.card-footer a,\s*\.card-footer a::after\s*\{[^}]*transition:\s*none")

    def test_reduced_motion_disables_hover_translation(self):
        block = INDEX.split("@media (prefers-reduced-motion: reduce)", 1)[1]
        self.assertRegex(block, r"\.card:hover,\s*\.card-footer a:hover,\s*\.card-footer a:active\s*\{[^}]*transform:\s*none")

    def test_default_hover_remains_available(self):
        self.assertIn("transform: translateY(-4px)", INDEX)
        self.assertIn("transform: scale(1.02)", INDEX)


if __name__ == "__main__":
    unittest.main()
