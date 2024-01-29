>import Data.Char

>convert2Int :: [Char] -> Int
>convert2Int l = foldl (\x y -> x*10 + y) 0 (map digitToInt l)

>digitHexToInt c = case c of 
>                   'a' -> 10
>                   'b' -> 11
>                   'c' -> 12
>                   'd' -> 13
>                   'e' -> 14
>                   'f' -> 15
>                   _ -> digitToInt c

>convertHex2Int :: [Char] -> Int
>convertHex2Int ('0':'x':l) = foldl (\x y -> x*16 + y) 0 (map digitHexToInt l)

>stdev :: [Float] -> Float
>stdev l = sqrt $ foldl (\x y -> x + 1/ fromIntegral(length(l)) * (y-mu)**2) 0 l
>               where mu = (sum l) / fromIntegral(length l)

>insert :: Ord a => [a] -> a -> [a]
>insert [] n = [n]
>insert l n = [x | x <- l, x < n] ++
>                 [n] ++
>                 [x | x <- l, x >= n]

>myMap :: (a->b) -> [a] -> [b]
>myMap f l = [f x | x <- l]

>divisors n = [x | x <- [2..n], mod n x == 0]

>prime n = (foldl (\x (i,e) -> x * (mod e i)) 1 (zip [2..n-1] [n,n..])) /= 0 

>factors :: Int -> [Int]
>factors n = [x | x <- divisors(n), prime x]


