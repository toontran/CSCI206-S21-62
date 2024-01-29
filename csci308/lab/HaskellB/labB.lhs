>roots :: Int -> Int -> Int -> (Float, Float)
>roots x y z = if ( (a == 0) || (delta < 0) )
>                 then error "No real roots\n"
>                 else ( (-b+sqrt(delta)) / (2*a), (-b-sqrt(delta)) / (2*a))
>              where 
>                   a = fromIntegral x
>                   b = fromIntegral y
>                   c = fromIntegral z
>                   delta = b^2 - 4*a*c 


>allRoots :: Int -> Int -> Int -> ((Float, Float), (Float, Float))
>allRoots x y z = if (a == 0)
>                 then error "No real roots\n"
>                 else if (delta >= 0)
>                 then ( ((-b+sqrt(delta)) / (2*a), 0), ((-b-sqrt(delta)) / (2*a), -0) )
>                 else ( ((-b)/(2*a),(sqrt(-delta))/(2*a)), ((-b)/(2*a),(-sqrt(-delta))/(2*a)) )
>              where 
>                   a = fromIntegral x
>                   b = fromIntegral y
>                   c = fromIntegral z
>                   delta = b^2 - 4*a*c 

>firstLast :: [Int] -> [Int]
>firstLast [] = error "Empty list\n"
>firstLast (x:y) = if length y == 0
>                   then []
>                   else reverse(tail (reverse y)) 

>strip :: Int -> [Int] -> [Int]
>strip n l = drop n (reverse (drop n (reverse l)))

>mrg :: [Int] -> [Int] -> [Int]
>mrg (a:b) (x:y) = if a < x
>                   then a : (mrg b (x:y))
>                   else x : (mrg (a:b) y)
 
>simpRat :: (Int, Int) -> (Int, Int)
>simpRat (a, b) = (div a d, div b d)
>                   where d = gcd a b  

>addRat :: (Int, Int) -> (Int, Int) -> (Int, Int)
>addRat (a, 0) (x, y) = error "Can't divide by zero!\n"
>addRat (a, b) (x, 0) = error "Can't divide by zero!\n"
>addRat (a, b) (x, y) = simpRat (a*y + x*b, b*y)
 
>mrg2 :: [Int] -> [Int] -> [Int]
>mrg2 [] l = l
>mrg2 l [] = l
>mrg2 (a:b) (x:y) = if a < x
>                   then a : (mrg b (x:y))
>                   else x : (mrg (a:b) y)

>sorted :: [Int] -> Bool
>sorted [] = True
>sorted [x] = True
>sorted (x:y:z) = if x <= y 
>                   then sorted (y:z)
>                   else False

>mySum :: [Int] -> Int
>mySum x = foldr (+) 0 x
