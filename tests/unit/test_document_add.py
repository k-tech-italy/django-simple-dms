from pathlib import Path

import pytest

from django_simple_dms.models import Document


@pytest.mark.parametrize(
    "input", [
        pytest.param(__file__, id='pathname'),
        pytest.param(open(__file__, 'rb'), id='handle'),
        pytest.param(Path(__file__), id='path'),
    ]
)
def test_document_add_local_file(input, db) -> None:
    doc_obj = Document.add(document=input)

    assert doc_obj.id is not None

