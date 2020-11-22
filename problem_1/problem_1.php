<?php

function multiples($n) {
    function three_or_five($n) {
        return $n % 3 == 0 || $n % 5 == 0;
    }
    return array_sum(array_filter(range(1, $n - 1), 'three_or_five'));
}

echo multiples(1000);

?>