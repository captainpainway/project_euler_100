<?php

function find_palindrome($n) {
    return $n == intval(implode("", array_reverse(str_split(strval($n)))));
}

function find_largest() {
    $palindromes = [];
    foreach(array_reverse(range(100, 999)) as $a) {
        foreach(array_reverse(range(100, 999)) as $b) {
            if (find_palindrome($a * $b)) {
                array_push($palindromes, $a * $b);
            }
        }
    }
    sort($palindromes, SORT_NUMERIC);
    return array_reverse($palindromes)[0];
}

var_dump(find_largest());

?>