use warnings;
open(FH,"fasta.txt")||die ($!);


while ($dna = <FH>){

if($dna!~/^>/){
$count = ( $dna=~ tr/GC//);
$sum+=$count;
}
}
