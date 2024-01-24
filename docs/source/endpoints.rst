=========
Endpoints
=========

Introduction
============

Welcome to the Mix Master API documentation. This comprehensive guide details every endpoint of the Mix Master API,
including queries, request and response formats, and examples. Designed for developers and cocktail enthusiasts alike,
this API offers a seamless way to access a wide array of cocktail recipes and ingredients.
Whether you are building a cocktail app or exploring new drink ideas, this documentation will
provide you with the necessary tools to make the most out of the Mix Master API.

.. note:: If you don't have an API key, visit our `purchase page <https://github.com/RobertArnosson/mixmasterapidoc>`_ to get one.

Cocktails
=========

List every cocktail
-------------------

Retrieves a comprehensive list of cocktails. You can filter the results by page, number of items per
page, search query, search accuracy threshold, and description language. This endpoint is ideal for
browsing cocktails or searching for specific drinks based on ingredients or names.

**GET** ``/api/cocktails``

+------------+------------+-------------------------------------------+----------------------------+
| Queries    | Type       | Description                               | Example                    |
+============+============+===========================================+============================+
| **p**      | int        | The current page                          | */api/cocktails*?p=2       |
+------------+------------+-------------------------------------------+----------------------------+
| **a**      | int        | Total amount of items per page (*max 50*) | */api/cocktails*?a=40      |
+------------+------------+-------------------------------------------+----------------------------+
| **s**      | string     | Search query                              | */api/cocktails*?s=vodka   |
+------------+------------+-------------------------------------------+----------------------------+
| **t**      | int        | Search percent threshold (*0-100*)        | */api/cocktails*?t=50      |
+------------+------------+-------------------------------------------+----------------------------+
| **l**      | string     | Description language                      | */api/cocktails*?l=en,fr   |
+------------+------------+-------------------------------------------+----------------------------+

+-----------------+-------------------------------------------+-----------------------------------------------------------+
| Headers         | Description                               | Example                                                   |
+=================+===========================================+===========================================================+
| **Mix-Api-Key** | Your api key goes in this header          | *Mix-Api-Key:* 92SoxiUG.mWOjrx4UDEFisdpTWvVyr8BSi6DunHsS  |
+-----------------+-------------------------------------------+-----------------------------------------------------------+

**Example Request**

.. sourcecode:: bash
  
    curl -s -H "Mix-Api-Key: 92SoxiUG.mWOjrx4UDEFisdpTWvVyr8BSi6DunHsS" curl -X GET https://api.mixmaster.app/api/cocktails

**Example Response**

.. sourcecode:: json

    {
        "items": [
          {
              "WIP"
          }
        ],
        "current_page": 1,
        "max_page": 1,
        "items_per_page": 25
    }

Get a cocktail from an id
-------------------------

Fetch detailed information about a specific cocktail by its unique ID. This endpoint is useful for
obtaining in-depth details of a cocktail, including its ingredients, preparation method, and history.
You can also specify the language for the cocktail description.

**GET** ``/api/cocktails/{id}``

+------------+------------+-------------------------------------------+----------------------------+
| Queries    | Type       | Description                               | Example                    |
+============+============+===========================================+============================+
| **l**      | string     | Description language                      | */api/cocktails*?l=en,fr   |
+------------+------------+-------------------------------------------+----------------------------+

+-----------------+-------------------------------------------+-----------------------------------------------------------+
| Headers         | Description                               | Example                                                   |
+=================+===========================================+===========================================================+
| **Mix-Api-Key** | Your api key goes in this header          | *Mix-Api-Key:* 92SoxiUG.mWOjrx4UDEFisdpTWvVyr8BSi6DunHsS  |
+-----------------+-------------------------------------------+-----------------------------------------------------------+

**Example Request**

.. sourcecode:: bash
  
    curl -s -H "Mix-Api-Key: 92SoxiUG.mWOjrx4UDEFisdpTWvVyr8BSi6DunHsS" curl -X GET https://api.mixmaster.app/api/cocktails/{id}

**Example Response**

.. sourcecode:: json

    {
        "WIP"
    }


Ingredients
===========

List every ingredient
---------------------

Access a complete list of ingredients used in cocktails. This endpoint supports filtering by page,
number of items per page, search queries, accuracy threshold for search results, and language for
ingredient descriptions. It's essential for discovering new ingredients or finding details about
familiar ones.

**GET** ``/api/ingredients``

+------------+------------+-------------------------------------------+----------------------------+
| Queries    | Type       | Description                               | Example                    |
+============+============+===========================================+============================+
| **p**      | int        | The current page                          | */api/ingredients*?p=2     |
+------------+------------+-------------------------------------------+----------------------------+
| **a**      | int        | Total amount of items per page (*max 50*) | */api/ingredients*?a=40    |
+------------+------------+-------------------------------------------+----------------------------+
| **s**      | string     | Search query                              | */api/ingredients*?s=vodka |
+------------+------------+-------------------------------------------+----------------------------+
| **t**      | int        | Search percent threshold (*0-100*)        | */api/ingredients*?t=50    |
+------------+------------+-------------------------------------------+----------------------------+
| **l**      | string     | Description language                      | */api/ingredients*?l=en,fr |
+------------+------------+-------------------------------------------+----------------------------+

+-----------------+-------------------------------------------+-----------------------------------------------------------+
| Headers         | Description                               | Example                                                   |
+=================+===========================================+===========================================================+
| **Mix-Api-Key** | Your api key goes in this header          | *Mix-Api-Key:* 92SoxiUG.mWOjrx4UDEFisdpTWvVyr8BSi6DunHsS  |
+-----------------+-------------------------------------------+-----------------------------------------------------------+

**Example Request**

.. sourcecode:: bash
  
    curl -s -H "Mix-Api-Key: 92SoxiUG.mWOjrx4UDEFisdpTWvVyr8BSi6DunHsS" curl -X GET https://api.mixmaster.app/api/ingredients

**Example Response**

.. sourcecode:: json

  {
      "items": [
          {
              "id": 1,
              "name": "Vodka",
              "description": {
                  "en": "Vodka is a clear distilled alcoholic be...",
                  "fr": "La vodka est une boisson alcoolisée dis..."
              },
              "type": "Spirit",
              "alcoholic": "Alcoholic",
              "abv": "40",
              "allergies": [],
              "imageURL": "https://mixmaster.pythonanywhere.com/img/ingredients/vodka",
              "last_modified": "2024-01-23T18:02:18.208282Z"
          },
          {
              "id": 2,
              "name": "Gin",
              "description": {
                  "en": "Gin is a distilled alcoholic drink that...",
                  "fr": "Le gin est une boisson alcoolisée disti..."
              },
              "type": "Spirit",
              "alcoholic": "Alcoholic",
              "abv": "40",
              "allergies": [],
              "imageURL": "https://mixmaster.pythonanywhere.com/img/ingredients/gin",
              "last_modified": "2024-01-23T18:02:18.325318Z"
          },
          {
              "id": 3,
              "name": "Tequila",
              "description": {
                  "en": "Tequila is a distilled beverage made fr...",
                  "fr": "La tequila est une boisson distillée fa..."
              },
              "type": "Spirit",
              "alcoholic": "Alcoholic",
              "abv": "40",
              "allergies": [],
              "imageURL": "https://mixmaster.pythonanywhere.com/img/ingredients/tequila",
              "last_modified": "2024-01-23T18:02:18.437972Z"
          }
      ],
      "current_page": 1,
      "max_page": 1,
      "items_per_page": 25
  }

Get an ingredient from an id
----------------------------

Obtain detailed information about a particular ingredient by its ID. This includes its type, alcohol
content, potential allergens, and a description in different languages. This endpoint is particularly
useful for learning more about specific ingredients, their uses, and their characteristics.

**GET** ``/api/ingredients/{id}``

+------------+------------+-------------------------------------------+----------------------------+
| Queries    | Type       | Description                               | Example                    |
+============+============+===========================================+============================+
| **l**      | string     | Description language                      | */api/ingredients*?l=en,fr |
+------------+------------+-------------------------------------------+----------------------------+

+-----------------+-------------------------------------------+-----------------------------------------------------------+
| Headers         | Description                               | Example                                                   |
+=================+===========================================+===========================================================+
| **Mix-Api-Key** | Your api key goes in this header          | *Mix-Api-Key:* 92SoxiUG.mWOjrx4UDEFisdpTWvVyr8BSi6DunHsS  |
+-----------------+-------------------------------------------+-----------------------------------------------------------+

**Example Request**

.. sourcecode:: bash
  
    curl -s -H "Mix-Api-Key: 92SoxiUG.mWOjrx4UDEFisdpTWvVyr8BSi6DunHsS" curl -X GET https://api.mixmaster.app/api/ingredients/1

**Example Response**

.. sourcecode:: json

    {
        "id": 1,
        "name": "Vodka",
        "description": {
            "en": "Vodka is a clear distilled alcoholic beverage...",
            "fr": "La vodka est une boisson alcoolisée distillée..."
        },
        "type": "Spirit",
        "alcoholic": "Alcoholic",
        "abv": "40",
        "allergies": [],
        "imageURL": "https://mixmaster.pythonanywhere.com/img/ingredients/vodka",
        "last_modified": "2024-01-23T18:02:18.208282Z"
    }


Lists
=====

This endpoint provides various categorized lists like cocktail categories, types of alcoholic beverages,
difficulty levels of recipes, available languages for descriptions, types of glasses used, temperature
at which drinks are served, and common allergens. It's a handy resource for filtering and categorizing
data based on specific attributes.

**GET** ``/api/list/{list}``

+-------------------+-------------------------------------------+----------------------------+
| Lists             | Description                               | Example                    |
+===================+===========================================+============================+
| **Category**      | Description language                      | /api/list/category         |
+-------------------+-------------------------------------------+----------------------------+
| **Alcoholic**     | Description language                      | /api/list/alcoholic        |
+-------------------+-------------------------------------------+----------------------------+
| **Difficulty**    | Description language                      | /api/list/difficulty       |
+-------------------+-------------------------------------------+----------------------------+
| **Languages**     | Description language                      | /api/list/languages        |
+-------------------+-------------------------------------------+----------------------------+
| **Glass**         | Description language                      | /api/list/glass            |
+-------------------+-------------------------------------------+----------------------------+
| **Type**          | Description language                      | /api/list/type             |
+-------------------+-------------------------------------------+----------------------------+
| **Temperature**   | Description language                      | /api/list/temperature      |
+-------------------+-------------------------------------------+----------------------------+
| **Allergen**      | Description language                      | /api/list/allergen         |
+-------------------+-------------------------------------------+----------------------------+

+-----------------+-------------------------------------------+-----------------------------------------------------------+
| Headers         | Description                               | Example                                                   |
+=================+===========================================+===========================================================+
| **Mix-Api-Key** | Your api key goes in this header          | *Mix-Api-Key:* 92SoxiUG.mWOjrx4UDEFisdpTWvVyr8BSi6DunHsS  |
+-----------------+-------------------------------------------+-----------------------------------------------------------+

**Example Request**

.. sourcecode:: bash
  
    curl -s -H "Mix-Api-Key: 92SoxiUG.mWOjrx4UDEFisdpTWvVyr8BSi6DunHsS" curl -X GET https://api.mixmaster.app/api/list/category

**Example Response**

.. sourcecode:: json

    {
        "data": [
            "Ordinary drink",
            "Cocktail",
            "Shake",
            "Cocoa",
            "Shot",
            "Coffee",
            "Tea",
            "Homemade",
            "Party drink",
            "Beer",
            "Soft drink",
            "Other"
        ]
    }