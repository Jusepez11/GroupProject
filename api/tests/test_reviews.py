import api.models
import pytest
from unittest.mock import MagicMock, patch
from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..controllers import reviews as controller
from api.schemas.reviews import ReviewCreate
from api.models.reviews import Review
from sqlalchemy.exc import SQLAlchemyError

# DO NOT DELETE THIS
# ************************************************************************************
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
# *************************************************************************************

@pytest.fixture
def mock_db():
    return MagicMock(spec=Session)

@pytest.fixture
def sample_request():
    return ReviewCreate(
        customer_id=1,
        menu_items_id=1,
        content="Great food!",
        rating=5
    )

def test_create_review_success(mock_db, sample_request):
    mock_review = Review(
        id=1,
        customer_id=sample_request.customer_id,
        menu_items_id=sample_request.menu_items_id,
        content=sample_request.content,
        rating=sample_request.rating
    )

    mock_db.add = MagicMock()
    mock_db.commit = MagicMock()
    mock_db.refresh = MagicMock()

    with patch("api.controllers.reviews.model.Review", return_value=mock_review):
        result = controller.create(mock_db, sample_request)

    assert result.customer_id == sample_request.customer_id
    assert result.content == "Great food!"
    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once()

from sqlalchemy.exc import SQLAlchemyError

def test_create_review_db_error(mock_db, sample_request):
    mock_db.add.side_effect = SQLAlchemyError("DB failure")

    with pytest.raises(HTTPException) as exc_info:
        controller.create(mock_db, sample_request)

    assert exc_info.value.status_code == 400
    assert "DB failure" in str(exc_info.value.detail)
