def calculate_average_price(books: list[dict]) -> float:
    if not books:
        return 0.0

    total = sum(book['price'] for book in books)
    return total / len(books)

books = [
    {"title": "Title of book 1", "price": 12.50},
    {"title": "Title of book 2", "price": 9.99},
    {"title": "Title of book 3", "price": 15.00}
]

average = calculate_average_price(books)
print(f"Average price: {average:.2f}")  # Output: Average price: 12.50
