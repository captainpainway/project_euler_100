import Data.List

threesAndFives x = sum ([3,6..(x - 1)] `union` [5,10..(x - 1)])
