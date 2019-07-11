foreach($line in Get-Content .\test.txt) {
    if($line -match $regex){
        docker rm $line
    }
}