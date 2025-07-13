# 🍺 BreweryDB Python Client

A lightweight Python client for querying the [Open Brewery DB](https://www.openbrewerydb.org/) API, with typed parameter validation and response modeling using `pydantic`.

---

## 📦 Features

- Fetch a **single brewery** by ID  
- Fetch a **list of breweries** filtered by city, state, type, and more  
- Optional parameters are validated and serialized cleanly  
- Uses Pydantic for **type safety** and **API response modeling**  
- Built-in logging for API request failures  
- Resilient to partial or missing data from the API  

---

## 🛠 Installation

This client requires **Python 3.10+**.

    pip install requests pydantic

---

## 🚀 Usage

### Import the classes

    from api import GetSingleBrewery, GetBreweryList

### Get a single brewery by ID

    client = GetSingleBrewery()
    brewery = client("10-barrel-brewing-co-bend-1")
    print(brewery.name)  # → "10 Barrel Brewing Co"

---

### Get a list of breweries with filters

    client = GetBreweryList()
    breweries = client(by_city="San Diego", by_type="micro", per_page=5)

    for b in breweries:
        print(f"{b.name} – {b.brewery_type}")

---

## 🎯 Supported Query Parameters

| Parameter     | Description                              |
|---------------|------------------------------------------|
| `by_city`     | Filter by city                           |
| `by_state`    | Filter by U.S. state                     |
| `by_country`  | Filter by country                        |
| `by_name`     | Filter by name (substring match)         |
| `by_postal`   | Filter by postal code                    |
| `by_type`     | One of: `micro`, `nano`, `brewpub`, etc. |
| `by_ids`      | List of brewery IDs                      |
| `by_dist`     | Tuple of `(latitude, longitude)`         |
| `per_page`    | Number of results per page (default: 20) |

---

## 📘 Response Schema

Example:

    BreweryInfo(
        id="10-barrel-brewing-co-bend-1",
        name="10 Barrel Brewing Co",
        brewery_type="large",
        city="Bend",
        state_province="Oregon",
        country="United States",
        latitude=44.06,
        longitude=-121.31,
        phone="1234567890",
        website_url="https://example.com"
    )

---

## 📂 Project Structure

    api.py           # Main client code
    README.md         # This file

---

## 🙋‍♂️ Author

Created by **Abel Joseph**
