>next :: [Int] -> [Int]
>next l = zipWith (+) (zipWith (+) ([0] ++ [0] ++ l) ([0] ++ l ++ [0])) (l ++ [0] ++ [0])

>tris :: [Int] -> [[Int]]
>tris l = l : tris (next l)

>triangle :: Int -> [[Int]]
>triangle n = [n] : [next x | x <- tris [n]]

