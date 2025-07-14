import logging

from api import BreweryInfo, GetSingleBrewery, GetBreweryList

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class TestAPI:
    def setup_method(self):
        test_data = [
            {
                "id": "5128df48-79fc-4f0f-8b52-d06be54d0cec",
                "name": "(405) Brewing Co",
                "brewery_type": "micro",
                "address_1": "1716 Topeka St",
                "city": "Norman",
                "state_province": "Oklahoma",
                "postal_code": "73069-8224",
                "country": "United States",
                "longitude": -97.46818222,
                "latitude": 35.25738891,
                "phone": "4058160490",
                "website_url": "http://www.405brewing.com",
                "state": "Oklahoma",
                "street": "1716 Topeka St",
            },
            {
                "id": "9c5a66c8-cc13-416f-a5d9-0a769c87d318",
                "name": "(512) Brewing Co",
                "brewery_type": "micro",
                "address_1": "407 Radam Ln Ste F200",
                "city": "Austin",
                "state_province": "Texas",
                "postal_code": "78745-1197",
                "country": "United States",
                "phone": "5129211545",
                "website_url": "http://www.512brewing.com",
                "state": "Texas",
                "street": "407 Radam Ln Ste F200",
            },
            {
                "id": "34e8c68b-6146-453f-a4b9-1f6cd99a5ada",
                "name": "1 of Us Brewing Company",
                "brewery_type": "micro",
                "address_1": "8100 Washington Ave",
                "city": "Mount Pleasant",
                "state_province": "Wisconsin",
                "postal_code": "53406-3920",
                "country": "United States",
                "longitude": -87.883363502094,
                "latitude": 42.720108268996,
                "phone": "2624847553",
                "website_url": "https://www.1ofusbrewing.com",
                "state": "Wisconsin",
                "street": "8100 Washington Ave",
            },
        ]

        self.test_data = [BreweryInfo.model_validate(x) for x in test_data]

    def test_single(self):
        gsb = GetSingleBrewery()

        for brewery in self.test_data:
            brew_id = brewery.id

            out = gsb(brew_id)
            assert BreweryInfo.model_validate(out) == brewery
            logger.info("Success for brewery ID: %s", brew_id)  # TODO: add handler

    def test_list_by_ids(self):
        ids = [x.id for x in self.test_data]

        gbl = GetBreweryList()
        out = gbl(by_ids=ids)

        for brew_info in out:
            bi = BreweryInfo.model_validate(brew_info)
            assert bi in self.test_data

    def test_list_by_dist(self):
        lat_long_pairs = [
            (i, (x.latitude, x.longitude))
            for i, x in enumerate(self.test_data)
            if (x.longitude and x.latitude)
        ]

        for i, pair in lat_long_pairs:
            gbl = GetBreweryList()
            out = gbl(by_dist=pair, per_page=3)

            assert self.test_data[i] in [BreweryInfo.model_validate(x) for x in out]
