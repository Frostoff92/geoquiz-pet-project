def test_health_check(client):
    responce = client.get("/health")

    assert responce.status_code == 200
    assert responce.json() == {"status": "ok"}

def test_get_countries(client):
    responce = client.get("/countries")

    assert responce.status_code == 200

    data = responce.json()

    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
    assert "name" in data[0]
    assert "flag" in data[0]
    assert "difficulty" in data[0]

def test_get_country_by_id(client):
    responce = client.get("/countries/1")

    assert responce.status_code == 200

    data = responce.json()

    assert data["id"] == 1
    assert data["name"] == "Indonesia"

def test_get_country_not_found(client):
    responce = client.get("/countries/999")

    assert responce.status_code == 404
    assert responce.json()["detail"] == "Country not found"

def test_get_random_quiz(client):
    responce = client.get("/quiz/random")

    assert responce.status_code == 200

    data = responce.json()

    assert "question_country_id" in data
    assert "question" in data
    assert "flag" in data
    assert "options" in data
    assert isinstance(data["options"], list)
    assert len(data["options"]) > 0

def test_get_random_quiz_with_difficulty(client):
    response = client.get("/quiz/random?difficulty=hard")

    assert response.status_code == 200

    data = response.json()

    assert "question_country_id" in data
    assert "options" in data

    countries_responce = client.get("/countries")
    countries = countries_responce.json()

    question_country = next(
        country
        for country in countries
        if country["id"] == data["question_country_id"]
    )

    assert question_country["difficulty"] == "hard"

def test_get_random_quiz_invalid_difficulty(client):
    response = client.get("/quiz/random?difficulty=easy")

    assert response.status_code == 422

def test_submit_correct_answer(client):
    response = client.post(
        "/quiz/answer",
        json={
            "question_country_id": 1,
            "selected_country_id": 1
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["correct"] is True
    assert data["message"] == "Correct answer!"

def test_submit_wrong_answer(client):
    response = client.post(
        "/quiz/answer",
        json={
            "question_country_id": 1,
            "selected_country_id": 2
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["correct"] is False
    assert data["message"] == "Wrong answer!"

def test_submit_answer_with_unknown_question_country_id(client):
    responce = client.post(
        "/quiz/answer",
        json={
            "question_country_id": 999,
            "selected_country_id": 1
        }
    )

    assert responce.status_code == 404
    assert responce.json()["detail"] == "Question country not found"

