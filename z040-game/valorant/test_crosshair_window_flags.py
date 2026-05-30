import ast
import unittest
from pathlib import Path


class CrosshairWindowFlagsTest(unittest.TestCase):
    def setUp(self):
        source = Path(__file__).with_name("cross.py").read_text(encoding="utf-8")
        self.tree = ast.parse(source)
        self.class_node = next(
            node for node in self.tree.body if isinstance(node, ast.ClassDef) and node.name == "TopmostCrosshair"
        )

    def test_force_topmost_uses_only_defined_swp_flags(self):
        method_node = next(node for node in self.class_node.body if isinstance(node, ast.FunctionDef) and node.name == "force_topmost")

        assigned = {
            target.id
            for node in ast.walk(method_node)
            if isinstance(node, ast.Assign)
            for target in node.targets
            if isinstance(target, ast.Name)
        }
        used_swp_flags = {
            node.id
            for node in ast.walk(method_node)
            if isinstance(node, ast.Name) and node.id.startswith("SWP_")
        }

        self.assertLessEqual(used_swp_flags, assigned)

    def test_layered_window_uses_color_key_instead_of_global_alpha(self):
        method_node = next(
            node
            for node in self.class_node.body
            if isinstance(node, ast.FunctionDef) and node.name == "set_window_properties_enhanced"
        )
        assigned_constants = {
            target.id: node.value.value
            for node in ast.walk(method_node)
            if isinstance(node, ast.Assign)
            and isinstance(node.value, ast.Constant)
            for target in node.targets
            if isinstance(target, ast.Name)
        }
        layered_calls = [
            node
            for node in ast.walk(method_node)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "SetLayeredWindowAttributes"
        ]

        self.assertEqual(assigned_constants.get("LWA_COLORKEY"), 0x01)
        self.assertNotIn("LWA_ALPHA", assigned_constants)
        self.assertTrue(layered_calls)
        self.assertEqual(layered_calls[0].args[-1].id, "LWA_COLORKEY")


if __name__ == "__main__":
    unittest.main()
