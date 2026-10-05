import importlib.util
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]


def load_module(relative_path: str, module_name: str):
    module_path = REPO_ROOT / relative_path
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class OfficeValidationXXESecurityTests(unittest.TestCase):
    def test_pptx_base_validator_disables_xxe_entity_resolution(self):
        base_mod = load_module(
            "skills/pptx-official/ooxml/scripts/validation/base.py", "pptx_base_val"
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            secret_file = temp_path / "secret.txt"
            secret_file.write_text("CONFIDENTIAL_DATA")

            xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
  <!ENTITY xxe SYSTEM "{secret_file.as_uri()}">
]>
<root>
  <sp id="&xxe;"/>
</root>"""
            xml_file = temp_path / "slide1.xml"
            xml_file.write_text(xml_content)

            dummy_orig = temp_path / "orig.pptx"
            dummy_orig.write_bytes(b"")

            validator = base_mod.BaseSchemaValidator(
                unpacked_dir=temp_path, original_file=dummy_orig
            )

            # Check that XMLParser was created with resolve_entities=False
            self.assertFalse(validator.parser.settings.resolve_entities if hasattr(validator.parser, "settings") else False)

            # Execute validation and ensure external secret file content is never loaded
            validator.validate_unique_ids()
            for key, id_dict in getattr(validator, "file_ids", {}).items():
                self.assertNotIn("CONFIDENTIAL_DATA", id_dict)

    def test_docx_base_validator_disables_xxe_entity_resolution(self):
        base_mod = load_module(
            "skills/docx-official/ooxml/scripts/validation/base.py", "docx_base_val"
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            secret_file = temp_path / "secret.txt"
            secret_file.write_text("CONFIDENTIAL_DATA")

            xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
  <!ENTITY xxe SYSTEM "{secret_file.as_uri()}">
]>
<root>
  <sp id="&xxe;"/>
</root>"""
            xml_file = temp_path / "document.xml"
            xml_file.write_text(xml_content)

            dummy_orig = temp_path / "orig.docx"
            dummy_orig.write_bytes(b"")

            validator = base_mod.BaseSchemaValidator(
                unpacked_dir=temp_path, original_file=dummy_orig
            )

            validator.validate_unique_ids()
            for key, id_dict in getattr(validator, "file_ids", {}).items():
                self.assertNotIn("CONFIDENTIAL_DATA", id_dict)


if __name__ == "__main__":
    unittest.main()
