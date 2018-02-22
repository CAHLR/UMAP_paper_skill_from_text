
 trap ctrl_c INT

 function ctrl_c() {
         break
 }

 for ((i=1;i < 2;i++)) {
     x=$i
     fname="Main/BOW/""main"$x".py"
     screen -dmS "BOW-&&-$i" python $fname
 }
