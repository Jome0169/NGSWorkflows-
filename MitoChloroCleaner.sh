


refGenome="MelonGenome.scf.fasta"
MitoGenome="CucumisSatMito.fasta"
ChloroGenome="CucumisSatChloro.fasta"



makeblastdb -in $refGenome -parse_seqids -dbtype nucl

blastn -db $regGenome -query $MitoGenome -outfrmt 7 
blastn -db $regGenome -query $ChloroGenome -outfrmt 7 











