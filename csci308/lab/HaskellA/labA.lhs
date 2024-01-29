>fact :: Int -> Int
>fact 0 = 1
>fact n = n * (fact (n-1))

(fact 10) `div` (fact 5 * fact (10-5))

>choose :: Int -> Int -> Int
>choose _ 1 = 1
>choose n k = (fact n) `div` (fact k * fact (n-k))

>choose2 _ 0 = 1
>choose2 0 _ = 0
>choose2 n k = choose2 (n-1) (k-1) + choose2 (n-1) k

>fib :: Integer -> Integer
>fib 0 = 0
>fib 1 = 1
>fib n = fib (n-1) + fib (n-2)

>fibsel :: Int -> Int
>fibsel n = if n==0 then 0
>           else if n==1 then 1
>           else fibsel (n-1) + fibsel (n-2)

>fibcase :: Int -> Int
>fibcase n = case n of
>               0 -> 0
>               1 -> 1
>               n -> fibcase (n-1) + fibcase (n-2)

>hyp :: Int -> Int -> Float
>hyp a b  
>    | a <= 0    = 0.0
>    | b <= 0    = 0.0
>    | otherwise = sqrt(fromIntegral(a^2 + b^2))

