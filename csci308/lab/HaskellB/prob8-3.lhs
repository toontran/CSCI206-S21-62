>mrg :: [Int] -> [Int] -> [Int]
>mrg l1 l2 = if l1 == [] then l2 else
>               if l2 == [] then l1 else
>               if head l1 < head l2
>                   then head l1 : (mrg (tail l1) l2)
>                   else head l2 : (mrg l1 (tail l2))

