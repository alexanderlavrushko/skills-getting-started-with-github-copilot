import src.app as app_module


def test_get_activities_returns_expected_structure(client):
    # Arrange
    expected_activity_count = len(app_module.activities)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) == expected_activity_count
    assert "Chess Club" in data
    assert set(data["Chess Club"]) == {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }
