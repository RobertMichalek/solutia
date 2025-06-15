<?php
function reverse_words(string $input_sentence): string {
    $words = preg_split('/\s+/', trim($input_sentence));

    $wordsReversed = array_reverse($words);

    return implode(' ', $wordsReversed);
}

$input_sentence = "I want to work in Solutia";
$result = reverse_words($input_sentence);
echo $result; // Output: "Solutia in work to want I"



///////////////////// Bonus #1
function reverse_words_punctuation(string $input_sentence): string {
    preg_match_all('/\S+|\s+/', $input_sentence, $matches);

    $parts = $matches[0];

    $words = array_filter($parts, fn($part) => trim($part) !== '' && !preg_match('/^\s+$/', $part));

    // Otočit words
    $wordsReversed = array_reverse($words);

    $index = 0;
    foreach ($parts as &$part) {
        if (trim($part) !== '' && !preg_match('/^\s+$/', $part)) {
            $part = $wordsReversed[$index++] ?? $part;
        }
    }

    return implode('', $parts);
}

$text = "I want to work in Solutia, please!";
echo reverse_words_punctuation($text);
// Output: !please, Solutia in work to want I


///////////////////// Bonus #2
function reverse_and_swap_case(string $input_sentence): string {
    preg_match_all('/\S+|\s+/', $input_sentence, $matches);

    $parts = $matches[0];

    $words = array_filter($parts, fn($part) => trim($part) !== '' && !preg_match('/^\s+$/', $part));

    $wordsReversed = array_reverse($words);

    $index = 0;
    foreach ($parts as &$part) {
        if (trim($part) !== '' && !preg_match('/^\s+$/', $part)) {
            $part = swap_case($wordsReversed[$index++] ?? $part);
        }
    }

    return implode('', $parts);
}

function swap_case(string $text): string {
    $result = '';
    $length = mb_strlen($text, 'UTF-8');

    for ($i = 0; $i < $length; $i++) {
        $char = mb_substr($text, $i, 1, 'UTF-8');
        $upper = mb_strtoupper($char, 'UTF-8');
        $lower = mb_strtolower($char, 'UTF-8');

        $result .= ($char === $lower) ? $upper : $lower;
    }

    return $result;
}

$text = "I want to work in Solutia, please!";
echo reverse_and_swap_case($text);
// Výstup: !PLEASE, sOLUTIA IN WORK TO WANT i
