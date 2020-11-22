<?php

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