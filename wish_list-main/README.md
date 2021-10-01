# book_wishlist
## Requirement
Please create a RESTful API in Python 3 to manage a user's book wishlist. Please feel free to use any web framework or other tools of your choice. This includes any database of your choice, though we would recommend SQLite for portability.
 
We would like to see API calls to add, update, or delete books from a user's wishlist.
 
For convenience, we've included what attributes users and books should have:
####	User
  -	First name
  -	Last name
  -	email
  -	Password
####	Book
  -	Title
  -	Author
  -	ISBN
  -	Date of publication
 
Tests are required.
Auth is not required.
 
Please also include a write-up of design and technology choices.
Extension for document – If you have to scale your API to GoodReads scale. What would you change in your design. Include any design diagrams that help us understand it better.

## Running Instruction
- Running the following command will start a PostgreSQL database, load sample data into it and start the Flask service

`
docker-compose up
`
- Rebuild postgres

`
rm -rf ./pg_data && docker-compose up
`
- Access postgres:

`
psql -U postgres -h localhost -d zonar
`

## Running Test
There are 3 folders under tests
- Integration: test post / put /delete endpoint
- Model: test model __str__ , __repr__, to_dict function
- Resource: unit test

`
cd src
pytest tests
`

## Note
- This endpoint is built using Flask
  - main reason I picked this because Flask is good for smaller project, easy to setup. __PLUS I already have boilerplate setup with docker.__
  - Same reason I choose to use Postgres, try to avoid wasting time on seting up project and focus on building and endpoints.
  - Did not have time to use flask migrate so go with easy route - create table schema during docker setup.
  - Ran out time + tired so code a little messy. LOL
- Future imrpovement: 
  - Add swagger doc
  - Refactor validate function
  - Let flask manage db ?
  - Maybe hash +salt password field ? 
  - Ability to delete by id
    - url: api/v1/book/wish_list/<int:wl_id>
  - Better error handling
  - Me TIRED ...

## Design
![book_wish_list](./book_wish_list.png)

## Endpoint
1. POST: Add book to wish list
* URL : `api/v1/book/wish_list`
* Add book to wish list base on user_id
```
| Name          | Data Type | Required | Description                    | Accept value          | Example    |
|---------------|-----------|----------|--------------------------------|-----------------------|------------|
| isbn          | string    | True     | isbn of the book to be insert. | string type           | 123-123    |
| user_id       | integer   | True     | User id.                       | integer bigger than 0 | 1          |
```
* Sample call:
```
curl --location --request POST 'http://localhost:5000/api/v1/book/wish_list?user_id=1&isbn=123-123'
```
* Response:
```
- Success: 200

"Added"

- Invalid request:400
{
    "error": [
        "Both isbn and user_id are required - 123-123 None"
    ]
}

- Doesn't exist: 404
{
    "error": "user_id - 10 doesnt exist"
}
```

2. PUT: Update wish list
* URL : `api/v1/book/wish_list`
* update wish list using old isbn and new isbn
```
| Name          | Data Type | Required | Description                    | Accept value          | Example    |
|---------------|-----------|----------|--------------------------------|-----------------------|------------|
| old_isbn      | string    | True     | old isbn to be update.         | string type           | 123-123    |
| new_isbn      | string    | True     | new isbn to update.            | string type           | 123-521    |
| user_id       | integer   | True     | User id.                       | integer bigger than 0 | 1          |
```
* Sample call:
```
curl --location --request PUT 'http://localhost:5000/api/v1/book/wish_list?user_id=1&old_isbn=123-123&new_isbn=121-513'
```
* Response:
```
- Success: 200

"Updated"

- Invalid request:400
{
    "error": "user_id must be int"
}

- Doesn't exist: 404
{
    "error": "Either old or new isbn 123-1234 - 121-513 doesnt exist"
}
```

3. DELETE: Remove book from wish list
* URL : `api/v1/book/wish_list`
* update wish list using old isbn and new isbn
```
| Name          | Data Type | Required | Description                    | Accept value          | Example    |
|---------------|-----------|----------|--------------------------------|-----------------------|------------|
| isbn          | string    | False    | isbn to be remove.             | string type           | 123-521    |
| user_id       | integer   | True     | User id.                       | integer bigger than 0 | 1          |
```
* Sample call:
```
curl --location --request DELETE 'http://localhost:5000/api/v1/book/wish_list?user_id=1&isbn=121-513'
```
* Response:
```
- Success: 200

"Delete"

- Invalid request:400
{
    "error": "user_id must be int"
}

- Doesn't exist: 404
{
    "error": "user_id - 10 doesnt exist"
}
```
