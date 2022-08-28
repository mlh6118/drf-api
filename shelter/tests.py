import email.utils

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from shelter.models import Animal
from http import HTTPStatus


class IntegrationTests(TestCase):
    """
    Test the forms on all pages for posting.
    Code guided by Joey Marianer.
    """

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass")

    def test_api_get(self):
        response = self.client.get(
            "/api/v1/shelter",)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_gets_animal(self):
        Animal.objects.create(
            animal_id=1,
            animal_name="Baby 'Roo",
            animal_type="Other",
            breed="Kangaroo",
            personality="Loves sitting next to me while I code.",
            cared_for_by=self.user
        )

        response = self.client.get("/api/v1/shelter")

        actual_length = len(response.json())
        expected_length = 1
        # Can be written as self.assertEqual(actual_length, expected_length).
        assert actual_length == expected_length

        actual_breed = response.json()[0]["breed"]
        expected_breed = "Kangaroo"
        assert actual_breed == expected_breed

        actual_carer_email = response.json()[0]["carer_email"]
        expected_carer_email = "tester@email.com"
        assert actual_carer_email == expected_carer_email

        assert response.json()[0]["carer_email"] == "tester@email.com"

    def test_returns_list_of_length_two(self):
        Animal.objects.create(
            animal_id=1,
            animal_name="Baby 'Roo",
            animal_type="Other",
            breed="Kangaroo",
            personality="Loves sitting next to me while I code.",
            cared_for_by=self.user
        )
        Animal.objects.create(
            animal_id=2,
            animal_name="LucyFurr",
            animal_type="Dog",
            breed="Corgi-Shepherd Mix",
            personality="Playful and energetic.",
            cared_for_by=self.user
        )

        response = self.client.get("/api/v1/shelter")

        actual_length = len(response.json())
        expected_length = 2
        self.assertEqual(actual_length, expected_length)
        self.assertEqual(len(response.json()), 2)
