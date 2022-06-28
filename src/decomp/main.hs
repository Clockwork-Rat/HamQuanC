import System.Environment
import Data.List

main = do
    args <- getArgs -- IO [String]
    progName <- getProgName
    --putStrLn  "The Arguments Are:"
    --mapM putStrLn args
    let size = (read (args !! 0) :: Integer)
    let s = show size
    putStrLn s

    if size == 0 
        then putStrLn "not correct"
    else if size == 2 
        then putStrLn "Size is 2"
    else putStrLn "Size is wrong"
    
    --putStrLn "The Program Name Is:"
    --putStrLn progName

