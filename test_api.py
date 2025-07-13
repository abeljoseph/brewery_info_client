from api import BreweryInfo, GetSingleBrewery, GetBreweryList


class TestAPI:
    def __init__(self):
        self.test_data = [
            {
                'id': '5128df48-79fc-4f0f-8b52-d06be54d0cec',
                'name': '(405) Brewing Co',
                'brewery_type': 'micro',
                'address_1': '1716 Topeka St',
                'city': 'Norman',
                'state_province': 'Oklahoma',
                'postal_code': '73069-8224',
                'country': 'United States',
                'longitude': -97.46818222,
                'latitude': 35.25738891,
                'phone': '4058160490',
                'website_url': 'http://www.405brewing.com',
                'state': 'Oklahoma',
                'street': '1716 Topeka St'
            },
            {
                'id': '9c5a66c8-cc13-416f-a5d9-0a769c87d318',
                'name': '(512) Brewing Co',
                'brewery_type': 'micro',
                'address_1': '407 Radam Ln Ste F200',
                'city': 'Austin',
                'state_province': 'Texas',
                'postal_code': '78745-1197',
                'country': 'United States',
                'phone': '5129211545',
                'website_url': 'http://www.512brewing.com',
                'state': 'Texas',
                'street': '407 Radam Ln Ste F200'
            },
            {
                'id': '34e8c68b-6146-453f-a4b9-1f6cd99a5ada',
                'name': '1 of Us Brewing Company',
                'brewery_type': 'micro',
                'address_1': '8100 Washington Ave',
                'city': 'Mount Pleasant',
                'state_province': 'Wisconsin',
                'postal_code': '53406-3920',
                'country': 'United States',
                'longitude': -87.883363502094,
                'latitude': 42.720108268996,
                'phone': '2624847553',
                'website_url': 'https://www.1ofusbrewing.com',
                'state': 'Wisconsin',
                'street': '8100 Washington Ave'
            },
        ]

    def test_print(self):
        print("testing")