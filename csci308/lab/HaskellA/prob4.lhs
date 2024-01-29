>grade :: Int -> Char
>grade n
>      | n < 0 = 'E'
>      | (n-60) < 0  = 'F'
>      | (n-70) < 0  = 'D'
>      | (n-80) < 0  = 'C'
>      | (n-90) < 0  = 'B'
>      | (n-100) < 1 = 'A'
>      | otherwise   = 'E'

>abs2 :: Int -> Int
>abs2 n = -1 * n

