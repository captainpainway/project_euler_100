<?php

function faster_largest_prime($n) {
    $factor = 2;
    $last_factor = 1;
    while ($n > 1) {
        if ($n % $factor == 0) {
            $last_factor = $factor;
            $n = $n / $factor;
        } else {
            $factor++;
        }
    }
    return $last_factor;
}

var_dump(faster_largest_prime(13195));
var_dump(faster_largest_prime(600851475143));

?>