<?php
function sieve_of_eratosthenes($n) {
    $arr = range(2, $n);
    $idx = 0;
    while ($idx < count($arr) / 2) {
        if ($arr[$idx] == null) {
            $idx++;
        } else {
            foreach(range($idx + $arr[$idx], count($arr), $arr[$idx]) as $i) {
                $arr[$i] = null;
            }
            $idx++;
        }
    }
    return array_filter($arr, function($x) {return $x != null;});
}

function smallest_multiple($n) {
    $primes = sieve_of_eratosthenes($n);
    $powers = array_map(function($x) use ($n) {
        return floor(log($n)/log($x));
    }, $primes);
    return array_reduce(array_map(function($v, $i) use ($powers) {
        return $v ** $powers[$i];
    } ,$primes, array_keys($primes)), function($a, $b) {
        return $a * $b;
    }, 1);
}

var_dump(smallest_multiple(20));

?>