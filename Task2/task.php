<?php

function calculate_average_price(array $books): float {
    $count = count($books);
    if ($count === 0) {
        return 0.0;
    }

    $total = 0.0;
    foreach ($books as $book) {
        $total += $book['price'];
    }

    return $total / $count;
}

$books = [
    ["title" => "Title of book 1", "price" => 12.50],
    ["title" => "Title of book 2", "price" => 9.99],
    ["title" => "Title of book 3", "price" => 15.00]
];

$average = calculate_average_price($books);
echo "Average price: " . number_format($average, 2) . "\n"; // Output: Average price: 12.50
