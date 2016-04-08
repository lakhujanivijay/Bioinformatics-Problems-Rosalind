use warnings;

open(FH, '73329NO11D216835YS_S11_L001_R2_001.fastq')  || die("could not be opened");
open(FG, ">",'result.fasta')  || die("could not be openend");

@file=<FH>;
$count=0;

foreach $file(@file){
	if($file=~/^[ATGC]/ && $file!~/>/ && $file!~/\// && $file!~/\?/ && $file!~/@/){
	$count++;
	print FG ">Read:$count\n$file\n";
	}
	}
