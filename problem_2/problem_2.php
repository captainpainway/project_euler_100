<?php

/**
 * @param $n
 * @return float|int
 *
 * Using the PHP array pointer functions end() and prev() to add the last two numbers
 * of the Fibonacci sequence together. Then, filtering for even numbers and getting the sum.
 */
function fib($n) {
    $arr = [1, 2];
    while (end($arr) < $n) {
        array_push($arr, end($arr) + prev($arr));
    }
    array_pop($arr);
    return array_sum(array_filter($arr, function ($x) {
        return $x % 2 == 0;
    }));
}

var_dump(fib(4000000));

?>