<?php

/**
 * @param $n
 * @return float|int
 *
 * Optimized with the formula:
 * sum_squares = (2n + 1)(n + 1)n / 6
 * sum = n(n + 1) / 2
 */
function sum_difference($n) {
    $sum_squares = (2 * $n + 1) * ($n + 1) * $n / 6;
    $square_sum = pow($n * ($n + 1) / 2, 2);
    return $square_sum - $sum_squares;
}

var_dump(sum_difference(100));

/**
 * @param $n
 * @return float|int|mixed|null
 *
 * The naive implementation, using map and reduce.
 */
function sum_difference_2($n) {
    function square($x) {
        return pow($x, 2);
    }
    function add($x, $y) {
        return $x + $y;
    }
    $sum_squares = array_reduce(array_map('square', range(1, $n)), 'add');
    $square_sum = square(array_reduce(range(1, $n), 'add'));
    return $square_sum - $sum_squares;
}

var_dump(sum_difference_2(100));