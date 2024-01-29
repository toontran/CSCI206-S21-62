>next :: [Int] -> Int -> [Int]
>next [] _ = []
>next l 0 = next l (head (reverse l))
>next (h:l) k = k:((h+k):(next l (h+k)))


>tris :: [Int] -> [[Int]]
>tris l = l : tris (next l 0)

>triangle :: Int -> [[Int]]
>triangle n = [n] : [x | x <- tris [n]]